#region Modules
from tkinter import *
from code_editor import *
from pylint_interaction import *
from Box import *
#endregion

#region UDF
def is_exists(var):
    return var in locals() or var in globals()

def get_per_of_num(num, per, returnInt=True):
    if returnInt:
        return int((per/100) * num)
    else:
        return (per/100) * num

def onclick_btn_submit(text):
    # Get the text
    code = text.get("1.0", END)
    # Save file
    with open(filepath, 'w') as f:
        f.write(code)
    # pass file to the pylint_interaction for getting score
    score_lbl['text'] = f'Current Score : {get_score(filepath)}'

    # update WarningPrefab
    update_wp()

    global cp
    global ep

    if get_score(filepath) == 10.0:
        CustomBox(inner_frame, CustomBox.COMPLETED)

    elif get_score(filepath) is None:
        CustomBox(inner_frame, CustomBox.ERROR)


def update_wp():
    # Clear the existing warning boxes
    for box in wp:
        box.delete_box()
    wp.clear()

    # Add new warning boxes based on the updated warnings
    for warning in get_output_warnings(filepath):
        wp.append(CustomBox(inner_frame, CustomBox.WARNING, warning))


            
#endregion

#region Variables
filepath = 'temp_code_file.py'
global wp
wp = []
cp = None
ep = None
#endregion

#region Main
root = Tk()
root.title('PW Editor')#='PW Editor'
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# Header
header = Frame(root, bg="black", height=50, width=width)
header.pack()

def_label = Label(header, text="A platform to measure Python code optimization and readability.", fg="gold", bg='black', font=("Monospace", 18), width=get_per_of_num(width, 7.54))
def_label.pack(padx=10, pady=10)

# Footer
footer = Frame(root, bg="lightblue", height=70, width=100)
footer.pack(fill=X, side=BOTTOM)
footer.pack_propagate(0)


#  Left part for editor
left_frame = Frame(root, bg = '#282828')
left_frame.pack(side=LEFT, fill=BOTH, expand=True)
ce = CodeEditor(left_frame)
ce.load_text(filepath)

# Right part for buttons and warnings
right_frame = Frame(root, bg='#282828')
right_frame.pack(side='left', expand=True, fill='both')

# Create a container frame for the warnings prefabs
warnings_frame = Frame(right_frame, bg='grey')
warnings_frame.pack(side='top', fill='both', expand=True)

# Add a scrollbar to the warnings frame
scrollbar = Scrollbar(warnings_frame)
scrollbar.pack(side='right', fill='y')

# Create a canvas to hold the warnings prefabs
canvas = Canvas(warnings_frame, bg='grey', yscrollcommand=scrollbar.set)
canvas.pack(side='left', fill='both', expand=True)

# Configure the scrollbar to scroll the canvas
scrollbar.config(command=canvas.yview)

# Create a frame to hold the warnings prefabs inside the canvas
inner_frame = Frame(canvas, bg='grey')
inner_frame.pack(side=TOP, fill=BOTH, expand=True)

# Set the size of the canvas and configure it to hold the inner frame
canvas.create_window((0, 0), window=inner_frame, anchor='nw', tags='inner_frame')
canvas.config(scrollregion=canvas.bbox('all'))

# Update the warnings prefabs to the inner frame
update_wp()

# Configure the canvas to resize with the window
def resize_canvas(event):
    canvas.config(scrollregion=canvas.bbox('all'))
canvas.bind('<Configure>', resize_canvas)

# score label
score_lbl = Label(footer, text="...", font=('Arial', 22), bg='#282828', fg='lightgreen', width=50)
score_lbl.pack(side=LEFT, fill=BOTH, padx=4, pady=4)


# Add the submit button to the bottom of the right frame
submit_btn = Button(footer, text='SUBMIT', font=('Arial', 18), command=lambda: onclick_btn_submit(ce.text))
submit_btn.pack(pady=(4, 4), padx=(0, 4), fill=BOTH, side=RIGHT, expand=True)
submit_btn['fg'] = 'gold'
submit_btn['bg'] = '#282828'

root.mainloop()
#endregion
