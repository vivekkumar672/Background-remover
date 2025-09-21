from tkinter import *
import tkinter as tk
from tkinter import font, filedialog as fd
from PIL import Image, ImageTk
from rembg import remove


output = ''

def openFile():
    global output
    ftypes = ( ('JPG Image', '*.jpg'), ('PNG Image', '*.png') )
    filename = fd.askopenfilename(filetypes=ftypes, title= "0pen Image File", initialdir='./')
    #filename = filename

    img =  ImageTk.PhotoImage(Image.open(filename).resize((lb3.winfo_width(), lb3.winfo_height())))
    lb3.configure(image=img)
    lb3.image = img

    input = Image.open(filename)
    output = remove(input)
    img2 = ImageTk.PhotoImage(output.resize((200,200)))
    lb4.configure(image=img2)
    lb4.image = img2

def saveFile():
    global output
    ftypes = (('GIF Image', '*.gif'), ('PNG Image', '*.png'))
    filename = fd.askopenfilename(filetypes=ftypes, title="Save Convert Image", initialdir='./')
    output.save(filename)


win = tk.Tk()

fnt = font.Font(size=18)
fnt2 = font.Font(size=15)

container = LabelFrame(win, text= "Image Background Remover", font=fnt2)
container.pack(padx=20, pady=20)

lb1 = Label(container,text="source file", font=fnt2)
lb1.grid(row=0, column=0, padx=10)

lb2 = Label(container,text="Preview Image", font=fnt2)
lb2.grid(row=0, column=1, padx=10)

defaultImage = ImageTk.PhotoImage(Image.new("RGB", (300,300), "white"))

lb3 = Label(container, image= defaultImage)
lb3.grid(row=1, column=0, padx=10)

lb4 = Label(container, image= defaultImage)
lb4.grid(row=1, column=1, padx=10)

btn1 = Button(container, text="Open File", font=fnt2, command= openFile)
btn1.grid(row=2, column=0, padx=10)

btn1 = Button(container, text="Save File", font=fnt2, command= saveFile)
btn1.grid(row=2, column=1, padx=10)




win.geometry("800x600")
win.resizable(False,False)
win.title("Image Background Remover")
win.mainloop()


