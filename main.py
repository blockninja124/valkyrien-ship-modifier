import tkinter as tk
from menu import ask_for_file, onSaveButton, onCloseButton
import globals

globals.is_modified = False

globals.root = tk.Tk()
globals.root.title("VS ship editor")
globals.root.geometry("500x500")

globals.item_buttons_frame = tk.Frame(globals.root)

globals.file_buttons_frame = tk.Frame(globals.root)
button3 = tk.Button(globals.file_buttons_frame, text="Save", command=onSaveButton)
button3.pack(side="left", padx=100, pady=10)
button4 = tk.Button(globals.file_buttons_frame, text="Close", command=onCloseButton)
button4.pack(side="right", padx=100, pady=10)

button = tk.Button(globals.item_buttons_frame)
button.pack()
button2 = tk.Button(globals.item_buttons_frame)
button2.pack()



button = tk.Button(globals.root, text="Open File", command=lambda: ask_for_file(button))
button.pack(pady=40)

globals.root.mainloop()







    
    


