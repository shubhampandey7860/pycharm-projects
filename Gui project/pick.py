from tkinter import *
from random import choice

# window object
App = Tk()

# Geometry of window
App.geometry('400x200')

App.title('color picker')

# entry widget
inp = Entry(App)
inp.pack()


# function
def color():
    Inp = inp.get().split(',')
    # msg = Label(App, text=choice(Inp))
    App['bg'] = choice(Inp)

    # msg.pack()


B = Button(App, text='choice', command=color)
B.pack()
# quit button
quit = Button(App, text='quit', command=App.quit)
quit.pack()

# mainloop
App.mainloop()
