import tkinter as tkr

def submit():
    username = entry.get()
    password = entry1.get()
    print("Hello ", username)
    print("Password: ", password)
    entry.config(state=tkr.DISABLED)
    entry1.config(state=tkr.DISABLED)

def delete():
    entry.delete(0, tkr.END)

def backspc():
    entry.delete(len(entry.get())-1, tkr.END)

root = tkr.Tk()

# entry box = text box that accepts a line of user input
entry = tkr.Entry(root, font=("Arial", 64),
              fg="green", bg="black")
entry.insert(0, "username")         # default text
entry.pack()

entry1 = tkr.Entry(root, font=("Arial", 64),
              fg="green", bg="black", show="*")
entry1.pack()

submit_button = tkr.Button(root, text="submit", command=submit)
submit_button.pack(side=tkr.RIGHT)

delete_button = tkr.Button(root, text="delete", command=delete)
delete_button.pack(side=tkr.RIGHT)

backspc_button = tkr.Button(root, text="backspace", command=backspc)
backspc_button.pack(side=tkr.RIGHT)

root.mainloop()
