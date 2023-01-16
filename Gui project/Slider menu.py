from tkinter import *
from tkinter import Scale

App = Tk()
App.title('slider menu')
slid_value = IntVar()
App.geometry('300x300')
sli = Scale(App, from_=0, to=100)

App.mainloop()
