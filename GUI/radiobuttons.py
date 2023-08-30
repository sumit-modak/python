import tkinter as tkr

root = tkr.Tk()

def order():
    if x.get()==0:
        print("You ordered pizza")
    elif x.get()==1:
        print("You ordered hamburger")
    elif x.get()==2:
        print("You ordered hotdog")
    else:
        print("huh?")

# radio button = similar to checkbox, but you can only select one from a group
x = tkr.IntVar()
pizzaimg = tkr.PhotoImage(file='pizza.png')
hamburgerimg = tkr.PhotoImage(file='hamburger.png')
hotdogimg = tkr.PhotoImage(file='hotdog.png')
foodimg = [pizzaimg, hamburgerimg, hotdogimg]

food = ["pizza", "hamburger", "hotdog"]
for index in range(len(food)):
    radiobutton = tkr.Radiobutton(root, 
                                  text=food[index],     # adds text to radio buttons
                                  variable=x,   # groups radiobuttons together if they share the same variable
                                  value=index,  # assigns each radiobutton a different value
                                  padx=25,
                                  image=foodimg[index], # adds image to radiobutton
                                  compound='left',
                                  indicatoron=0,        # eliminate circle indicators
                                  width=400,
                                  command=order)
    radiobutton.pack(anchor=tkr.W)
root.mainloop()
