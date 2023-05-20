from tkinter import *
from tkinter import scrolledtext
from tkinter.font import Font
import os
import socket

def install():
    try:
        socket.create_connection(("www.google.com", 80))
    except OSError:
        console.delete('1.0', END)
        console.insert(INSERT, 'No Internet Connection\nPlease check your internet connection and try again.')
        return

    # install all the dependencies
    console.delete('1.0', END)
    console.insert(INSERT, 'Installing all the dependencies ....\n\n')
    console.insert(INSERT, 'Installing Pylint ......\n')
    output_stream = os.popen('pip install pylint')
    console.insert(INSERT, output_stream.read())

    console.insert(INSERT, '\n----------------------------------------------------------------------------------------------------------\n')

    console.insert(INSERT, 'Installing Tkinter ......\n')
    output_stream = os.popen('pip install tk')
    console.insert(INSERT, output_stream.read())
    console.insert(INSERT, '\nINSTALLATION COMPLETED')


root = Tk()
root.title("PW Editor - Dependencies Installer")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.config(bg='#282828')

my_font = Font(family="Georgia", size=36, weight="bold")
title_label = Label(text="PW Editor - Dependencies Installer", font=my_font, fg='#FFFFFF', bg=root.cget("bg"))
title_label.pack()

install_btn = Button(text="Install", font=("Arial", 24), bg='#008080', fg='#FFFFFF', command=install, padx=20, pady=10)
install_btn.pack(pady=20)

console = scrolledtext.ScrolledText(
    width=100,
    height=10,
    wrap=WORD,
    bg='#101010',
    fg='white',
    font=('Arial', 18)
)
console.pack(padx=200, pady=28, expand=True, fill=BOTH)
console.bind("<Key>", lambda e: "break")

# run the main loop of the window
root.mainloop()
