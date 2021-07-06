from tkinter import *

root = Tk()

def printName(event):
    print("Satyam is my creator")

# button_1 = Button(root,text="Who is your creator",command=printName)

button_1 = Button(root,text="Who is your creator")
button_1.bind("<Button-1>",printName)

button_1.pack()

root.mainloop()
