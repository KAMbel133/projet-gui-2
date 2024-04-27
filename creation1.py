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

#creation de la fonction nouveau fichier
def newFile():
    textArea.delete(1.0, END)

#creation de la fonction ouvri un fichier

def openFile():
    #creation de la variable qui vas contenir le type de document a ouvrir 
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
       
        textArea.delete(1.0, END) # supprime le contenu de la page ouverte 
        f = open(file)
        textArea.insert(1.0, f.read()) # ouvre le nouveau contenu souhaiter

#creation de la fonction sauvgardé
def save():
    #tenter d'nregistre le cotenu
    try:
        file_content = textArea.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", ".txt"), ("Text files", "*.txt")])
        if not file_path:
            return
        with open(file_path, 'w') as file: 
            file.write(file_content)
            messagebox.showinfo("succes", "Le fichier a ete sauvegardé avec succés.")
    except Exception as e:
            messagebox.showerror("Erreur", str(e)) #lors que le fichier n'arrive pas etre sauvegardé affiche le message d'erreur
# creation de la fonction pour quitter la page 
def quitFile():
    root.destroy()
#creation de la fonction couper le texte
def cut():
    textArea.event_generate(("<<Cut>>"))

#creation de la fonction copier le texte
def copy():
    textArea.event_generate(("<<Copy>>"))

#creation de la fonction coller
def paste():
    textArea.event_generate(("<<Paste>>"))

 # fonction info du bloc note   
def info():
    messagebox.showinfo("About Bloc note", '''Bloc note
    
Version - 1.1.1
Developper - kenne idriss, christopher, Loic
    de la premiere année en informatique a L'Ecole IT''')

# changer la taille du texte 
def changeSizeWindow():
    def changeSize():
        global font_size 
        font_size = size.get()
        NotePad_font.configure(size=font_size)
        TextSize.destroy()
    
    TextSize = Toplevel()
    TextSize.geometry("400x100")
    TextSize.title("tAILLE DE TEXTE")

    size = StringVar()
    size.set(NotePad_font.cget('size'))
    
    Label(TextSize, text="Enter la taille de texte que vous voulez:", font="lucida 15 bold").pack()
    Entry(TextSize, textvariable=size, font="lucida 15").pack()
    Button(TextSize, text="Appliqué", command=changeSize).pack()
    

#creation de la zone de texte
    textArea = Text(root, font=NotePad_font, yscrollcommand=ScrollBar.set)
    file = None
    textArea.pack(expand=True,fill="both")

    ScrollBar.config(command=textArea.yview) # creation de la scrollbar

    
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