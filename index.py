from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from  stegano import lsb
from tkinter import messagebox

root=Tk()
root.title("Message Cracker")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

#icon
filename=""
# for open image
def openimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image file",filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("JPEG file","*.jpeg"),("all file",".txt")))

    if filename:
        img=Image.open(filename)
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img,width=250,height=250)
        lbl.image=img


def SAVE():
    global secret
    message=text1.get(1.0,END)
    if filename and message:
        out_put=filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Save Image file",
            defaultextension=".png",
            filetypes=(("PNG file",".*png"),("all files","."))

        )
        if out_put:
            secret=lsb.hide(str(filename),message)
            secret.save(out_put)
            messagebox.showinfo("Success","Message hidden successfully!")
            text1.delete(1.0, END)
            lbl.configure(image=None) 
            lbl.image = None

        else:
            messagebox.showwarning("Warning","Please provide a valid output file name!")
    else:
        messagebox.showwarning("Warning","Please select image and enter a message!")


    


def Show():
    global filename
    if filename:
        clear_message=lsb.reveal(filename)
        text1.delete(1.0,END)
        text1.insert(END,clear_message)
    else:
        messagebox.showwarning("Warning","Please select an image")

# def save():
#     secret.save("image.png");

image = Image.open("Images/download.jpg")
new_size = (150, 75)
image = image.resize(new_size)
# Convert the image to a compatible format (e.g., GIF)
image = image.convert("RGB")

# Create a PhotoImage object from the converted image
image_icon = ImageTk.PhotoImage(image)

root.wm_iconphoto(False,image_icon)

#logo
logo=ImageTk.PhotoImage(image)
Label(root,image=logo,bg="#2f4155").place(x=20,y=10)


Label(root,text="StegoSec",bg="#2d4155",fg="white",font="Hacked-KerX.ttf 29 bold").place(x=300,y=25)

f=Frame(root,bd=3,bg="black",width=340,height=285,relief=GROOVE)
f.place(x=9,y=102)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

frame2=Frame(root,bd=3,width=340,height=285,bg="white",relief=GROOVE)
frame2.place(x=352,y=102)

# text
text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

Scrollbar1=Scrollbar(frame2)
Scrollbar1.place(x=320,y=0,height=300)

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

# //left button framw
frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=390)

Button(frame3,text="Open Image",width=10,height=2,font="Hacked-KerX.ttf 14 bold",command=openimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="Hacked-KerX.ttf 14 bold",command=SAVE).place(x=180,y=30)

Label(frame3,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

# //right button frame

frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=390)
Button(frame4,text="Hide Data",width=10,height=2,font="Hacked-KerX.ttf 14 bold",command=SAVE).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="Hacked-KerX.ttf 14 bold",command=Show).place(x=180,y=30)

Label(frame4,text="Picture,Data,Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()