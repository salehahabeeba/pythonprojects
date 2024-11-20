#QUIZ

while(True):
    inp = int(input("enter your number\n"))
    if inp<=100:
        print("try again")
        continue
    else:
        print("congratulations you've entered a number greater than 100\n")
        break

