import logging
import sys
from typing import Any, Self

import glfw
import OpenGL.GL as gl
from imgui_bundle import imgui

from memory import (
    boat_manager_handle,
    combat_manager_handle,
    level_manager_handle,
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
            combat_manager_handle().update()
            new_dialog_manager_handle().update()
            if "WorldMap" in scene_name:
                boat_manager_handle().update()


class Window:
    def __init__(self: Self, config: dict) -> None:
        super().__init__()

        self.backgroundColor = (0, 0, 0, 1)

        # Create Window/Context and set up renderer
        self.window = create_glfw_window()
        gl.glClearColor(*self.backgroundColor)
        imgui.create_context()

        self.io = imgui.get_io()
        self.io.config_flags |= imgui.ConfigFlags_.nav_enable_keyboard
        self.io.config_flags |= imgui.ConfigFlags_.docking_enable

        imgui.style_colors_dark()

        vsync = config.get("vsync", True)
        glfw.swap_interval(1 if vsync else 0)

        # Setup Platform/Renderer backends
        import ctypes

        # You need to transfer the window address to imgui.backends.glfw_init_for_opengl
        # proceed as shown below to get it.
        glsl_version = "#version 150"
        window_address = ctypes.cast(self.window, ctypes.c_void_p).value
        imgui.backends.glfw_init_for_opengl(window_address, True)
        imgui.backends.opengl3_init(glsl_version)

    def is_open(self: Self) -> bool:
        return not glfw.window_should_close(self.window)

    def start_frame(self: Self) -> None:
        glfw.poll_events()
        update_memory()
        imgui.backends.opengl3_new_frame()
        imgui.backends.glfw_new_frame()
        imgui.new_frame()

    def start_window(self: Self, title: str) -> None:
        imgui.begin(title, True)

    # Finalize window
    def end_window(self: Self) -> None:
        imgui.end()

    # Finalize drawing
    def end_frame(self: Self) -> None:
        imgui.render()

        gl.glClearColor(*self.backgroundColor)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.backends.opengl3_render_draw_data(imgui.get_draw_data())
        glfw.swap_buffers(self.window)

    # Cleanup
    def close(self: Self) -> None:
        imgui.backends.opengl3_shutdown()
        imgui.backends.glfw_shutdown()
        imgui.destroy_context()

        glfw.destroy_window(self.window)
        glfw.terminate()


class LayoutHelper:
    """
    This class provides helper functions for creating GUI elements.

    add_spacer():
        Adds a horizontal line with some padding.

    add_spacings(n)
        Adds n imgui.spacing() elements.

    add_tooltip(text)
        Adds a tooltip to the previous element."""

    def add_spacer() -> None:
        """Adds a horizontal line with some padding."""
        imgui.spacing()
        imgui.separator()
        imgui.spacing()

    def add_spacings(n: int) -> None:
        """Adds multiple imgui.spacing() at once."""
        for _ in range(n):
            imgui.spacing()

    def add_tooltip(text: str) -> None:
        """Adds a tooltip to the previous element."""
        if imgui.is_item_hovered():
            imgui.set_tooltip(text)
