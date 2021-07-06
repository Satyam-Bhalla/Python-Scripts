from tkinter import *
import tkinter.messagebox as tm

root = Tk()

# tm.showinfo('Window Title','Message box text')
answer = tm.askquestion('Question 1','Are you tired?')

if answer == 'yes':
    print('Yes')
else:
	print('No')
root.mainloop()
