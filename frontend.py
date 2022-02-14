import tkinter

m = tkinter.Tk()

m.title('Encryption')
button = tkinter.Button(m, text='Close', width=25, command=m.destroy)
button.pack()

m.geometry("500x200")
m.mainloop()
