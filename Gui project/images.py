from tkinter import *
from PIL import Image, ImageTk

app = Tk()
# setting icon for application
app.iconbitmap(r'images/python.ico')
app.title('App')
img = ImageTk.PhotoImage(Image.open(r'images/python_icon.png'))
lbl = Label(app, image=img)
lbl.pack()
app.mainloop()
