#! /usr/bin/python3

import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
a=Tk()

a.geometry("350x250")
a.title("Shortcut Maker")

sname=tk.StringVar()
scomment=tk.StringVar()
scommand=tk.StringVar()

def selecticon():
  global iconfile
  iconfile = askopenfilename(filetypes = [('Icons', '*.png')])
  icon_btn.config(text = iconfile)

def make():
  w = sname.get()
  x = scomment.get()
  y = scommand.get()
  z = iconfile
  home = os.environ['HOME']
  fpath = os.path.join(home, ".local/share/applications")
  sfilename = "%s.desktop" % w
  with open(f"{fpath}/{sfilename}", 'w') as ffile:
       ffile.write("[Desktop Entry]\n")
       ffile.write("Type=Application\n")
       ffile.write("Encoding=UTF-8\n")
       ffile.write("Name=")
       ffile.write(w + '\n')
       ffile.write("Comment=")
       ffile.write(x + '\n')
       ffile.write("Exec=")
       ffile.write(y + '\n')
       ffile.write("Icon=")
       ffile.write(z + '\n') 
  os.chmod(f"{fpath}/{sfilename}",0o0775)
  make_btn.config(text = "Done!")

def exit():
  a.destroy()

label1 = tk.Label(a, text = "Shortcut name:").place(x=20,y=20)
label2 = tk.Label(a, text = "Comment:").place(x=20,y=50)
label3 = tk.Label(a, text = "Command:").place(x=20,y=80)
label4 = tk.Label(a, text = "Icon:").place(x=20,y=110)

sname_entry = tk.Entry(a, textvariable = sname).place(x=165,y=20)
comment_entry = tk.Entry(a, textvariable = scomment).place(x=165,y=50)
command_entry = tk.Entry(a, textvariable = scommand).place(x=165,y=80)
icon_btn = tk.Button(a, text = "Select an icon", command = selecticon, width = 17)
icon_btn.place(x=165,y=110)
make_btn = tk.Button(a, text = "Make shortcut", command = make)
make_btn.place(x=100,y=170)
exit_btn = tk.Button(a, text = "Exit", command = exit).place(x=13,y=210)

a.mainloop()