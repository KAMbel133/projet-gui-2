from tkinter import *
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