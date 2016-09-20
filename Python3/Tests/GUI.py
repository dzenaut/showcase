from tkinter import *

class View():
    #Tk() creates a toplevel widget, usually the main window. Only to be instantiated once in an application
    def __init__(self):
        self.window = Tk()
        self.button = Button(self.window)
        #self.button.pack(side=TOP, expand=True)
        self.button.config(fg = 'red', text='Button')
        self.button.grid(sticky='nsew')






#Widget class is only meant to be subclassed to make real widgets

view = View()
view.window.mainloop()
