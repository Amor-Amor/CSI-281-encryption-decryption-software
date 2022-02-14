import tkinter
from tkinter import *
m = tkinter.Tk()

#Sets window title
m.title('Encryption')

#title for GUI
titleLabel = Label(m, text='Encryption/Decryption GUI').grid(row=0, column=0, columnspan=4)

#Selection box for user to select encryption algorithm
algorithmSelectorLabel = Label(m, text='Select Algorithm: ').grid(row=1, column=0, columnspan=1, padx=10, pady=10)
algorithms =['Caesar','None']
selectedAlgorithm = StringVar(m)
selectedAlgorithm.set('Caesar')
selectionBox = OptionMenu(m, selectedAlgorithm, *algorithms)
selectionBox.grid(row=1, column=1, columnspan=3,padx=10,pady=10)

#Text and key entry fields
textEntryLabel= Label(m, text='Enter Text: ').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
textEntry = Text(m, height=1, width=20).grid(row=2, column=1, padx=5, pady=5)
keyEntryLabel = Label(m, text='Key: ').grid(row=2, column=2, columnspan=1, padx=5, pady=5)
keyEntry = Text(m, height=1, width=5).grid(row=2, column=3, padx=5, pady=5)

#Encrypt and Decrypt Buttons
encryptButton = Button(m, text='Encrypt').grid(row=3, column=1, padx=10, pady=10)
encryptButton = Button(m, text='Decrypt').grid(row=3, column=2, padx=10, pady=10)

#Output Label and Box
outputLabel = Label(m, text="Output: ").grid(row=4, column=0,padx=10, pady=10)
outputBox= Text(m,height=1, width=40).grid(row=4, column=1,columnspan=2, padx=10, pady=10)

#Close Button
button = tkinter.Button(m, text='Close', width=25, command=m.destroy).grid(row=5, column=1, columnspan=2, padx=10, pady=10)

#Sets window geometry and runs
m.geometry('550x250')
m.mainloop()
