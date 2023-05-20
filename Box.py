from tkinter import *

class CustomBox:
    WARNING = 'warning'
    ERROR = 'error'
    COMPLETED = 'completed'

    prev_boxes = {}
    current_type = None
    current_box = None

    def __init__(self, parent, box_type, text={}):
        self.parent = parent
        self.box_type = box_type
        self.text = text
        self.bg_color = self.get_bg_color()
        self.label_color = self.get_label_color()

        if self.box_type not in CustomBox.prev_boxes:
            CustomBox.prev_boxes[self.box_type] = []
        
        if self.box_type == CustomBox.current_type:
            self.create_box()
        else:
            self.delete_boxes()
            self.create_box()

        CustomBox.prev_boxes[self.box_type].append(self.frm)
        CustomBox.current_type = self.box_type

    def create_box(self):
        # create frame
        self.frm = Frame(self.parent, bg=self.bg_color, width=512)
        self.frm.pack(expand=True, fill=BOTH, padx=10, pady=10)

        # create label
        if self.box_type == self.WARNING:
            label = Label(self.frm, text= f'msg: {self.text["wmsg"]}\nline: {self.text["ln"]}\tcolumn: {self.text["cn"]}\twarn code: {self.text["wcode"]}', fg=self.label_color, bg=self.bg_color, width=62, wraplength=500)
            label.bind("<Button-1>", lambda event, wcode=self.text["wcode"]: self.copy_wcode(wcode))
        
        elif self.box_type == self.COMPLETED:
            label = Label(self.frm, text='Congratulations, You have solved all the warnings.', fg=self.label_color, bg=self.bg_color, width=62, wraplength=500)

        elif self.box_type == self.ERROR:
            label = Label(self.frm, text='Your code has some errors.', fg=self.label_color, bg=self.bg_color, width=62, wraplength=500)
        
        label.pack()

    def delete_boxes(self):
        if CustomBox.current_type is not None:
            for box in CustomBox.prev_boxes[CustomBox.current_type]:
                box.destroy()
            CustomBox.prev_boxes[CustomBox.current_type] = []
    
    def delete_box(self):
        if self.frm is not None:
            self.frm.destroy()
            self.frm = None
    
    def copy_wcode(self, wcode):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(wcode)

    def get_bg_color(self):
        if self.box_type == self.ERROR:
            return 'red'
        elif self.box_type == self.WARNING:
            return 'orange'
        elif self.box_type == self.COMPLETED:
            return 'green'
        else:
            return 'white'

    def get_label_color(self):
        if self.box_type == self.ERROR:
            return 'white'
        else:
            return 'black'
