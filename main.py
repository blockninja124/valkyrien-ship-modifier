import tkinter as tk
from menu import ask_for_file, onSaveButton, onCloseButton, on_search, on_reset
import globals

globals.is_modified = False

globals.root = tk.Tk()
globals.root.title("VS ship editor")
globals.root.geometry("500x500")

globals.tree_frame = tk.Frame(globals.root)
globals.tree_frame.pack(side="top", fill="both", expand=True)

globals.item_buttons_frame = tk.Frame(globals.root)

globals.file_buttons_frame = tk.Frame(globals.root)

entry = tk.Entry(globals.file_buttons_frame)
entry.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=2)
button = tk.Button(globals.file_buttons_frame, text="Search", command=lambda: on_search(entry))
button.grid(row=0, column=2, sticky="nsew", pady=2)
button2 = tk.Button(globals.file_buttons_frame, text="Reset Search", command=on_reset)
button2.grid(row=0, column=3, sticky="nsew", pady=2)

button3 = tk.Button(globals.file_buttons_frame, text="Save", command=onSaveButton)
button3.grid(row=1, column=1, sticky="nsew", pady=2)
button4 = tk.Button(globals.file_buttons_frame, text="Close", command=onCloseButton)
button4.grid(row=1, column=2, sticky="nsew", pady=2)

button = tk.Button(globals.tree_frame, text="Open File", command=lambda: ask_for_file(button))
button.pack(pady=40)

globals.root.mainloop()