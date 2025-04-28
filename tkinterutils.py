import tkinter as tk
from tkinter import ttk

class SearchableTreeview(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.search_matches = []
        self.original_open_states = {}

        self.tag_configure("highlight", background="yellow")

    def search(self, search_text):
        self.reset_search()

        for item in self.get_children_recursively():
            item_text = self.item(item, "text")
            if str(search_text).lower() in str(item_text).lower():
                self.search_matches.append(item)

                # Expand all parents
                parent = self.parent(item)
                while parent:
                    if parent not in self.original_open_states:
                        self.original_open_states[parent] = self.item(parent, "open")
                    self.item(parent, open=True)
                    parent = self.parent(parent)

                self.item(item, tags=("highlight",))

        # Scroll to the first match
        if self.search_matches:
            self.see(self.search_matches[-1])

    def reset_search(self):
        # Clear highlights
        for item in self.search_matches:
            self.item(item, tags=())

        # Restore original open/closed states
        for item, was_open in self.original_open_states.items():
            self.item(item, open=was_open)

        self.search_matches.clear()
        self.original_open_states.clear()

    def get_children_recursively(self, item=""):
        children = []
        stack = list(self.get_children(item))
        while stack:
            child = stack.pop()
            children.append(child)
            stack.extend(self.get_children(child))
        return children
