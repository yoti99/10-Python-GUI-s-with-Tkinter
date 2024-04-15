# Images
import tkinter
from PIL import ImageTk, Image

# Define the window
root = tkinter.Tk()
root.title('Image Basics!')
root.iconbitmap('thinking.ico')
root.geometry('700x700')

# Define functions
def make_image():
    '''Print an Image'''
    global dog_image
    # Using PIL for jpg
    dog_image = ImageTk.PhotoImage(Image.open('dog.jPeg'))
    dog_label = tkinter.Label(root, image=dog_image)
    dog_label.pack()

# Basics...works for png
my_image = tkinter.PhotoImage(file='shield.png')
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

# Not for jpeg
# dog_image = tkinter.PhotoImage(file='dog.jpeg')
# dog_label = tkinter.Label(root, image=dog_image)
# dog_label.pack()

make_image()

# Run windows main loop
root.mainloop()