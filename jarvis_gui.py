import tkinter as tk
from tkinter import Canvas, Button, Label
import subprocess
import sys
import threading
import time
from PIL import Image, ImageTk, ImageSequence
import pyttsx3  # Text-to-speech library

class AnimatedGIF:
    def __init__(self, canvas, path, x, y, delay=100):
        self.canvas = canvas
        self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(path))]
        self.index = 0
        self.image_id = canvas.create_image(x, y, anchor=tk.NW, image=self.frames[self.index])
        self.delay = delay
        self.animate()

    def animate(self):
        self.index = (self.index + 1) % len(self.frames)
        self.canvas.itemconfig(self.image_id, image=self.frames[self.index])
        self.canvas.after(self.delay, self.animate)

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS Assistant")
        self.root.geometry("1366x768")
        self.root.config(bg="black")
        self.root.resizable(True, True)  # Allow resizing (min/maximize)

        # Canvas
        self.canvas = Canvas(self.root, width=1366, height=768, highlightthickness=0)
        self.canvas.pack()

        # Load and Animate GIFs
        self.bg_anim = AnimatedGIF(self.canvas, "images/live_wallpaper.gif", 0, 0, 50)

        # Time Label
        self.time_label = Label(self.root, font=("OCR A Extended", 16), fg="cyan", bg="black")
        self.time_label.place(x=20, y=20)
        self.update_time()

        # RUN Button
        self.run_btn = Button(self.root, text="RUN", font=("OCR A Extended", 16), bg="yellow", fg="black", command=self.run_jarvis)
        self.run_btn.place(x=1100, y=650)

        # EXIT Button
        self.exit_btn = Button(self.root, text="EXIT", font=("OCR A Extended", 16), bg="red", fg="white", command=self.exit_program)
        self.exit_btn.place(x=1200, y=650)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text="Time: " + current_time)
        self.root.after(1000, self.update_time)

    def run_jarvis(self):
        print("RUN button clicked.")
        # Run in a new thread to avoid blocking the main GUI thread
        threading.Thread(target=self.start_jarvis).start()

    def start_jarvis(self):
        try:
            # Use subprocess to run the index.py script without blocking the main thread
            subprocess.Popen([sys.executable, "index.py"])  # Runs index.py as a new process
        except Exception as e:
            print("Error running JARVIS:", e)

    def exit_program(self):
        # Display Goodbye message in the console and say goodbye aloud
        print("Goodbye! Have a nice day.")
        self.say_goodbye()  # Make the assistant say goodbye aloud
        self.root.quit()  # Close the window immediately after saying goodbye

    def say_goodbye(self):
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Set speech speed
        engine.setProperty('volume', 1)  # Set volume (0.0 to 1.0)
        engine.say("Goodbye! Have a nice day.")
        engine.runAndWait()

