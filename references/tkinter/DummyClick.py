import tkinter
window = tkinter.Tk()
window.title('GUI')

def say_hi():
	tkinter.Label(window, text = 'hi').pack()

tkinter.Button(window, text = 'click me!', command = say_hi).pack()

window.mainloop()