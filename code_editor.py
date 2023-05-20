from tkinter import *


class CodeEditor:
    def __init__(self, parent):
        self.parent = parent
        
        # Create the UI elements
        self.scrollbar = Scrollbar(self.parent)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text = Text(self.parent, wrap=WORD, yscrollcommand=self.scrollbar.set, bg='#282828', fg='hotpink', insertbackground='white')
        self.text.pack( fill=BOTH, expand=True)

        # Bind keyboard shortcuts
        self.text.bind("<Control-c>", self.copy_text)
        self.text.bind("<Control-a>", self.select_text)
        self.text.bind("<Control-x>", self.cut_text)

        self.scrollbar.config(command=self.text.yview)
    
    def load_text(self, filepath):
        # load file
        with open(filepath, 'r') as f:
            self.text.insert('1.0', f.read())

    def copy_text(self, event=None):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def select_text(self, event=None):
        self.text.tag_add("sel", "1.0", "end")
        return "break"

    def cut_text(self, event=None):
        self.copy_text()
        self.text.delete("sel.first", "sel.last")
