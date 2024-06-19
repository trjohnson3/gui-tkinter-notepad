import tkinter
from tkinter import StringVar
from PIL import ImageTk, Image

#Define window
root = tkinter.Tk()
root.title('Notepad')
root.iconbitmap('./images/notepad.ico')
root.geometry('600x600')
root.resizable(0, 0)

#Define fonts and colors
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'
root.config(bg= root_color)

#Define functions


#GUI layout
#Create frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout for menu frame
#create menu with new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('./images/new.png'))
new_button = tkinter.Button(menu_frame, image=new_image)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('./images/open.png'))
open_button = tkinter.Button(menu_frame, image=open_image)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('./images/save.png'))
save_button = tkinter.Button(menu_frame, image=save_image)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('./images/close.png'))
close_button = tkinter.Button(menu_frame, image=close_image,
                              command=root.destroy)
close_button.grid(row=0, column=3, padx=5, pady=5)

#Create a list of fonts to use
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria',
            'Georgia', 'MS Gothic', 'SimSun', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families)
font_family.set('terminal')
#Set width to hold longest font and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4)

#Run app
root.mainloop()
