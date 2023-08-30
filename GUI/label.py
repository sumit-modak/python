import tkinter as tkr

root = tkr.Tk()
photo = tkr.PhotoImage(file='logo.png')

# Label = an area widget that holds texts, images within a window
l = tkr.Label(root, text="Hi Bro, do you even code?", 
              font=('Arial', 32, 'bold'), 
              fg='green', bg='black',           # text foreground and background color
              relief=tkr.RAISED,                # border style
              bd=10,                            # border size
              padx=10, pady=10,                 # adds horizontal and vertical padding between border and text
              image=photo,                      # adds image to the label
              compound='bottom')                # reletive position of image to text

l.pack()                      # adds label to the window
# l.place(x=0, y=0)           # adds label according to the given pixels


root.mainloop()