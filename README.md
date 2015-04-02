# Python-Tkinter-Tutorial
Examples used as part of a Python Tkinter Tutorial

In order to create Graphical User Interfaces, Python comes with Tkinter as standard. Tkinter isn't fully features or particularly beautiful but it provides basic widget types that you can use to quickly create application that you can run on your Raspberry Pi.

Lets sort out some terminology first. 
A window is what you see when you open any graphical program on your computer, it will include the minimise, maximise and close buttons depending on your operating system. It will also show the name of the application. 
A frame is a blank object that exists inside a window. It can contain buttons, text entry fields, labels, checkboxes and many more, these are all called widgets.
A widgets are object that can be used as part of your application these can be buttons, text entries, check boxes or something more complex like a a collection of widgets that are joined together to create something more complicated, we will create an example of this in this tutorial.

All the examples in this tutorial have been developed for Python 3 using IDLE3 on a Raspberry Pi. You can find IDLE3 on Raspbain in the programming menu.

## Tutorial 1 - Our First Tkinter Program
Our first example isn't very exciting but it does introduce you to the basics needed to get create a create a simple Tkinter Class and make this visible to the user.
Open IDLE3 from the programming menu, and from the "File" menu select "New File". This will bring up a blank text editor window. Enter the python code in the box below. Python is very strict with indentation so make sure you put the correct number of spaces before each line of code.
To save the file, select "Save" from the "File" menu. Give the file a name remembering to give the file the .py extension and press "Save".
Now that we've saved the file lets run it and see what happens. To run the program, either press F5 or click on "Run Module" from the "Run" menu.
Not very impressive is it!! What we have done is to tell python to create a Tkinter window and draw a blank Frame on to the window. 

## Tutorial 2 - Adding some widgets.
