#library to import for interface design
import tkinter as hm

#codes required for interface design
cal = hm.Tk()
cal.title('CALCULATOR')
cal.geometry("275x300+500+150")
cal.resizable(0,0)
cal.configure(background="BEIGE")


#functions to perform the necessary operations
def addition():
    if num1.get() and num2.get():
        data1=int(data1.get())
        data2=int(data2.get())
        result.configure(text=str(data1+data2))
def subtraction():
    if num1.get() and num2.get():
        data1=int(data1.get())
        data2=int(data2.get())
        result.configure(text=str(data1-data2))
def multiplication():
    if num1.get() and num2.get():
        data1=int(data1.get())
        data2=int(data2.get())
        result.configure(text=str(data1*data2))
def division():
    if num1.get() and num2.get():
        data1=int(data1.get())
        data2=int(data2.get())
        result.configure(text=str(data1/data2))


#placement of information inputs on the interface
result =hm.Label(cal, text="|----------|", width=30,bg="BEIGE")
result.place(x=80, y=60)
num1 = hm.Label(text="|>>").place(x=10,y=40)
num1 = hm.Entry(cal,  width=40)
num1.place(x=40, y=40,width=100,height=30)
num2 = hm.Label(text="|>>").place(x=10,y=80)
num2 = hm.Entry(cal,  width=40)
num2.place(x=40, y=80,width=100,height=30)



#layout of buttons in the interface
add  = hm.Button(cal, text='+', command=addition).place(x=12, y=130,width=60,height=60)
subt = hm.Button(cal, text='-', command=subtraction).place(x=75, y=130,width=60,height=60)
mult = hm.Button(cal, text='*', command=multiplication).place(x=138, y=130,width=60,height=60)
div  = hm.Button(cal, text='/', command=division).place(x=200, y=130,width=60,height=60)

cal.mainloop()