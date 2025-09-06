import tkinter
window = tkinter.Tk()
#to rename the title of the window
window.title('mytkinter')
#pack is used to show the object in the window
label = tkinter.Label(window, text="Hi welcome").pack()
window.mainloop()