import tkinter
window = tkinter.Tk()
window.title('GUI')

logo1 = tkinter.PhotoImage(file = "C:/workspace/mypython/python_modules/tkinter/Adtran.png")
tkinter.Label(window, image = logo1).pack()

window.mainloop()