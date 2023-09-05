import logging
import sys

import glfw
import imgui
import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer

from memory.boat_manager import boat_manager_handle
from memory.combat_manager import combat_manager_handle
from memory.core import mem_handle
from memory.level_manager import level_manager_handle
from memory.player_party_manager import player_party_manager_handle
from memory.title_sequence_manager import title_sequence_manager_handle

logger = logging.getLogger(__name__)


# Create the window that our GUI/visualization will be in
def create_glfw_window(window_name="Sea of Stars TAS", width=600, height=720):
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


def update_memory():
    mem_handle().update()
    if mem_handle().ready_for_updates:
        level_manager_handle().update()
        scene_name = level_manager_handle().scene_name
        loading = level_manager_handle().loading

        if scene_name == "TitleScreen":
            title_sequence_manager_handle().update()
        elif scene_name is not None and loading is False:
            player_party_manager_handle().update()
            combat_manager_handle().update()
            if "WorldMap" in scene_name:
                boat_manager_handle().update()


class Window:
    def __init__(self, config: dict) -> None:
        super().__init__()

        self.backgroundColor = (0, 0, 0, 1)

        # Create Window/Context and set up renderer
        self.window = create_glfw_window()
        gl.glClearColor(*self.backgroundColor)
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)
        vsync = config.get("vsync", True)
        glfw.swap_interval(1 if vsync else 0)

    def is_open(self) -> bool:
        return not glfw.window_should_close(self.window)

    def start_frame(self) -> None:
        glfw.poll_events()
        update_memory()
        self.impl.process_inputs()
        imgui.new_frame()

    def start_window(self, title: str) -> None:
        imgui.begin(title, True)

    # Finalize window
    def end_window(self) -> None:
        imgui.end()

    # Finalize drawing
    def end_frame(self) -> None:
        imgui.render()

        gl.glClearColor(*self.backgroundColor)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        self.impl.render(imgui.get_draw_data())
        glfw.swap_buffers(self.window)

    # Cleanup
    def close(self) -> None:
        self.impl.shutdown()
        glfw.terminate()


class GUI_helper:
    """
    This class provides helper functions for creating GUI elements.

    Methods:
        add_spacer():
            Adds a horizontal line with some padding."""

    def add_spacer():
        """Adds a horizontal line with some padding."""
        imgui.spacing()
        imgui.separator()
        imgui.spacing()
