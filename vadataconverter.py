from os import path
from time import sleep
from threading import Thread
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

from converter import convert

file_list = []
isFirstFile = True

def open_file():
    global file_list
    global isFirstFile
    filetypes = (
        ('Excel 97-2003 Workbook', '*.xls'),
        ('All Files', '*')
    )

    filenames = fd.askopenfilenames(
        title = 'Select File(s)',
        initialdir=path.expanduser('~'),
        filetypes=filetypes
    )

    if isFirstFile == True:
        lbl_file_txt.set('')
        isFirstFile = False

    lbl_str = lbl_file_txt.get()
    for f in filenames:
        file_list.append(f)
        lbl_str += path.basename(f)
        lbl_str += '\n'
    lbl_file_txt.set(lbl_str)

def convert_files():
    global file_list
    global isFirstFile
    sheet_name = 'individual-cause-of-death'
    
    for f in file_list:
        old = lbl_file_txt.get()
        new = old + 'Converting ' + path.basename(f) + '\n'
        lbl_file_txt.set(new)


        bname = path.splitext(f)[0]
        ext = path.splitext(f)[1]
        outfile = bname + '_converted' + ext

        try:
            convert(f, sheet_name, outfile)
            
            old = lbl_file_txt.get()
            new = old + 'Done!\n'
            lbl_file_txt.set(new)
        except:
            old = lbl_file_txt.get()
            new = old + 'Error!\n'
            lbl_file_txt.set(old)

    lbl_status_txt.set("Done!")
    
    btn_convert['state'] = 'normal'
    btn_browse['state'] = 'normal'
    
    isFirstFile = True
    file_list = []

def do_convert():
    global file_list
    lbl_status_txt.set('Converting...')
    lbl_file_txt.set('')

    btn_convert['state'] = 'disabled'
    btn_browse['state'] = 'disabled'
    
    cthread = Thread(target = convert_files)
    cthread.start()

root = Tk()
root.geometry("600x400")
    
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

lbl_file_txt = StringVar()
lbl_file_txt.set("Selected files will be shown here")
lbl_files = Label(
    frm_mid,
    relief=RIDGE,
    font=font,
    textvariable=lbl_file_txt,
    justify=LEFT,
    anchor='nw',
    wraplength=500,
    height=13
)

lbl_files.pack(fill=X, expand=False)

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
