import tkinter

window = tkinter.Tk()

topPart = tkinter.Frame(window)
topPart.pack()

bottomPart = tkinter.Frame(window)
bottomPart.pack(side=tkinter.BOTTOM)

button1 = tkinter.Button(topPart, text="the best button ever (button1)", fg="red")
button2 = tkinter.Button(topPart, text="the second best button ever (button2)", fg="green")
button3 = tkinter.Button(topPart, text="the third best button ever (button3)", fg="gray")
button4 = tkinter.Button(bottomPart, text="(button4)", fg="purple")

button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.LEFT)
button3.pack(side=tkinter.LEFT)
button4.pack(side=tkinter.BOTTOM)



window.mainloop()
