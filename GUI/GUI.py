"""
GUI Module.

Responsible for setting up the GUI window using glfw, and handling the
backend side of imgui rendering and event polling.
"""

import ctypes
import logging
import sys
from typing import Any, Self

import glfw
import OpenGL.GL as gl
from imgui_bundle import imgui

from memory import (
    boat_manager_handle,
    combat_manager_handle,
    currency_manager_handle,
    inventory_manager_mem_handle,
    level_manager_handle,
    level_up_manager_handle,
    mem_handle,
    new_dialog_manager_handle,
    player_party_manager_handle,
    time_of_day_manager_handle,
    title_sequence_manager_handle,
)

logger = logging.getLogger(__name__)


# Create the window that our GUI/visualization will be in
def create_glfw_window(
    window_name: str = "Sea of Stars TAS", width: int = 480, height: int = 800
) -> Any:  # noqa: ANN401
    """Initialize the glfw window and OpenGL context."""
    if not glfw.init():
        logger.error("Could not initialize OpenGL context")
        sys.exit(1)

    # Set up OpenGL
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(
        width=int(width),
        height=int(height),
        title=window_name,
        monitor=None,
        share=None,
    )
    glfw.make_context_current(window)

    # Check we actually managed to create a window
    if not window:
        glfw.terminate()
        logger.error("Could not initialize glfw window")
        sys.exit(1)

    return window


def update_memory() -> None:
    """Update all game memory modules."""
    mem_handle().update()
    if mem_handle().ready_for_updates:
        level_manager_handle().update()
        scene_name = level_manager_handle().scene_name
        loading = level_manager_handle().loading

        if scene_name == "TitleScreen":
            title_sequence_manager_handle().update()
        elif scene_name is not None and loading is False:
            player_party_manager_handle().update()
            time_of_day_manager_handle().update()
            level_up_manager_handle().update()
            combat_manager_handle().update()
            new_dialog_manager_handle().update()
            inventory_manager_mem_handle().update()
            currency_manager_handle().update()
            if "WorldMap" in scene_name:
                boat_manager_handle().update()


class Window:
    """Class to handle the top level GUI window."""

    def __init__(self: Self, config: dict) -> None:
        super().__init__()

        self.background_color = (0, 0, 0, 1)

        # Create Window/Context and set up renderer
        self.window = create_glfw_window()
        gl.glClearColor(*self.background_color)
        imgui.create_context()

        self.io = imgui.get_io()
        self.io.config_flags |= imgui.ConfigFlags_.nav_enable_keyboard
        self.io.config_flags |= imgui.ConfigFlags_.docking_enable

        imgui.style_colors_dark()

        vsync = config.get("vsync", True)
        glfw.swap_interval(1 if vsync else 0)

        # Setup Platform/Renderer backends

        # You need to transfer the window address to imgui.backends.glfw_init_for_opengl
        # proceed as shown below to get it.
        glsl_version = "#version 150"
        window_address = ctypes.cast(self.window, ctypes.c_void_p).value
        imgui.backends.glfw_init_for_opengl(window_address, True)
        imgui.backends.opengl3_init(glsl_version)

    def is_open(self: Self) -> bool:
        """Return True while the GUI window is open. Return False if the user quits the program."""
        return not glfw.window_should_close(self.window)

    def start_frame(self: Self) -> None:
        """Call at start of frame to handle imgui setup, memory readout and event polling."""
        glfw.poll_events()
        update_memory()
        imgui.backends.opengl3_new_frame()
        imgui.backends.glfw_new_frame()
        imgui.new_frame()

    # TODO(orkaboy): start_window/end_window should be static (or removed)
    def start_window(self: Self, title: str) -> None:
        """Initialize sub-window."""
        imgui.begin(title, True)

    def end_window(self: Self) -> None:
        """Finalize sub-window."""
        imgui.end()

    def end_frame(self: Self) -> None:
        """Finalize drawing. Should be called at the end of each frame."""
        imgui.render()

        gl.glClearColor(*self.background_color)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.backends.opengl3_render_draw_data(imgui.get_draw_data())
        glfw.swap_buffers(self.window)

    def close(self: Self) -> None:
        """Cleanup imgui and cleanly close down glfw."""
        imgui.backends.opengl3_shutdown()
        imgui.backends.glfw_shutdown()
        imgui.destroy_context()

        glfw.destroy_window(self.window)
        glfw.terminate()


class LayoutHelper:
    """
    Provides helper functions for creating GUI elements.

    ```py
    add_spacer()             # Add a horizontal line with some padding.
    add_spacings(n)          # Add n imgui.spacing() elements.
    add_tooltip(text, width) # Add a tooltip to the previous element.
    ```
    """

    @staticmethod
    def add_spacer() -> None:
        """Add a horizontal line with some padding."""
        imgui.spacing()
        imgui.separator()
        imgui.spacing()

    @staticmethod
    def add_spacings(n: int = 2) -> None:
        """Add multiple imgui.spacing() at once."""
        for _ in range(n):
            imgui.spacing()

    @staticmethod
    def add_tooltip(text: str, width: int = 300) -> None:
        """
        Add a tooltip to the previous element.

        Set `width` to `-1` to disable automatic text wrapping.
        """
        if imgui.is_item_hovered(flags=imgui.HoveredFlags_.delay_normal) and imgui.begin_tooltip():
            imgui.set_next_window_size(size=imgui.ImVec2(0.0, 0.0))  # auto-fit tooltip to content
            imgui.push_text_wrap_pos(width)
            imgui.text_unformatted(text)
            imgui.pop_text_wrap_pos()
            imgui.end_tooltip()
