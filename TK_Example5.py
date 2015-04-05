from tkinter import *
"""A button - what can we do with it?
Well lets make it change the colour of the text label 
and change the style of the button when it is pressed"""

class OnOffButton(Button):
    def __init__(self,master=None,onText=None,offText=None):
        self.onText = onText
        self.offText = offText
        Button.__init__(self,master,text=self.offText)
        self['command'] = self._onButtonClick
    def _onButtonClick(self):
        """This method is called when the start button is pressed.
        If the button colour is the default, set it to red and sink the button
        Otherwise set it to the default again and raise the button"""
        if self['fg'] == "SystemButtonText":
            self['fg'] = "red"
            self['relief'] = "sunken"
            self['text'] = self.onText
        else:
            self['fg'] = "SystemButtonText"
            self['relief'] = "raised"
            self['text'] = self.offText

class App(Frame):
    """Our Application. We inherit all the properties
    and methods of a Tkinter Frame"""
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.lblHello = Label(self,text="Hello World")
        self.lblHello['fg'] = "red"
        self.lblHello.grid()
        self.btnStart = OnOffButton(self,onText="Click Me Again",offText="Click Me")
        self.btnStart.grid()
        self.btn2 = OnOffButton(self,onText="Disable",offText="Enable")
        self.btn2.grid()

def main():
    root = Tk()
    app = App(master=root)
    app.grid()

"""This is the code that is executed by python when we run this .py file"""
if __name__ == '__main__':
    main()
