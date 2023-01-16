from tkinter import *
from random import choice

# window object
App = Tk()

# Geometry of window
App.geometry('250x100')

App.title('grid system')
App['background'] = 'blue'

# entry widget
inp = Entry(App, background='white', foreground='green')
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=5)


# function
def Random():
    Inp = inp.get().split(',')
    Choice = 'choice' + ': ' + str(choice(Inp))
    msg = Label(App, text=Choice, font=('courier', 12), background='white', foreground="red", relief='raised', width=15)
    # font : (name ,size)
    # relief=['raised','groove','flat','sunken','solid']
    # App['bg'] = choice(Inp)

    msg.grid(row=2, column=0,columnspan=2, padx=40, pady=5)
    if quit['state'] == DISABLED:
        quit['state'] = NORMAL


B = Button(App, text='choice', command=Random )
B.grid(row=1, column=0, padx=25, pady=5)
# quit button
quit = Button(App, text='quit', command=App.quit, state=DISABLED, background='red', foreground='white')
quit.grid(row=1, column=1, padx=25, pady=5)

# mainloop
App.mainloop()
