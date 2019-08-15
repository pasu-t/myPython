import tkinter

window = tkinter.Tk()
window.title("MyTkinter")

#creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

#now create some widgets in top_frame and bottom_frame

btn1 = tkinter.Button(top_frame, text = 'button1', fg = "red").pack()
btn2 = tkinter.Button(top_frame, text = 'button2', fg = "green").pack()
btn3 = tkinter.Button(bottom_frame, text = 'button3', fg = "blue").pack(side = 'left')
btn4 = tkinter.Button(bottom_frame, text = 'button4', fg = "purple").pack(side = 'left')

window.mainloop()
