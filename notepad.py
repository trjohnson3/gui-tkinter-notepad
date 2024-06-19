import tkinter
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



#Run app
root.mainloop()
