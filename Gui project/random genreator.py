from tkinter import *
from random import randint

# window object
App = Tk()

# App title
App.title('Random Number Generator')
App.geometry('350x350')


def show_number():
    msg = Label(App, text=randint(1, 100))
    msg.pack()


# Button
B = Button(App, text='Generate', command=show_number)
B.pack()

App.mainloop()
