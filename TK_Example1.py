from tkinter import *
"""Our very basic Tkinter Application
This just creates a window with no widgets."""

class App(Frame):
    """Our Application. We inherit all the properties
    and methods of a Tkinter Frame"""
    def __init__(self,master=None):
        Frame.__init__(self,master)

def main():
    root = Tk()
    app = App(master=root)

"""This is the code that is executed by python when we run this .py file"""
if __name__ == '__main__':
    main()
