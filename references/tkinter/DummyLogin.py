import tkinter

window = tkinter.Tk()
window.title("MyTkinter")

tkinter.Label(window, text = "username").grid(row = 0) #this is placed in 0 0
tkinter.Entry(window).grid(row = 0, column = 1) #this is placed in 0 1
tkinter.Label(window, text = "password").grid(row = 1, column = 0) #this is placed in 1 0
tkinter.Entry(window).grid(row = 1, column = 1) #this is placed in 1 1

tkinter.Checkbutton(window, text = "Keep me logged in").grid(columnspan = 2) # 'columnspan' tells to take the width of 2 columns .
                                                                             # you can also use 'rowspan' in the similar manner

window.mainloop()