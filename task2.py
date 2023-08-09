import tkinter  
from tkinter import *  
from tkinter import messagebox  
  
var = ""  
A = 0  
operator = ""  
  
# defining the function for Button 
def button_1Clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
  
def button_2Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
  
def button_3Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
   
def button_4Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  

def button_5Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
def button_6Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
def button_7Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
   
def button_8Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
def button_9Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  

def button_0Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
def button_AddClicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  
def button_SubClicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
 
def button_MulClicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
  
def button_DivClicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  

def button_EqualClicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  
 
def button_CClicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  

window = tkinter.Tk()  
# setting the size of the window  
window.geometry("320x500+400+400")  
# disabling the resize option for better UI  
window.resizable(0, 0)  
# setting the title of the Calculator window  
window.title("GUI Calculator")  
  
# creating the label for the window  
the_data = StringVar()  
guiLabel = Label(  
    window,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  
# using the pack() method  
guiLabel.pack(expand = True, fill = "both")  
  
# creating the frames for the buttons  

frameOne = Frame(window, bg = "#000000")  
frameOne.pack(expand = True, fill = "both") # frame can expand if it gets some space  
  
frameTwo = Frame(window, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  
 
frameThree = Frame(window, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  

frameFour = Frame(window, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
  
# creating buttons for each frame  
 
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_1Clicked  
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
  

buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2Clicked  
)  
  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  

buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3Clicked  
)  

buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  

buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_CClicked  
)  
  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4Clicked  
)  

buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5Clicked  
)  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  

buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6Clicked  
)  
  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  

buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_AddClicked  
)  

buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  

buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7Clicked  
)  
 
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  

buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8Clicked  
)  

buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9Clicked  
)  
 
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_SubClicked  
)  
 
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
 
 
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_0Clicked  
)  
 
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_MulClicked  
)  

buttonMUL.pack(side = LEFT, expand = True, fill = "both")  

buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_DivClicked  
)  

buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  
 
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
  
  
window.mainloop()  