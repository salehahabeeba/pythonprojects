import random
print("The rules of the game are\n1.Stone will kill the scissor\n2.Scissor will cut the paper\n3.Paper will cover the"
      "stone ")
l = ["st", "pp", "sc"]
user_points = 0
computer_points = 0
print("You have only 10 chances")
i = 1
def
while (i <= 10):
    inp = input("choose \nss for snake\npp for paper\nsc for scissor\n")
    ran = random.choice(l)