#creation de fenetre tkinter
#import des module
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
import os
#creation du bloc note
if __name__ == "__main__":
    #creation de fenetre tkinter
    root = Tk()
    root.title("Bloc note ")
    root.geometry("600x400")
    NotePad_font = Font(root,family='lucida',size=13)
    
    
    ScrollBar = Scrollbar(root)
    
    ScrollBar.pack(fill=Y, side=RIGHT)

    

#creation de la zone de texte
    textArea = Text(root, font=NotePad_font, yscrollcommand=ScrollBar.set)
    file = None
    textArea.pack(expand=True,fill="both")

    ScrollBar.config(command=textArea.yview)

    
#creation des menu et sous menu
    
    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="nouveau fichier", command=newFile)
    FileMenu.add_command(label="ouvrir un fichier", command=openFile)
    FileMenu.add_command(label="Sauvegardé", command=save)
    FileMenu.add_separator()
    FileMenu.add_command(label="Quitte", command=quitFile)
    MenuBar.add_cascade(label="Fchier", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    EditMenu.add_command(label="Font Size", command=changeSize)
    EditMenu.add_command(label="Font Style", command=changeStyle)
    
    
    MenuBar.add_cascade(label="Edition", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="about", command=info)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)



    root.config(menu=MenuBar)

    

    

    

    root.mainloop() 