
import tkinter as tk

root = tk.Tk()

# hola mundo orientado a objetos
class helloworld(tk.Frame):

	def __init__(self, parent):
		super(helloworld, self).__init__(parent)

		self.label = tk.Label(self, text = 'hello world!')
		self.label.pack(padx = 20, pady = 20)


if __name__ == "__main__" :
	# root = tk.Tk()
	main = helloworld(root)
	main.pack(fill = 'both', expand = True)
	root.mainloop()