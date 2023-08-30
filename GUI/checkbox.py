import tkinter as tkr

def display():
    if(x.get()==1):                 # x.get()=='YES'  x.get()
        print("You agree")
    else:
        print("You don't agree")

root = tkr.Tk()

x = tkr.IntVar()        # StringVar, BooleanVar
photo = tkr.PhotoImage(file='logo.png')
check_button = tkr.Checkbutton(root, 
                               text="I agree to terms and polices",
                               variable=x, 
                               onvalue=1, offvalue=0,       # [YES, NO], [True, False]
                               command=display,
                               fg="green",
                               bg="black",
                               activebackground="black",
                               activeforeground="green",
                               padx=25,
                               pady=10,
                               image=photo,
                               compound='left')
check_button.pack()
root.mainloop()
