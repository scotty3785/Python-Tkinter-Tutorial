from tkinter import *
"""A button - what can we do with it?
Well lets make it change the colour of the text label 
and change the style of the button when it is pressed"""

class App(Frame):
    """Our Application. We inherit all the properties
    and methods of a Tkinter Frame"""
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.lblHello = Label(self,text="Hello World")
        self.lblHello['fg'] = "red"
        self.lblHello.grid()
        self.btnStart = Button(self,text="Click Me")
        self.btnStart['command'] = self._onStartClick
        self.btnStart.grid()
    def _onStartClick(self):
        """This method is called when the start button is pressed.
        If the button colour is the default, set it to red and sink the button
        Otherwise set it to the default again and raise the button"""
        if self.btnStart['fg'] == "SystemButtonText":
            self.btnStart['fg'] = "red"
            self.btnStart['relief'] = "sunken"
        else:
            self.btnStart['fg'] = "SystemButtonText"
            self.btnStart['relief'] = "raised"

def main():
    root = Tk()
    app = App(master=root)
    app.grid()

"""This is the code that is executed by python when we run this .py file"""
if __name__ == '__main__':
    main()
