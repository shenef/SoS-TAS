import imgui
import glfw
import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer


# Create the window that our GUI/visualization will be in
def create_glfw_window(window_name="Sea of Stars TAS", width=1280, height=720):
    if not glfw.init():
        print("Could not initialize OpenGL context")
        exit(1)

    # Set up OpenGL
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(width=int(width), height=int(height), title=window_name, monitor=None, share=None)
    glfw.make_context_current(window)

    # Check we actually managed to create a window
    if not window:
        glfw.terminate()
        print("Could not initialize glfw window")
        exit(1)

    return window


class Window(object):
    def __init__(self) -> None:
        super().__init__()

        self.backgroundColor = (0, 0, 0, 1)

        # Create Window/Context and set up renderer
        self.window = create_glfw_window()
        gl.glClearColor(*self.backgroundColor)
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)

    def is_open(self) -> bool:
        return not glfw.window_should_close(self.window)


    def start_frame(self) -> None:
        glfw.poll_events()
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

