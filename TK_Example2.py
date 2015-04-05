from tkinter import *
"""A simple hello world example
We create a label inside our application with the text Hello World and
configure the foreground colour to be red."""

class App(Frame):
    """Our Application. We inherit all the properties
    and methods of a Tkinter Frame"""
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.lblHello = Label(self,text="Hello World")
        self.lblHello['fg'] = "red"
        self.lblHello.grid()
        self.btnStart = Button(self,text="Click Me")
        self.btnStart.grid()

def main():
    root = Tk()
    app = App(master=root)
    app.grid()

"""This is the code that is executed by python when we run this .py file"""
if __name__ == '__main__':
    main()
