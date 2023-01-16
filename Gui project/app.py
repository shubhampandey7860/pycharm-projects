from tkinter import *

# Tk() class is used for creating window
App = Tk()

# title method is used to change windows title

App.title('APP')

# Geometry : window size

App.geometry('300x300')


# function
def show_message():
    msg = Label(App, text='Have a nice day')
    msg.pack()


# Button
B = Button(App, text='click me', command=show_message)
B.pack()

# Label

Display = Label(App, text='Application window')
Display.pack()

# window.mainloop() tells Python to run the Tkinter event loop

App.mainloop()
