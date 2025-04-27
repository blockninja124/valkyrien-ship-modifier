from tkinter import ttk
import globals

def add_dic_to_tree(dic: dict, tree: ttk.Treeview, parent: str, r_count: int):
    if r_count > 20:
        print("Warning: recursion limit hit. Returning early")
    
    for key, val in dic.items():
        if val == None:
            val = "null"
        
        if isinstance(val, dict):
            new_parent = tree.insert(parent, "end", text=key)
            add_dic_to_tree(val, tree, new_parent, r_count + 1)
        elif isinstance(val, list):
            new_parent = tree.insert(parent, "end", text=key+"-list")
            add_dic_to_tree(list_to_dict(val), tree, new_parent, r_count + 1)
        else:
            if isinstance(val, bool):
                val = str(val)
            new_parent = tree.insert(parent, "end", text=key)
            tree.insert(new_parent, "end", text=val)

def tree_to_dict(tree: ttk.Treeview, parent: str) -> dict:
    result = {}
    children = tree.get_children(parent)

    for child in children:
        text = tree.item(child, "text")
        grand_children = tree.get_children(child)

        if grand_children:
            # Single value keys will have grand-children,
            # but it will be a single item tuple e.g. ('I0001',).
            # So if they have only 1 grand child, simply use that as their value.
            # But also make sure the single-child doesn't have children of its own.
            if len(grand_children) == 1 and not tree.get_children(grand_children[0]):
                value_text = tree.item(grand_children[0], "text")
                
                # null (json) -> None (python) -> "null" (Tkinter) -> None (python) -> null (json)
                # This is "null" (Tkinter) -> None (python)
                if value_text == "null":
                    result[text] = None
                # Convert to literal bool
                elif value_text in globals.bool_list:
                    result[text] = (value_text == "True")
                else:
                    result[text] = value_text
            
            # We're a list or dict key
            else:
                is_list = str(text).endswith("-list")
                nested = tree_to_dict(tree, child)

                if is_list:
                    # Sort list items by their index (we named them 0, 1, etc when adding to treeview)
                    list_items = [
                        nested[key]
                        for key in sorted(
                            nested.keys(),
                            key=lambda x: x
                        )
                    ]
                    result[text[:-5]] = list_items

                else:
                    result[text] = nested

        # No grandchildren is when a key-node has no value (null)
        # E.g. {"GravityForcesInducer": {}} will have no grandchildren
        # Since {} isn't added as a node to the treeview
        else:
            if (str(text).endswith("-list")):
                result[text[:-5]] = []
            else:
                result[text] = {}

    return result



def list_to_dict(l):
    return {index: value for index, value in enumerate(l)}