import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

# needed to get ttk.Label colors to work properly on OS X
style = ttk.Style()
style.theme_use('classic')

label = ttk.Label(root, text = 'Hey There')
label.pack()
label.config(foreground = 'blue')
label.config(background = 'yellow')

root.mainloop()

