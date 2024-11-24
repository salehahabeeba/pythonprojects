#Project- SNAKE,WATER AND GUN
import random
from sys import orig_argv
print("The rules of the game are-\n1.If you choose snake and I choose water then snake will drink the water and you win"
      "\n2.If you choose snake and I choose gun then gun will kill sSthe snake and I win\n3.If you choose gun and I choose"
      " water then gun will drown in water and I win \t......Vice Versa")
l=["S","W","G"]
user_points=0
computer_points=0
print("You have only 10 chances")
i=1
while(i<=10):
    inp=input("choose \nS for snake\nW for water\nG for gun\n")
    ran = random.choice(l)
    if ran=="S" and inp=="S":
        print("game is tied")
        print("No Points")
        print("your points",user_points)
        print("My points",computer_points)
        print("-----------------------------")
    elif ran=="W" and inp=="S":
        print("you won! My choice was water")
        user_points+=1
        print("your points", user_points)
        print("My points",computer_points)
        print("-----------------------------")
    elif ran=="G" and inp=="S":
        print("I won! My choice was gun" )
        computer_points+=1
        print("your points", user_points)
        print("My points", computer_points)
        print("-----------------------------")
    elif ran=="S" and inp=="W":
        print("I won! My choice was snake")
        computer_points += 1
        print("your points", user_points)
        print("My points", computer_points )
        print("-----------------------------")
    elif ran=="W" and inp=="W":
        print("game is tied")
        print("No Points")
        print("your points", user_points)
        print("My points", computer_points)
        print("-----------------------------")
    elif ran=="G" and inp=="W":
        print("You won! My choice was gun")
        user_points += 1
        print("your points", user_points)
        print("My points", computer_points)
        print("-----------------------------")
    elif ran=="S" and inp=="G":
        print("You won! My choice was snake")
        user_points += 1
        print("your points", user_points)
        print("My points", computer_points)
        print("-----------------------------")
    elif ran=="W" and inp=="G":
        print("I won! my choice was water")
        computer_points += 1
        print("your points", user_points)
        print("My points", computer_points)
        print("-----------------------------")
    elif ran=="G" and inp=="G":
        print("game is tied")
        print("No Points")
        print("your points", user_points)
        print("My points", computer_points)

    elif inp != l:
       print("Please enter the valid input")
    i=i+1
    print("-----------------------------")

    print("number of chances left",11-i)

else:
    print("Your points",user_points, "My points",computer_points)
    if user_points>computer_points:
        print("you have conquered the game with most number of points")
    elif user_points<computer_points:
        print("I have conquered the game with most number of points")
    elif user_points==computer_points:
        print("We both got same number of points. The game is tied")


