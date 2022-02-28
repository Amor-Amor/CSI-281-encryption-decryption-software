import tkinter as tk
from turtle import bgcolor
import csi280_codec

from tkinter import *

m = tk.Tk()

def move_window(event):
    m.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

# Sets window color
m.configure(bg='grey10')
#m.title('Encryption')

in_box = tk.StringVar()

def click_encrypt_button():
    print("en_str: " + in_box.get())
    # outputBox = csi280_codec.encode(in_box.get())
    # outputLabel.config(text="changed text!")

def click_decrypt_button():
    print("de_str: " + in_box.get())
    # outputBox = csi280_codec.decode(in_box.get())

#top bar set up
top_bar= Frame(m, bg='grey10', relief='raised', bd=2)
top_bar_title = Label(top_bar, text='Encryption/Decryption GUI', font=('courier', 10), bg='grey10', fg = 'grey80')
close_button= Button(top_bar, text="X", bg='grey15', fg='grey80', command=m.destroy)

#creates main window
main_window= Canvas(m, bg='grey10')

# Selection box for user to select encryption algorithm
algorithm_selector_label = Label(main_window, text='Select Algorithm: ', font=('courier', 8), bg='grey10', fg='grey80').grid(row=1, column=0, columnspan=1, padx=10, pady=10)
algorithms = ['Caesar', 'None']
selected_algorithm = StringVar(m)
selected_algorithm.set('Caesar')
selection_box = OptionMenu(main_window, selected_algorithm, *algorithms)
selection_box.config(bg= 'grey15', fg='grey80', font=('courier', 8))
selection_box_menu = main_window.nametowidget(selection_box.menuname)
selection_box_menu.config(font=('courier', 8))
selection_box.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

# Text and key entry fields
text_entry_label = Label(main_window, text='Enter Text: ', bg='grey10', fg='grey80', font=('courier', 8)).grid(row=2, column=0, columnspan=1, padx=5, pady=5)
text_entry = tk.Entry(main_window, textvariable=in_box, font=('courier', 8), bg='grey15', fg='grey80').grid(row=2, column=1, padx=5, pady=5)
key_entry_label = Label(main_window, text='Key: ', bg='grey10', fg='grey80', font=('courier', 8)).grid(row=2, column=2, columnspan=1, padx=5, pady=5)
key_entry = Text(main_window, height=1, width=5, bg='grey15', fg='grey80', font=('courier', 8)).grid(row=2, column=3, padx=5, pady=5)

# Encrypt and Decrypt Buttons
encrypt_button = Button(main_window, text='Encrypt', command=click_encrypt_button, bg='grey15', fg='grey80', font=('courier', 8)).grid(row=3, column=1, padx=10, pady=10)
decrypt_button = Button(main_window, text='Decrypt', command=click_decrypt_button, bg='grey15', fg='grey80', font=('courier', 8)).grid(row=3, column=2, padx=10, pady=10)

# Output Label and Box
output_label = Label(main_window, text="Output: ",bg='grey10', fg='grey80', font=('courier', 8)).grid(row=4, column=0, padx=10, pady=10)
output_box = Text(main_window, height=1, width=40, bg='grey15', fg='grey80', font=('courier', 8)).grid(row=4, column=1, columnspan=2, padx=10, pady=10)

# Sets window geometry and title bar
m.overrideredirect(True)
m.geometry('550x210')
top_bar.pack(expand=1, fill=X)
top_bar_title.pack(side=LEFT)
close_button.pack(side=RIGHT)
main_window.pack(expand=1, fill=BOTH)
top_bar_title.bind('<B1-Motion>', move_window)
top_bar.bind('<B1-Motion>', move_window)

#runs GUI
m.mainloop()