# Start the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import tkinter as tk
# # from tkinter import Canvas, Button, Label
# # import subprocess
# # import sys
# # import threading
# # import time
# # from PIL import Image, ImageTk, ImageSequence
# #
# # class AnimatedGIF:
# #     def __init__(self, canvas, path, x, y, delay=100):
# #         self.canvas = canvas
# #         self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(path))]
# #         self.index = 0
# #         self.image_id = canvas.create_image(x, y, anchor=tk.NW, image=self.frames[self.index])
# #         self.delay = delay
# #         self.animate()
# #
# #     def animate(self):
# #         self.index = (self.index + 1) % len(self.frames)
# #         self.canvas.itemconfig(self.image_id, image=self.frames[self.index])
# #         self.canvas.after(self.delay, self.animate)
# #
# # class JarvisGUI:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("JARVIS Assistant")
# #         self.root.geometry("1366x768")
# #         self.root.config(bg="black")
# #         self.root.resizable(True, True)  # Allow resizing (min/maximize)
# #
# #         # Canvas
# #         self.canvas = Canvas(self.root, width=1366, height=768, highlightthickness=0)
# #         self.canvas.pack()
# #
# #         # Load and Animate GIFs
# #         self.bg_anim = AnimatedGIF(self.canvas, "images/live_wallpaper.gif", 0, 0, 50)
# #
# #         # Time Label
# #         self.time_label = Label(self.root, font=("OCR A Extended", 16), fg="cyan", bg="black")
# #         self.time_label.place(x=20, y=20)
# #         self.update_time()
# #
# #         # RUN Button
# #         self.run_btn = Button(self.root, text="RUN", font=("OCR A Extended", 16), bg="yellow", fg="black", command=self.run_jarvis)
# #         self.run_btn.place(x=1100, y=650)
# #
# #         # EXIT Button
# #         self.exit_btn = Button(self.root, text="EXIT", font=("OCR A Extended", 16), bg="red", fg="white", command=self.exit_program)
# #         self.exit_btn.place(x=1200, y=650)
# #
# #     def update_time(self):
# #         current_time = time.strftime("%H:%M:%S")
# #         self.time_label.config(text="Time: " + current_time)
# #         self.root.after(1000, self.update_time)
# #
# #     def run_jarvis(self):
# #         print("RUN button clicked.")
# #         # Run in a new thread to avoid blocking the main GUI thread
# #         threading.Thread(target=self.start_jarvis).start()
# #
# #     def start_jarvis(self):
# #         try:
# #             # Use subprocess to run the index.py script without blocking the main thread
# #             subprocess.Popen([sys.executable, "index.py"])  # Runs index.py as a new process
# #         except Exception as e:
# #             print("Error running JARVIS:", e)
# #
# #     def exit_program(self):
# #         # Display Goodbye message and then close the window
# #         print("Goodbye! Have a nice day.")
# #         self.canvas.create_text(683, 384, text="Goodbye! Have a nice day.", fill="cyan", font=("OCR A Extended", 24))
# #         self.root.after(2000, self.root.quit)  # Close the window after 2 seconds
# #
# # # Start the GUI
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = JarvisGUI(root)
# #     root.mainloop()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # from tkinter import *
# # # from PIL import Image, ImageTk, ImageSequence
# # # import time
# # # import threading
# # # import importlib
# # # import sys
# # #
# # # class AnimatedGIF:
# # #     def __init__(self, canvas, path, x, y, delay=100):
# # #         self.canvas = canvas
# # #         self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(path))]
# # #         self.index = 0
# # #         self.image_id = canvas.create_image(x, y, anchor=NW, image=self.frames[self.index])
# # #         self.delay = delay
# # #         self.animate()
# # #
# # #     def animate(self):
# # #         self.index = (self.index + 1) % len(self.frames)
# # #         self.canvas.itemconfig(self.image_id, image=self.frames[self.index])
# # #         self.canvas.after(self.delay, self.animate)
# # #
# # # class JarvisGUI:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("JARVIS Assistant")
# # #         self.root.geometry("1366x768")
# # #         self.root.config(bg="black")
# # #         self.root.resizable(True, True)  # Allow resizing (min/maximize)
# # #
# # #         # Canvas
# # #         self.canvas = Canvas(self.root, width=1366, height=768, highlightthickness=0)
# # #         self.canvas.pack()
# # #
# # #         # Load and Animate GIFs
# # #         self.bg_anim = AnimatedGIF(self.canvas, "images/live_wallpaper.gif", 0, 0, 50)
# # #
# # #         # Time Label
# # #         self.time_label = Label(self.root, font=("OCR A Extended", 16), fg="cyan", bg="black")
# # #         self.time_label.place(x=20, y=20)
# # #         self.update_time()
# # #
# # #         # RUN Button
# # #         self.run_btn = Button(self.root, text="RUN", font=("OCR A Extended", 16), bg="yellow", fg="black", command=self.run_jarvis)
# # #         self.run_btn.place(x=1100, y=650)
# # #
# # #         # EXIT Button
# # #         self.exit_btn = Button(self.root, text="EXIT", font=("OCR A Extended", 16), bg="red", fg="white", command=self.exit_program)
# # #         self.exit_btn.place(x=1200, y=650)
# # #
# # #     def update_time(self):
# # #         current_time = time.strftime("%H:%M:%S")
# # #         self.time_label.config(text="Time: " + current_time)
# # #         self.root.after(1000, self.update_time)
# # #
# # #     def run_jarvis(self):
# # #         print("RUN button clicked.")
# # #         # Run in a new thread to avoid blocking the main GUI thread
# # #         threading.Thread(target=self.start_jarvis).start()
# # #
# # #     def start_jarvis(self):
# # #         try:
# # #             # Import and run the main index.py script
# # #             import index  # assuming index.py is in the same directory as this GUI file
# # #             index.main()  # If index.py has a main function to run the assistant, use that
# # #         except Exception as e:
# # #             print("Error running JARVIS:", e)
# # #
# # #     def exit_program(self):
# # #         # Display Goodbye message and then close the window
# # #         print("Goodbye! Have a nice day.")
# # #         self.canvas.create_text(683, 384, text="Goodbye! Have a nice day.", fill="cyan", font=("OCR A Extended", 24))
# # #         self.root.after(2000, self.root.quit)  # Close the window after 2 seconds
# # #
# # # # Start the GUI
# # # if __name__ == "__main__":
# # #     root = Tk()
# # #     app = JarvisGUI(root)
# # #     root.mainloop()
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # from tkinter import *
# # # # from PIL import Image, ImageTk, ImageSequence
# # # # import time
# # # # import threading
# # # # import os
# # # #
# # # # class AnimatedGIF:
# # # #     def __init__(self, canvas, path, x, y, delay=100):
# # # #         self.canvas = canvas
# # # #         self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(path))]
# # # #         self.index = 0
# # # #         self.image_id = canvas.create_image(x, y, anchor=NW, image=self.frames[self.index])
# # # #         self.delay = delay
# # # #         self.animate()
# # # #
# # # #     def animate(self):
# # # #         self.index = (self.index + 1) % len(self.frames)
# # # #         self.canvas.itemconfig(self.image_id, image=self.frames[self.index])
# # # #         self.canvas.after(self.delay, self.animate)
# # # #
# # # # class JarvisGUI:
# # # #     def __init__(self, root):
# # # #         self.root = root
# # # #         self.root.title("JARVIS Assistant")
# # # #         self.root.geometry("1366x768")
# # # #         self.root.config(bg="black")
# # # #         self.root.resizable(True, True)  # Allow resizing (min/maximize)
# # # #
# # # #         # Canvas
# # # #         self.canvas = Canvas(self.root, width=1366, height=768, highlightthickness=0)
# # # #         self.canvas.pack()
# # # #
# # # #         # Load and Animate GIFs
# # # #         self.bg_anim = AnimatedGIF(self.canvas, "images/live_wallpaper.gif", 0, 0, 50)
# # # #
# # # #         # Time Label
# # # #         self.time_label = Label(self.root, font=("OCR A Extended", 16), fg="cyan", bg="black")
# # # #         self.time_label.place(x=20, y=20)
# # # #         self.update_time()
# # # #
# # # #         # RUN Button
# # # #         self.run_btn = Button(self.root, text="RUN", font=("OCR A Extended", 16), bg="yellow", fg="black", command=self.run_jarvis)
# # # #         self.run_btn.place(x=1100, y=650)
# # # #
# # # #         # EXIT Button
# # # #         self.exit_btn = Button(self.root, text="EXIT", font=("OCR A Extended", 16), bg="red", fg="white", command=self.root.quit)
# # # #         self.exit_btn.place(x=1200, y=650)
# # # #
# # # #     def update_time(self):
# # # #         current_time = time.strftime("%H:%M:%S")
# # # #         self.time_label.config(text="Time: " + current_time)
# # # #         self.root.after(1000, self.update_time)
# # # #
# # # #     def run_jarvis(self):
# # # #         print("RUN button clicked.")
# # # #         # Run in a new thread to avoid blocking the main GUI thread
# # # #         threading.Thread(target=self.start_jarvis).start()
# # # #
# # # #     def start_jarvis(self):
# # # #         try:
# # # #             # Running JARVIS in a separate thread
# # # #             os.system("python index.py")  # or import index and run its function
# # # #         except Exception as e:
# # # #             print("Error running JARVIS:", e)
# # # #
# # # # # Start the GUI
# # # # if __name__ == "__main__":
# # # #     root = Tk()
# # # #     app = JarvisGUI(root)
# # # #     root.mainloop()
