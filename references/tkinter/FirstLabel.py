import tkinter

window = tkinter.Tk()
window.title("MyTkinter")


#creating 3 simple labels containing any text

#sufficient width
tkinter.Label(window, text = 'Suff.width', fg = "white", bg = "black").pack()
#width of X
tkinter.Label(window, text = 'Taking all available X width', fg = "white", bg = "green").pack(fill = "x")
#height of Y
tkinter.Label(window, text = 'Taking all available Y height', fg = "white", bg = "purple").pack(side = 'left', fill = "y")

window.mainloop()
