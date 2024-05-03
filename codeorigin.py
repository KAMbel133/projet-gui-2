from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox
import os




def newFile():
    
    text.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
       
        text.delete(1.0, END)
        f = open(file)
        text.insert(1.0, f.read())
        
def save():
    #tenter d'nregistre le cotenu
    try:
        file_content = text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", ".txt"), ("Text files", "*.txt")])
        if not file_path:
            return
        with open(file_path, 'w') as file: 
            file.write(file_content)
            messagebox.showinfo("succes", "Le fichier a ete sauvegardé avec succés.")
    except Exception as e:
            messagebox.showerror("Erreur", str(e))
def quitFile():
    root.destroy()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))

    
def info():
    messagebox.showinfo("About Bloc note", '''Bloc note
    
Version - 1.1.1
Developper: kenne idriss
            christopher Ferry 
            Loic K
    de la premiere année en informatique a L'Ecole IT''')


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
    

def changeSize():
    changeSizeWindow()

def gras():
    gras_font = text.tag_ranges("sel")
   
    text.tag_config("bold", font=("Arial", 15, "bold" ))
    tag_actu = text.tag_names("sel.first")
    text.tag_add("bold", "sel.first", "sel.last")


def mettre_en_italique():
    # Obtient les indices du texte sélectionné
    debut, fin = text.tag_ranges("sel")
    # Applique la balise "italique" au texte sélectionné
    text.tag_add("italique", debut, fin)
    # Crée une balise "italique" qui met le texte en italique
    text.tag_configure("italique", font=("Arial", 15, "italic"))






