from tkinter import *

class ProcessButtonEvent:
    
    def __init__(self):
        window=Tk()
        button_ok=Button(window,text="OK",command=self.ProcessOK)
        button_cancel=Button(window,text="Cancel",command=self.ProcessCancel)
        button_ok.pack()
        button_cancel.pack()
        window.mainloop()
        
    def ProcessOK(self):
        print("OK is clicked")

    def ProcessCancel(self):
        print("Cancel is clicked")

if __name__ == '__main__':
    ProcessButtonEvent()
