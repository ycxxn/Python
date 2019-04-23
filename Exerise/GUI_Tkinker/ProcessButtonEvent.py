from tkinter import *

def processOK():
    print("OK button is clicked")
def processCancel():
    print("Cancel button is clicked")

window=Tk()
button_ok=Button(window,text="OK",fg="blue",command=processOK)
button_cancel=Button(window,text="Cancel",bg="yellow",command=processCancel)

button_ok.pack()
button_cancel.pack()

window.mainloop()