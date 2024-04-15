# Notepad
import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

# Define window
root = tkinter.Tk()
root.title('NotePad')
root.iconbitmap('pad.ico')
root.geometry('600x600')
root.resizable(0, 0)

# Define fonts and colors
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'
root.config(bg=root_color)

# Define Functions
def change_font(event):
    """Change the given font based off of given dropbox options"""
    if font_option.get() == 'none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

    # Change the font style
    input_text.config(font=my_font)

def new_note():
    """Create a new note which essentially clears the screen"""
    # Use the messagebox to ask for a new note
    question = messagebox.askyesno("New note", "Are you sure you want to start a new Note?")
    if question == 1:
        # ScrolledText starting widgets starting index is 1.0 not 0.
        input_text.delete('1.0', END)

def close_note():
    """Close the note which essentially quits the program"""
    # use a message box to ask to close
    question = messagebox.askyesno("Close Note", "Are You sure you want to close your Note?")
    if question == 1:
        root.destroy()

def save_note():
    """Save the given note. First three lines are saved as font family, font size, font option."""
    # Use filedialog to get location and name of where/what to save the file as.
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note", filetypes=(("Text Files", "*txt"), ("All Files", "*.*")))
    with open(save_name, 'w') as f:
        # First three lines of save file are font_family, font_size, and font_options. Font_size must be a string and not an int.
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_option.get() + "\n")

        # Write remaining text in field to the file
        f.write(input_text.get("1.0", END))

def open_note():
    """Open a previous;y saved note. First three lines of note are font family, font size, and font option. First set the font then load the text. """
    # USe filedialog to get location and direction of note file
    open_name = filedialog.askopenfilename(initialdir="./", title='Open Note', filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    with open(open_name, 'r') as f:
        # Clear the current text
        input_text.delete("1.0", END)

        # First three lines are font_family, font-size, and font_option.. You must strip the newline char at the end of each line!
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        # Call the change font for these .set() and pass the arbitary value
        change_font(1)

        # Read the rest of the file and insert it into the text field
        text = f.read()
        input_text.insert("1.0", text)

# Define Layout
# Define frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Layout for menu frame
# Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

# Create list of fonts to use
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambri', 'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wing dings', 'Carlito']
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Terminal')

# Set the with to fit 'Times New Roman' and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column= 4, padx=5, pady=5)

sizes = [2, 4, 6, 8, 10, 12, 16, 32, 48, 56, 64, 82, 94]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)

# Set width to be constant even if it is 8.
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['none', 'bold', 'italic']
font_option = StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command=change_font)
font_option.set('none')

# Set width to be constant
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

# Layout ofr the text frame
my_font = (font_family.get(), font_size.get())

# Create input_text as a scrolltext so you can scroll through the text field
# Set default width and height to be more than the window size so that on the smallest text sizethe text field size is constant
input_text = tkinter.scrolledtext.ScrolledText(text_frame, width=1000, height=100, bg=text_color, font=my_font)
input_text.pack()

# Run the root windows menu loop
root.mainloop()