# Basic Windows
import tkinter

# Define window
root = tkinter.Tk()
root.title('Windows Basics!')
root.iconbitmap('thinking.ico')
root.geometry('250x400')
root.resizable(0,1)
root.config(bg='blue')

# Second Window
top = tkinter.Toplevel()
top.title('Second Window')
top.config(bg="#123456")
top.geometry('200x200+500+50')
# Run root windows main loop
root.mainloop()
