from time import sleep

from tkinter import (
    Tk,
    RIGHT,
    LEFT,
    BOTTOM,
    BOTH,
    X,
    Y,
    E,
    W,
    SUNKEN,
    GROOVE,
    RIDGE,
    Frame,
    Label,
    Button,
    Entry,
    StringVar,
)    

from tkinter import filedialog as fd


def open_file():
    filetypes = (
        ('Text Files', '*.txt'),
        ('All Files', '*')
    )

    filenames = fd.askopenfilenames(
        title = 'Select File(s)',
        initialdir='C:\\',
        filetypes=filetypes
    )

    lbl_str = ''
    for f in filenames:
        lbl_str += f
        lbl_str += '\n'
    print(lbl_str)
    lbl_file_text.set(lbl_str)

def do_convert():
    print(lbl_file_text.get().split(sep='\n'))
    lbl_status_txt.set("Converting...")
    lbl_status_txt.set("Done!")

root = Tk()
root.geometry("600x400+300+300")
root.attributes('-type', 'dialog')
    
root.title("VADataConverter")

frame_border_width=5

font = ('Arial', 14, 'bold')

frm_top = Frame(root, borderwidth=frame_border_width)
frm_top.pack(fill=X)

file_edit = Entry(frm_top, font=font)
btn_browse = Button(frm_top, text="Add", font=font, command=open_file)

file_edit.pack(side=LEFT, fill=X, expand=True)
btn_browse.pack(side=RIGHT, padx=2)

frm_mid = Frame(root, borderwidth=frame_border_width)
frm_mid.pack(fill=BOTH, expand=True)

lbl_file_text = StringVar()
lbl_file_text.set("Selected files will be shown here")
lbl_files = Label(
    frm_mid,
    relief=RIDGE,
    font=font,
    textvariable=lbl_file_text,
    justify=LEFT,
    anchor='nw',
)

lbl_files.pack(fill=BOTH, expand=True)

frm_bot = Frame(root, borderwidth=frame_border_width)
frm_bot.pack(fill=X)

lbl_status_txt = StringVar()
lbl_status_txt.set("Add file(s) and press convert...")
lbl_status = Label(frm_bot, textvariable=lbl_status_txt, relief=SUNKEN, font=font, anchor='w')
btn_quit = Button(frm_bot, text = "Quit", font=font, command=root.destroy)
btn_convert = Button(frm_bot, text = "Convert", font=font, command=do_convert)

lbl_status.pack(side=LEFT, expand=True, fill=X)
btn_convert.pack(side=RIGHT)
btn_quit.pack(side=RIGHT, padx=2)

root.mainloop()
