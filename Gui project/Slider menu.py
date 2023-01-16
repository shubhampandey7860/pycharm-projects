from tkinter import *
from tkinter import Scale

App = Tk()
App.title('slider menu')
slid_value = IntVar()
App.geometry('300x300')
sli = Scale(App, from_=0, to=100,variable=slid_value,orient=HORIZONTAL)
sli.pack()


#
def show_slider():
    msg = Label(App, text=slid_value.get(),font=('arial',10))
    msg.pack()


B = Button(App, text='show', command=show_slider,background='red',foreground='white',font=('arial',10))
B.pack()

App.mainloop()
