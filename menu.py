import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import shutil
from tkinter import Event, ttk
from ship_nbt import readShipsFile, writeShipsFile
from treeutils import add_dic_to_tree, list_to_dict, tree_to_dict

import globals

def ask_for_file(button):
    globals.is_modified = False
    
    filename = tkinter.filedialog.askopenfilename(
        title="Select a VS ship data file:",
        filetypes=[
            ("VS ship data files", "vs_ship_data.dat"),
            ("NBT data files", "*.dat")
        ]
    )
    if filename:
        print(f"Selected file: {filename}")
        on_file_selected(button, filename)

def on_file_selected(button, filename):
        button.pack_forget()
        
        globals.tree = ttk.Treeview(globals.root)
        globals.tree.bind("<<TreeviewSelect>>", treeviewSelect)

        globals.tree.pack(fill=tk.BOTH, expand=True)

        globals.file_buttons_frame.pack(after=globals.tree, side="bottom")
        
        globals.filename = filename

        ships_dic = readShipsFile(filename)
        
        parent = globals.tree.insert("", "end", text="Ships-list")
        add_dic_to_tree(list_to_dict(ships_dic["ships"]), globals.tree, parent, 0)
        
        globals.tree.bind("<Double-1>", on_double_click)
        
def on_double_click(event):
    
    item_id = globals.tree.identify_row(event.y)
    if not item_id or (globals.tree.get_children(item = item_id) != ()):
        return

    x, y, width, height = globals.tree.bbox(item_id)
    
    value = globals.tree.item(item_id)['text']

    isBool = False
    if value in globals.bool_list:
        isBool = True
        
    entry = tk.Entry(globals.root)
    entry.place(x=x, y=y + globals.tree.winfo_y(), width=width, height=height)
    entry.insert(0, value)
    entry.focus()

    def validate_input(new_val):
        # If it was a number, it stays a number
        if isinstance(value, int):
            return new_val.lstrip("-").isdigit() or new_val == ""
        
        # We don't know what null values are meant to be, so we can't edit them
        if value == "null":
            return False
        
        return True

    vcmd = (globals.root.register(validate_input), "%P")
    entry.config(validate="key", validatecommand=vcmd)

    def save_edit(event=None):
        if isBool:
            if entry.get() not in globals.bool_list:
                # If it was a boolean, but they didn't put in a boolean, cancel saving
                entry.destroy()
                return
            
        globals.is_modified = True
        new_value = entry.get()
        globals.tree.item(item_id, text=new_value)
        entry.destroy()

    entry.bind("<Return>", save_edit)
    entry.bind("<FocusOut>", lambda e: entry.destroy())

def treeviewSelect(event: Event):
    selected = globals.tree.selection()
    if selected == ():            
        globals.item_buttons_frame.pack_forget()
        return
    
    globals.item_buttons_frame.pack(after=globals.file_buttons_frame, side="top")

    
def onCloseButton():
    if globals.is_modified:
        action = tkinter.messagebox.Message(
            title="Confirm Exit", 
            message="Are you sure?", 
            detail="You have unsaved changes that will be lost", 
            icon=tkinter.messagebox.WARNING, 
            type=tkinter.messagebox.OKCANCEL
        ).show()

        if action == "cancel":
            return
    globals.root.quit()


def onSaveButton():

    if not globals.is_modified:
        return

    action = tkinter.messagebox.Message(
        title="Confirm Save", 
        message="Are you sure?", 
        detail="This will overwrite your ships.dat", 
        icon=tkinter.messagebox.WARNING, 
        type=tkinter.messagebox.OKCANCEL
    ).show()

    if action == "cancel":
        return
    
    shutil.copy(globals.filename,  globals.filename+"_old")

    try:
        tree_dict = tree_to_dict(globals.tree, "")
        ships_dic = readShipsFile(globals.filename)

        ships_dic['ships'] = tree_dict['Ships']

        writeShipsFile(globals.filename, ships_dic)
    except Exception as e:
        tkinter.messagebox.Message(
            title="Error", 
            message="Error saving file:", 
            detail=str(e), 
            icon=tkinter.messagebox.ERROR, 
            type=tkinter.messagebox.OK
        ).show()
    else:
        tkinter.messagebox.Message(
            title="Success", 
            message="File saved!", 
            detail="", 
            icon=tkinter.messagebox.INFO, 
            type=tkinter.messagebox.OK
        ).show()
    finally:
        globals.is_modified = False
    
    







"""
def try_open_menu(event):
    selected = globals.tree.selection()

    print(tree_to_dict(globals.tree, ""))

    if selected != ():
        m = tk.Menu(globals.root, tearoff=0)
        m.add_command(label="Cut")
        m.add_command(label="Copy")
        m.add_command(label="Paste")
        m.add_command(label="Reload")
        m.add_separator()
        m.add_command(label="Rename")
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()

"""