from tkinter import *

# window object
App = Tk()

# title
App.title('Entry Fields')
App.geometry('350x350')

# entry field
inp = Entry(App)
inp.pack()


# function
def show():
    msg = inp.get()
    output = Label(App, text=msg)
    output.pack()


# button
b1 = Button(App, text='get', command=show)
b1.pack()

# mainloop
App.mainloop()
