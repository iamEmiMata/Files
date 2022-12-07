
import tkinter as tk

# tk._test()

# hello world from tkinter!

root = tk.Tk()
label = tk.Label(root, text = 'hola, hola... ') # Create a text label
label.pack(padx = 20, pady = 20) # Pack it into the window

# salida
root.mainloop()