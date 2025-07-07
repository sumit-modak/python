import random

ch = ["rock", "paper", "scissors"]
computer = 0
player = 0

print("Computer \t Player")
while computer < 5 and player < 5:
    cch = random.choice(ch)
    pch = input("Enter your choice : ")
    if pch == "rock":
        if cch == "paper":
            computer+=1
        elif cch == "scissors":
            player+=1
    elif pch == "paper":
        if cch == "rock":
            player+=1
        elif cch == "scissors":
            computer+=1
    elif pch == "scissors":
        if cch == "rock":
            computer+=1
        elif cch == "paper":
            player+=1

    if pch == ch[0] or pch == ch[1] or pch == ch[2]:
        print("Score : "+str(computer)+"\t"+str(player))
    else:
        print("Enter correctly (rock, paper or scissors)")

if computer == 5:
    print("computer won!")
else:
    print("player won!")