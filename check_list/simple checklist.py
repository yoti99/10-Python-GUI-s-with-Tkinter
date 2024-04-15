# Simple Checklist
import tkinter
from tkinter import END, ANCHOR

# Define window
root = tkinter.Tk()
root.title('Simple checklist')
root.iconbitmap('check.ico')
root.geometry('400x400')
root.resizable(0,0)

# Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = '#e84a3e'
button_color = '#dc951b'
root.config(bg=root_color)

# Define functions
def add_item():
    """Add an individual Item to the list box"""
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

def remove_item():
    """Remove the selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)

def clear_list():
    """Delete all elements from the listbox"""
    my_listbox.delete(0, END)

def save_list():
    """Save the list to a simple txt file"""
    with open('checklist.txt', 'w') as f:
        # listbox.get() returns a tuple..
        list_tuple = my_listbox.get(0,END)
        for item in list_tuple:
            # Take proper precautions to include only one \n for formatting Purposes
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + "\n")
        
def open_list():
    """Open the list upon starting the program if there is one"""
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                my_listbox.insert(END, line)
    except:
        return

# Define Layout

# Create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

# input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tkinter.Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color, command=add_item)
list_entry.grid(row=0, column=0,padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

# output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, height=15, width=45, borderwidth=3, font=my_font, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview) #Link scrollbar to listbox
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky='NS')

# Button Frame layout
list_remove_button = tkinter.Button(button_frame, text='Remove Item', borderwidth=2, font=my_font, bg=button_color, command=remove_item)
list_clear_button = tkinter.Button(button_frame, text='Clear List', borderwidth=2, font=my_font, bg=button_color, command=clear_list)
save_button = tkinter.Button(button_frame, text='Save List', borderwidth=2, font=my_font, bg=button_color, command=save_list)
quit_button = tkinter.Button(button_frame, text='Quit', borderwidth=2, font=my_font, bg=button_color, command=root.destroy)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)

# Open the previous list if available
open_list()

# Run the root windows main loop
root.mainloop()