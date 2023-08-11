import imgui
from GUI import Window

# Temporary window
class SoSWindow(Window):
    def __init__(self) -> None:
        super().__init__()
        # Local state
        self.string = ""
        self.f = 0.5

    def draw_window(self) -> None:
        # Print some text
        imgui.text("Hello, world!")
        # A button
        if imgui.button("OK"):
            print(f"String: {self.string}")
            print(f"Float: {self.f}")
        # Set up some interactive values
        _, self.string = imgui.input_text("A String", self.string, 256)
        _, self.f = imgui.slider_float("float", self.f, 0.25, 1.5)


if __name__ == "__main__":
    gui = SoSWindow()
    # Main loop
    while(gui.is_open()):
        gui.start_frame()
        # Create a window and draw it
        gui.start_window("Custom window")
        gui.draw_window()
        gui.end_window()
        # End of imgui frame (render)
        gui.end_frame()
    # Cleanup
    gui.close()
