import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS")
        self.root.geometry("800x600")  # Set window size
        self.root.configure(bg="black")  # Set background color to black

        # Load the GIF file
        self.gif_path = os.path.join(os.path.dirname(__file__), "jarvis.gif")  # Replace with your GIF file path
        if not os.path.exists(self.gif_path):
            raise FileNotFoundError(f"GIF file not found at {self.gif_path}")

        self.load_gif(self.gif_path)

        # Center the window on the screen
        self.center_window()

    def load_gif(self, gif_path):
        """Load and display the GIF file."""
        self.gif = Image.open(gif_path)
        self.frames = []
        try:
            while True:
                frame = ImageTk.PhotoImage(self.gif.copy())
                self.frames.append(frame)
                self.gif.seek(len(self.frames))  # Move to the next frame
        except EOFError:
            pass

        self.gif_label = ttk.Label(self.root, image=self.frames[0], background="black")
        self.gif_label.pack(expand=True)  # Center the GIF in the window

        self.animate(0)

    def animate(self, frame_index):
        """Animate the GIF."""
        frame = self.frames[frame_index]
        self.gif_label.configure(image=frame)
        frame_index = (frame_index + 1) % len(self.frames)
        self.root.after(100, self.animate, frame_index)  # Update every 100ms

    def center_window(self):
        """Center the window on the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2  # Adjust for window width
        y = (screen_height - 600) // 2  # Adjust for window height
        self.root.geometry(f"800x600+{x}+{y}")

# Define the start_gui function
def start_gui():
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()