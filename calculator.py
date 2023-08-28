from tkinter import *
rt = Tk()
rt.title("Simple Calculator")
rt.geometry('486x486')
rt.resizable(0,0)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression=""

expression = ""

input_text= StringVar()
ipframe=Frame(rt,width=470,height=75,bg='blue',highlightthickness=1)
ipframe.pack(side=TOP)
ipfield=Entry(ipframe,font=('arial',27,'bold'),textvariable=input_text,width=75,bg="cyan",bd=5,justify=RIGHT)
ipfield.grid(row=0,column=0)
ipfield.pack()

btframe=Frame(rt,width=570,height=511,bg='red')
btframe.pack()
clear = Button(btframe,text="C",width=52,height=5,cursor='hand2',command = lambda: btn_clear())
clear.grid(row=0,column=0,columnspan=3)
divide= Button(btframe,text="/",width=16,height=5,cursor='hand2', command= lambda: btn_click("/"))
divide.grid(row=0,column=3)
seven=Button(btframe,text="7",width=16,height=5,cursor='hand2',command= lambda: btn_click("7"))
seven.grid(row=1,column=0)
eight=Button(btframe,text='8',width=16,height=5,cursor='hand2',command=lambda:btn_click("8"))
eight.grid(row=1,column=1)
nine=Button(btframe,text='9',width=16,height=5,cursor='hand2',command=lambda: btn_click("9"))
nine.grid(row=1,column=2)
multiply=Button(btframe,text='X',width=16,height=5,cursor='hand2',command=lambda:btn_click("*"))
multiply.grid(row=1,column=3)
four=Button(btframe,text='4',width=16,height=5,cursor='hand2',command=lambda:btn_click("4"))
four.grid(row=2,column=0)
five=Button(btframe,text='5',width=16,height=5,cursor='hand2',command=lambda: btn_click('5'))
five.grid(row=2,column=1)
six=Button(btframe,text='6',width=16,height=5,cursor='hand2',command=lambda:btn_click("6"))
six.grid(row=2,column=2)
minus=Button(btframe,text='-',width=16,height=5,cursor='hand2',command=lambda:btn_click("-"))
minus.grid(row=2,column=3)
one=Button(btframe,text='1',width=16,height=5,cursor='hand2',command=lambda:btn_click('1'))
one.grid(row=3,column=0)
two=Button(btframe,text='2',width=16,height=5,cursor='hand2',command=lambda:btn_click("2"))
two.grid(row=3,column=1)
three=Button(btframe,text='3',width=16,height=5,cursor='hand2',command=lambda:btn_click('3'))
three.grid(row=3,column=2)
plus=Button(btframe,text='+',width=16,height=5,cursor='hand2',command=lambda:btn_click("+"))
plus.grid(row=3,column=3)
decimal=Button(btframe,text='.',width=16,height=5,cursor='hand2',command=lambda:btn_click("."))
decimal.grid(row=4,column=2)
zero=Button(btframe,text='0',width=34,height=5,cursor='hand2',command=lambda: btn_click("0"))
zero.grid(row=4,column=0,columnspan=2)
equal=Button(btframe,text='=',width=16,height=5,cursor='hand2',command=lambda:btn_equal())
equal.grid(row=4,column=3)

rt.mainloop()
