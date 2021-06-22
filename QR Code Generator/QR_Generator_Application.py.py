from tkinter import *                  #standard Python interface to the Tk GUI toolkit
from tkinter import messagebox 
import pyqrcode                        #QR code generator package 
import os                              #fetching its contents, changing and identifying the current directory
window = Tk()
window.title("QR Code Generator")

def generate():                                             #created a function to generate the QR code #Saranraj😎
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!","Please Enter the Subject")
    try:
        showcode()
    except:
        pass

def showcode():                                                  #created a function to show the QR code 
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="showing QR code for:" + subject.get())
def save():                                                    #created a function to save the QR code 
    dir = path1 = os.getcwd() + "\\QR codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir,name.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Error!","File name can not be empty!")
    except:
        messagebox.showinfo("Error!","Please generate the code first")

lab1 = Label(window, text="Enter subject",font=("Helvetica", 12))       # Helvetica as the default sans-serif font in Matplotlib
lab1.grid(row=0,column=0,sticky=N + S + E + W)                          # collection of functions that make matplotlib

lab2 = Label(window, text="Enter File Name",font=("Helvetica",12))
lab2.grid(row=1,column=0, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Helvetica,12"))
subjectEntry.grid(row=0,column=1, sticky=N + S + E + W)

name = StringVar()
nameEntry = Entry(window, textvariable=subject, font=("Helvetica,12"))
nameEntry.grid(row=1,column=1, sticky=N + S + E + W)

createButton = Button(window,text="create QR code",font=("Helvetica",12),width=15,command=generate)      # create button
createButton.grid(row=0,column=3,sticky=N + S + E +W)

notificationLabel = Label(window)
notificationLabel.grid(row=2,column=1,sticky=N + S + E + W)

subLabel = Label(window, text="")
subLabel.grid(rows=3,column=1,sticky=N + S + E + W)

showButton = Button(window,text="save as PNG",font=("Helvetica",12),width=15,command=save)
showButton.grid(row=1,column=1, sticky=N + S + E + W)

totalRows = 3
totalCols = 3
for row in range(totalRows + 1):
    window.grid_rowconfigure(row,weight=1)
for col in range(totalCols + 1):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()

#Saranraj😎



