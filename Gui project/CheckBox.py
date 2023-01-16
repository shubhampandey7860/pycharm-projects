from tkinter import *

App = Tk()
App.title('CheckBox')
App.geometry('300x300')
#
display=Label(App, text='choose your option')
display.pack()

check = StringVar()
chk = Checkbutton(App, text='Checkbox', variable=check, onvalue='yes', offvalue='no')
chk.deselect()
chk.pack()


# function
def show():
    msg = Label(App, text=check.get())
    msg.pack()


# Button
B = Button(App, text='click', command=show)
B.pack()

App.mainloop()
