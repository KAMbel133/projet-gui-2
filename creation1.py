#creation de fenetre tkinter
#import des module
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
import os
#creation de fenetre tkinter
if __name__ == "__main__":
    #creation de fenetre tkinter
    root = Tk()
    root.title("Bloc note ")
    root.geometry("600x400")
    NotePad_font = Font(root,family='lucida',size=13)
    
    
    ScrollBar = Scrollbar(root)
    
    ScrollBar.pack(fill=Y, side=RIGHT)

    

    
    textArea = Text(root, font=NotePad_font, yscrollcommand=ScrollBar.set)
    file = None
    textArea.pack(expand=True,fill="both")

    ScrollBar.config(command=textArea.yview)

    
#creation des menu et sous menu
   

    

    

    root.mainloop() 