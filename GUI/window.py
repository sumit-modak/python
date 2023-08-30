import tkinter as tkr

root = tkr.Tk() # instantiates an instance of a window 
root.geometry("800x800")
root.title("Application")

icon = tkr.PhotoImage(file="logo.png")
root.iconphoto(True, icon)

root.config(background="black")

root.mainloop()
