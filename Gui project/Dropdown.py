from tkinter import *

# Application window
App = Tk()
App.title('Dropdowns')
App.geometry('300x300')
menu_ch = StringVar()
option = ['red', 'green', 'blue', 'white', 'black']
menu = OptionMenu(App, menu_ch, *option)
menu.pack()
menu_ch.set('white')

output = Toplevel()
output.title('output')


#
def show():
    msg = Label(output, text=menu_ch.get(), background=menu_ch.get(), fg='white')
    msg.pack()


#
B = Button(App, text='show', command=show)
B.pack()

App.mainloop()
