import tkinter as tkr

count = 0
def click():
    global count
    count += 1
    print(count)

root = tkr.Tk()
photo = tkr.PhotoImage(file='like.png')

# button = if you click it, it does stuff
b = tkr.Button(root, text="Like!", font=('Comic Sans', 32),
               fg='#00FF00', bg='#000000',
               activeforeground="#00FF00", activebackground="#000000",  # fg and bg color upon hovering the mouse
               image=photo, compound='left',
               state=tkr.ACTIVE, command=click)
b.pack()

root.mainloop()