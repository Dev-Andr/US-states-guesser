from tkinter import *

window = Tk()
window.title("Proggrem")
window.minsize(width=500, height=300)

l1 = Label(text="Miles", font=("Jokerman", 22, "bold"))
l1.grid()

e1 = Entry(width = 10)
e1.insert(END,string = "0")
e1.grid(column=1,row=0)

l2 = Label(text="KM", font=("Jokerman", 22, "bold"))
l2.grid(row = 1)

l3 = Label(text="0", font=("Jokerman", 22, "bold"))
l3.grid(row = 1, column = 1)

def b():
    l3.config(text=(float(e1.get())*1.6))

b1 = Button(text="Calculate",command = b)
b1.grid(row=4)

window.mainloop()