def calulatrice():
    
    import math
    import tkinter.messagebox


    root =Tk()
    root.title("calculatrice scientifique")
    root.configure(background="powder blue")
    root.resizable(width=False, height=False)
    root.geometry("220x298+0+0")

    calculator = Frame(root)
    calculator.grid()
    #--------------entrer les informations -----------------
    txtDisplay =Entry(calculator, font=('arial',14,'bold'), bg="blue", bd=25,width=15,justify=RIGHT)
    txtDisplay.grid(row=0,column=0,columnspan=4,pady=1,padx=1)
    txtDisplay.insert(0,"0")
    #-----------------------------------------party logique-----------------------------------------------------------

    class Calculator :
        def __init__(self):
            self.total= 0
            self.current = ''
            self.input_value = True
            self.check_sum = False
            self.oper=''
            self.result =False

        def numberEnter(self , num) :
            self.result =False
            firstnum=txtDisplay.get()
            secondnum = str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value=False
            else:
                if secondnum =='.':
                    if secondnum in firstnum:
                        return
                self.current=firstnum+ secondnum
            self.display(self.current)


        def sum_of_total(self):
            self.result=True
            self.current= float(self.current)
            if self.check_sum == True:
                self.valid_function()

            else:
                self.total=float(txtDisplay.get())


        def valid_function(self):
            if self.oper =='add':
                self.total += self.current 
            if self.oper =='sub':
                self.total -=self.current 
            if self.oper =='mul':
                self.total *=self.current 
            if self.oper =='div':
                self.total /=self.current   
            if self.oper =='mod':
                self.total %=self.current  

            self.input_value = True
            self.check_sum = False
            self.display(self.total)

        def operator(self ,oper):
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
                self.input_value = True
            self.check_sum = True
            self.oper = oper
            self.result = False 

        def clear(self):
            self.result = False
            if len(self.current)>0:
                if len(self.current) ==1:
                    self.display(0)
                    self.input_value = True
                else:
                    self.current= self.current[0: len(self.current)-1] 
                    self.display(self.current)
            else:
                self.display(0)
                self.input_value =True

        def clearAll(self):
            self.display(0)
            self.input_value = True 
                

        def PM(self):
            self.result =False
            self.current =-(float(txtDisplay.get()))
            self.display(self.current)


        def pi(self):
            self.result=False
            self.current =math.pi
            self.display(self.current)

    
        def twopi(self):
            self.result=False
            self.current =math.tau
            self.display(self.current) 

        def e(self):
            self.result=False
            self.current =math.e
            self.display(self.current) 

        def EXP(self):
            self.result=False
            self.current =math.exp(float(txtDisplay.get()))
            self.display(self.current) 


        def sin(self):
            self.result=False
            self.current =math.sin(float(txtDisplay.get()))
            self.display(self.current) 


        def cos(self):
            self.result=False
            self.current =math.cos(float(txtDisplay.get()))
            self.display(self.current) 


        def tan(self):
            self.result=False
            self.current =math.tan(float(txtDisplay.get()))
            self.display(self.current) 


        def log(self):
            self.result=False  
            a =float(txtDisplay.get())
            if a < 0 :
                self.display("can't log negatif number")
            elif a ==0:
                self.display("can't log zero")
                
            else:
                self.current =math.log(float(txtDisplay.get()))
                self.display(self.current) 

        def sinh(self):
            self.result=False
            self.current =math.sinh(float(txtDisplay.get()))
            self.display(self.current) 


        def cosh(self):
            self.result=False
            self.current =math.cosh(float(math.radians(txtDisplay.get())))
            self.display(self.current) 


        def tanh(self):
            self.result=False
            self.current =math.tanh(float(txtDisplay.get()))
            self.display(self.current) 

        def Mod(self):
            self.result=False
            self.current =math.modf(float(txtDisplay.get()))
            self.display(self.current) 

        def log2(self):
            self.result=False
            self.current =math.log2(float(txtDisplay.get()))
            self.display(self.current) 


        def Deg(self):
            self.result=False
            self.current =math.degrees(float(txtDisplay.get()))
            self.display(self.current) 


        def acosh(self):
            self.result=False
            self.current =math.acosh(float(txtDisplay.get()))
            self.display(self.current) 


        def asinh(self):
            self.result=False
            self.current =math.asinh(float(txtDisplay.get()))
            self.display(self.current) 


        def log10(self):
            self.result=False
            self.current =math.log10(float(txtDisplay.get()))
            self.display(self.current) 

        def expm1(self):
            self.result=False
            self.current =math.expm1(float(txtDisplay.get()))
            self.display(self.current) 


        def gamma(self):
            self.result=False
            self.current =math.gamma(float(txtDisplay.get()))
            self.display(self.current) 


        def log1p(self):
            self.result=False
            self.current =math.log1p(float(txtDisplay.get()))
            self.display(self.current)   


        def sqrt(self):
            self.result=False
            self.current =math.sqrt(float(txtDisplay.get()))
            self.display(self.current)       
            
            
        def display(self, value):
            txtDisplay.delete(0,END)
            txtDisplay.insert(0,value)

    added_value = Calculator()

    #-------------------boutons -------------------------------------------------------------------------------
    numberstd="789456123"
    btn=[]
    i=0
    for j in range(2,5):
        for k in range(3):
            button = Button(calculator,width=3,height=1, font=('arial',15,'bold'),bd=2,text=numberstd[i])
            btn.append(button)
        #    button.bind("<Button-1>", onclik)
            btn[i].grid(row=j,column=k,pady=1)
            btn[i] [COMMAND]= lambda i = numberstd[i]:added_value.numberEnter(i)
            i+=1

    #-----------------------------------standard-----------------------------------------------------
    btnclear = Button(calculator,text=chr(67),width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command=added_value.clear).grid(row=1,column=0,pady=1,)
    btnallclear= Button(calculator,text=chr(67)+chr(69),width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command = added_value.clearAll).grid(row=1,column=1,pady=1)
    btnsq= Button(calculator,text=chr(8730),width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command=added_value.sqrt).grid(row=1,column=2,pady=1)
    btnadd = Button(calculator,text="+",width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command = lambda : added_value.operator("add")).grid(row=1,column=3,pady=1)
    btnsub = Button(calculator,text="-",width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command = lambda : added_value.operator("sub")).grid(row=2,column=3,pady=1)
    btnMul = Button(calculator,text="*",width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command = lambda : added_value.operator("mul")).grid(row=3,column=3,pady=1)
    btndiv = Button(calculator,text=chr(247),width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command = lambda : added_value.operator("div")).grid(row=4,column=3,pady=1)


    btnZerro = Button(calculator,text="0",width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command=lambda :added_value.numberEnter("0")).grid(row=5,column=0,pady=1,)
    btnpoint= Button(calculator,text=".",width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command=lambda :added_value.numberEnter(".")).grid(row=5,column=1,pady=1)
    btnPM= Button(calculator,text=chr(177),width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.PM).grid(row=5,column=2,pady=1)
    btnEgual = Button(calculator,text="=",width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command = added_value.sum_of_total).grid(row=5,column=3,pady=1)
    #-------------------------------scientifique------------------------------------------------------------------
    btnpi =Button(calculator,text="π", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command=added_value.pi).grid(row=1,column=4,pady=1)
    btncos =Button(calculator,text="cos", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.cos).grid(row=1,column=5,pady=1)
    btnTan=Button(calculator,text="tan", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.tan).grid(row=1,column=6,pady=1)
    btnSin=Button(calculator,text="sin", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.sin).grid(row=1,column=7,pady=1)
    #----------------------------------ligne 2--------------------------------
    btn2pi =Button(calculator,text="2π", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command=added_value.twopi).grid(row=2,column=4,pady=1)
    btncoh =Button(calculator,text="cosh", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.cosh).grid(row=2,column=5,pady=1)
    btnTanh=Button(calculator,text="tanh", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.tanh).grid(row=2,column=6,pady=1)
    btnSinh=Button(calculator,text="sinh", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.sinh).grid(row=2,column=7,pady=1)
    #----------------------------------ligne3-------------------------------------------------------
    btnlog =Button(calculator,text="log", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.log).grid(row=3,column=4,pady=1)
    btnEXP =Button(calculator,text="exp", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.EXP).grid(row=3,column=5,pady=1)
    btnMod =Button(calculator,text="%", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.Mod).grid(row=3,column=6,pady=1)
    btnE   =Button(calculator,text="e", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.e).grid(row=3,column=7,pady=1)
    #----------------------------------ligne4------------------------------------------------------------------
    btnlog2 =Button(calculator,text="log2", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.log2).grid(row=4,column=4,pady=1)
    btnDeg =Button(calculator,text="Deg", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.Deg).grid(row=4,column=5,pady=1)
    btnacosh=Button(calculator,text="arch", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.acosh).grid(row=4,column=6,pady=1)
    btnasinh=Button(calculator,text="arsh", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.asinh).grid(row=4,column=7,pady=1)
    #---------------------------------ligne 5 ----------------------------------------------------------
    btnlog10 =Button(calculator,text="log10", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.log10).grid(row=5,column=4,pady=1)
    btnlog1p =Button(calculator,text="log1p", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.log1p).grid(row=5,column=5,pady=1)
    btnExpm1=Button(calculator,text="expm1", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.expm1).grid(row=5,column=6,pady=1)
    btngamma=Button(calculator,text="gamma", width=3,height=1,font=('arial',15,'bold'),bd=2,bg="#DCEE03",command= added_value.gamma).grid(row=5,column=7,pady=1)

    TextDisplay =Label(calculator,text="Scientific calculator ",font=('arial',15,'bold'),justify=CENTER)
    TextDisplay.grid(row=0,column=4,columnspan=4)

    # TextDisplay
    #---------------menu-----------

    def quitter():
        quitter = tkinter.messagebox.askyesno("calculatrice scientifique","voulez-vous vraiment Quitter?")
        if quitter > 0 :
            root.destroy()
            return


    def scientifique():
        root.resizable(width=False, height=False)
        root.geometry("430x300+0+0")
    def standard ():
        root.resizable(width=False, height=False)
        root.geometry("220x298+0+0")   

    menubar = Menu(calculator)
    filemenu = Menu(menubar,tearoff=0)

    menubar.add_cascade(label="fichier", menu=filemenu)
    filemenu.add_command(label="standard",command=standard)
    filemenu.add_command(label="scientifique",command=scientifique)
    filemenu.add_separator()
    filemenu.add_command(label="quitter",command=quitter)

    editmenu =Menu(menubar, tearoff=0)
    menubar.add_cascade(label="editer", menu=editmenu)
    editmenu.add_command(label="couper")
    editmenu.add_command(label="copier")
    editmenu.add_separator()
    editmenu.add_command(label="coller")
    helpmenu =Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Aide", menu=helpmenu)
    helpmenu.add_command(label="obtenir l'aide")
    root.config(menu=menubar)
    root.mainloop() 

    

if __name__ == "__main__":
    
    root = Tk()
    root.title("Bloc note ")
    root.geometry("600x400")
    NotePad_font = Font(root,family='lucida',size=13)

    
    
    
    ScrollBar = Scrollbar(root)
    
    ScrollBar.pack(fill=Y, side=RIGHT)

    

    
    text = Text(root, font=NotePad_font, yscrollcommand=ScrollBar.set)
    file = None
    text.pack(expand=True,fill="both")

    ScrollBar.config(command=text.yview)
    

    

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
    EditMenu.add_command(label="Size", command=changeSize)
   
    
    
    MenuBar.add_cascade(label="Edition", menu=EditMenu)


    formenu= Menu(MenuBar, tearoff=0)
    formenu.add_cascade(label= "Gras", command=gras)
    formenu.add_cascade(label="italic", command=mettre_en_italique)
    MenuBar.add_cascade(label="Style", menu=formenu)

    calomenu= Menu(MenuBar, tearoff=0)
    calomenu.add_cascade(label= "Calculatrice", command=calulatrice)
    MenuBar.add_cascade(label="Operation", menu=calomenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="about", command=info)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    

    root.config(menu=MenuBar)

    

    

    root.mainloop() 