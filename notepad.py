import tkinter
from tkinter import StringVar, IntVar, END, filedialog
import tkinter.scrolledtext
from PIL import ImageTk, Image
from tkinter import messagebox

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
#event parameter is automitically passed by the dropdown, so it must be included
# the function declaration
def change_font(event):
    '''Change the given font based on drop box options'''
    if font_option.get() == 'None':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())
    
    #Change font style
    input_text.config(font=my_font)


def new_note():
    '''Create a new note, essentially clears the screen'''
    #Use messsage box to check yes/no on new note w.o saving
    question = messagebox.askyesno("New Note", 'Are you sure you want to start a new note?')
    if question:
        #Scrolled text widgets starting index is 1.0, not 0!
        input_text.delete(1.0, END)


def close_note():
    '''Closes the note, essentially closing the program'''
    #Use messsage box to check yes/no on new note w.o saving
    question = messagebox.askyesno("Close Note", 'Are you sure you want to close notepad?')
    if question:

        #Scrolled text widgets starting index is 1.0, not 0!
        root.destroy()


def save_note():
    '''Save given note. First three lines are saved as font family, size, and option.'''
    #Use filedialog to get location and name of where/what to save teh file
    save_name = filedialog.asksaveasfilename(initialdir="./", title='Save Note', defaultextension=".txt",
                                         filetypes=(("Text files", '*.txt'), ('All files', ('*.*'))))
    with open(save_name, 'w') as f:
        #first 3 lines hold font family, size, and option (cast size to a string)
        f.write(font_family.get() + '\n')
        f.write(str(font_size.get()) + '\n')
        f.write(font_option.get() + '\n')
        #write remining text to the file
        f.write(input_text.get('1.0', END))
        f.close()


def open_note():
    '''Open a previously saved note. Should set the font family, size, and option'''
    #First set font, then load text
    open_name = filedialog.askopenfilename(initialdir="./", title='Save Note',
                                         filetypes=(("Text files", '*.txt'), ('All files', ('*.*'))))
    with open(open_name, 'r') as f:
        #clear current text
        input_text.delete('1.0', END)
        #First 3 lines are font family, size, and option
        #Must strip \n from end of line
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())
        #Call change font and pass an arbitrary value
        change_font(1)
        #read rest of ile and insert into text field
        text = f.read()
        input_text.insert('1.0', text)



#GUI layout
#Create frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout for menu frame
#create menu with new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('./images/new.png'))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('./images/open.png'))
open_button = tkinter.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('./images/save.png'))
save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('./images/close.png'))
close_button = tkinter.Button(menu_frame, image=close_image,
                              command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

#Create a list of fonts to use
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria',
            'Georgia', 'MS Gothic', 'SimSun', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('terminal')
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

#Create a list of font sizes
sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['None', 'bold', 'italic']
font_option = StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command=change_font)
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
