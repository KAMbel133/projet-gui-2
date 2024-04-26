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
#-----------------------------------------party logique-----------------------------------------------------------
class Calculator:
    def _init_(self):
        self.total=0
        self.current= ''
        self.input_value =True
        self.check_sum=False
        self.oper= ''
        self.result =False
        
    def numberEnter(self,num):
        self.result=False
        firstnum= txtDisplay.get()
        secondnum= str(num)
        if self. input_value:
           self.current=secondnum
           self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.display(self.current)

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
added_value =Calculator()        


