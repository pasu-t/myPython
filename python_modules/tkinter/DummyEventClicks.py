import tkinter
window = tkinter.Tk()
window.title('GUI')

#creating3 different functions for 3 different events
def left_click(event):
	tkinter.Label(window, text = 'left click').pack()
def right_click(event):
	tkinter.Label(window, text = 'right click').pack()
def middle_click(event):
	tkinter.Label(window, text = 'middle click').pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", right_click)
window.bind("<Button-3>", middle_click)

window.mainloop()