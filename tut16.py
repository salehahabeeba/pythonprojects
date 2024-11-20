#exercise GUESS THE NUMBER
n=17
i=1
print("you have only 5 guesses to guess the correct number")

while(i<=5):
    inp=int(input("guess the number\n"))

    if inp<n:
        print("increase your number")
        print("-----------------------")

    elif inp>n:
            print("decrease your number")
            print("-----------------------")

    elif inp==n:
     print("congratulations you have correctly guessed the number")
     print("no. of guesses you took",i)
     break
    print("number of guesses left",5- i)
    i = i + 1

if i>5:
    print("game over! you've crossed the limit of your guesses ")
