from tkinter import *

App = Tk()
App.title('Radio Button')
App.geometry('300x300')

# radiobutton
choice = StringVar()
rb1 = Radiobutton(App, text='option 1', variable=choice, value='Rb1 selected')
rb2 = Radiobutton(App, text='option 2', variable=choice, value='Rb2 selected')
rb1.select()
rb2.deselect()
rb1.pack()
rb2.pack()


# function
def show():
    msg = Label(App, text=choice.get())
    msg.pack()


B = Button(App, text='show', command=show)
B.pack()

App.mainloop()
