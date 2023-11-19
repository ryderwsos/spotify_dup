from tkinter import *
import tkinter as tk
from filter import find_dups

root = tk.Tk()

root.title("Spotify Playlist Dup Checker")
top = Tk()  
sb = Scrollbar(top)  
sb.pack(side = RIGHT, fill = Y)  
    
dups = []

def submit():
    id = playlist_id_var.get()
    dups = find_dups(id)
    mylist = Listbox(top, yscrollcommand = sb.set )  
    for x in dups:
        mylist.insert(END, x)
    
    mylist.pack( side = LEFT )  
    sb.config( command = mylist.yview )  

playlist_id_var = tk.StringVar()
playlist_id_label = tk.Label(root, text = "Playlist ID", font=('calibre', 12, 'bold'))
playlist_id_entry = tk.Entry(root, textvariable=playlist_id_var, font=('calibre', 12, 'normal'))
playlist_id_label.grid(row=0,column=0)
playlist_id_entry.grid(row=0,column=1)

sub_button = tk.Button(root, text = "Submit", command = submit)
sub_button.grid(row=1, column=0)

root.mainloop()