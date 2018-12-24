from tkinter import *

result = ''

def click(num):
    global result
    result += str(num)
    calculate.set(result)

def equalClick():

    try:
        global result
        final = str(eval(result))
        calculate.set(final)
        result = ''
    except:
        calculate.set('Error!!!')
        result=''

def reset():
    global result
    calculate.set('')
    result=''


Calc = Tk()
Calc.title('Calculator -- Concept By Dorgival Filho')

calculate = StringVar()
Input = Entry(Calc, textvariable=calculate, bg='black')
Input.grid(columnspan=6, ipadx=65)

calculate.set('Expression: ')

but1 = Button(Calc, text='1', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(1))
but1.grid(row=1, column=0)

but2 = Button(Calc, text='2', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(2))
but2.grid(row=1, column=1)

but3 = Button(Calc, text='3', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(3))
but3.grid(row=1, column=2)

but4 = Button(Calc, text='4', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(4))
but4.grid(row=2, column=0)

but5 = Button(Calc, text='5', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(5))
but5.grid(row=2, column=1)

but6 = Button(Calc, text='6', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(6))
but6.grid(row=2, column=2)

but7 = Button(Calc, text='7', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(7))
but7.grid(row=3, column=0)

but8 = Button(Calc, text='8', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(8))
but8.grid(row=3, column=1)

but9 = Button(Calc, text='9', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(9))
but9.grid(row=3, column=2)

but0 = Button(Calc, text='0', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(0))
but0.grid(row=4, column=0)

plus = Button(Calc, text='+', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('+'))
plus.grid(row=1, column=3)

minus = Button(Calc, text='-', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('-'))
minus.grid(row=2, column=3)

multi = Button(Calc, text='*', fg='black',bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('*'))
multi.grid(row=3, column=3)

div = Button(Calc, text='/', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('/'))
div.grid(row=4, column=3)

equal = Button(Calc, text='=', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=equalClick)
equal.grid(row=4, column=1)

square = Button(Calc, text='**', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('**'))
square.grid(row=4, column=2)

lParent = Button(Calc, text='(', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('('))
lParent.grid(row=1, column=4)

rParent = Button(Calc, text=')', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click(')'))
rParent.grid(row=2, column=4)

dot = Button(Calc, text='.', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=lambda:click('.'))
dot.grid(row=3, column=4)

reset = Button(Calc, text='C', fg='black', bg='white', font=('Kalimati', '10'), height=1, width=5, command=reset)
reset.grid(row=4, column=4)

InfoText = StringVar()
InfoText.set('If you want to calculate a\nsquare root,raise any number\nto (1/2) using the\npower button ("**")\nExample: 4**(1/2)\n27**(1/3).') 
Text = Label(Calc, textvariable=InfoText, font=('Kalimati', '10'))
Text.grid(columnspan=18, ipadx=10)

Calc.mainloop()