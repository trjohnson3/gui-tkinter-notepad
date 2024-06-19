import tkinter
from tkinter import StringVar, IntVar, scrolledtext
import tkinter.scrolledtext
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
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

#Create a list of font sizes
sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes)
font_size.set(12)
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['None', 'Bold', 'Italics']
font_option = StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options)
font_option.set('None')
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

#Layout for text frame
my_font = (font_family.get(), font_size.get())
#Create input text as a scroll text widget
#Set default height and width to be larger than the window so that on the smallest
#font size, the windo is constant
input_text = tkinter.scrolledtext.ScrolledText(text_frame, bg=text_color, font=my_font,
                                               width=1000, height=100)
input_text.pack()

#Run app
root.mainloop()
