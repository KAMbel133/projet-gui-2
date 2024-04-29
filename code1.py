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
        self.current =math.exp
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


