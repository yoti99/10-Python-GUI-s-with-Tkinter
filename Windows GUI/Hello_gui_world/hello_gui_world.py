# Hello GUI World
# Icon from:  https://iconsmind.com
import tkinter
import PIL
from tkinter import BOTH, StringVar, END
from PIL import ImageTk, Image

# Define window
root = tkinter.Tk()
root.title("Hello GUI World")
root.iconbitmap('wave.ico')
root.geometry("400x400")
root.resizable(0, 0)

# Define Fonts and colors
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
root.config(bg=root_color)


# Define functions
def submit_name():
    """Say Hello to the User."""
    # Create label for the username based on the radio button values
    if case_style.get() == 'normal':
        name_label = tkinter.Label(output_frame, text="Hello " + name.get() + "! Keep learning Tkinter !", bg=output_color)
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text=("Hello " + name.get() + "! Keep learning Tkinter !").upper(), bg=output_color)

    # Pack label onto Screen
    name_label.pack()

# Define Layouts

# Define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# Create widgets
name = tkinter.Entry(input_frame, text="Enter your name", width=20)
submit_button = tkinter.Button(input_frame, text="submit", command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)

# create radio buttons for text display
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text="Normal Case", variable=case_style, value='normal',
                                    bg=input_color)
upper_button = tkinter.Radiobutton(input_frame, text="Upper Case", variable=case_style, value='upper', bg=input_color)
normal_button.grid(row=1, column=0, padx=2, pady=2)
upper_button.grid(row=1, column=1, padx=2, pady=2)

# Add an Image
smile_img = ImageTk.PhotoImage(Image.open('Smile1.png'))
smile_label = tkinter.Label(output_frame, image=smile_img, bg=output_color)
smile_label.pack()

# Clear the entry field for the next user
name.delete(0, END)

# Run root window's main loop
root.mainloop()
