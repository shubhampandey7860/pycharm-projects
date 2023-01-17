from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

app = Tk()
# setting icon for application
app.iconbitmap(r'images/python.ico')
app.title('App')
app.geometry('300x400')


def img_select():
    global img
    app.fname = filedialog.askopenfilename(initialdir='images', title='choose file',
                                           filetypes=(
                                           ('PNG Images', '*.png'), ("ICON Files", '*.ico'), ("All files", '*.*')))
    B.destroy()
    img = ImageTk.PhotoImage(Image.open(app.fname))
    lbl = Label(app, image=img)
    lbl.pack()


B = Button(app, text='View', command=img_select)
B.pack()
app.mainloop()
