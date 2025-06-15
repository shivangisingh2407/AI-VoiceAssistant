import tkinter as tk


def create_notepad():
    root = tk.Tk()
    root.title("JARVIS Notepad")

    text_area = tk.Text(root, wrap='word', width=60, height=20)
    text_area.pack(expand='true', fill='both')

    def save_note():
        with open("note.txt", "w") as file:
            file.write(text_area.get(1.0, tk.END))

    def open_note():
        try:
            with open("note.txt", "r") as file:
                text_area.insert(tk.END, file.read())
        except FileNotFoundError:
            pass

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Save", command=save_note)
    file_menu.add_command(label="Open", command=open_note)
    menu_bar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menu_bar)

    root.mainloop()


create_notepad()
