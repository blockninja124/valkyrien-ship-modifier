import tkinter as tk
from tkinter import ttk
from tkinterutils import SearchableTreeview

root: tk.Tk
item_buttons_frame: tk.Frame
file_buttons_frame: tk.Frame
filename: str
is_modified: bool
tree_frame: tk.Frame
tree: SearchableTreeview
bool_list = ["True", "False"]