import datetime

while input:
    print("Note: For correct operations, you must enter the keys as suggested.")
    person = input("Whom? Enter 'hy' for harry, 'rn' rohan, 'hd' for hammad: ")
    rl = input("Enter 'r' for retrieve, 'l' for lock: ")
    en = input("Enter 'e' for exercise, 'n' for nutrition: ")


    # retrieves files
    def retrieve_harry_exercise():
        with open("harry_e.txt") as f:
            harry_exercise = f.read()
            print(harry_exercise)


    def retrieve_rohan_exercise():
        with open("rohan_e.txt") as f:
            rohan_exercise = f.read()
            print(rohan_exercise)


    def retrieve_hammad_exercise():
        with open("hammad_e.txt") as f:
            hammad_exercise = f.read()
            print(hammad_exercise)


    def retrieve_harry_nutrition():
        with open("harry_n.txt") as f:
            harry_nutrition = f.read()
            print(harry_nutrition)


    def retrieve_rohan_nutrition():
        with open("rohan_n.txt") as f:
            rohan_nutrition = f.read()
            print(rohan_nutrition)


    def retrieve_hammad_nutrition():
        with open("hammad_n.txt") as f:
            hammad_nutrition = f.read()
            print(hammad_nutrition)

            # write into files directly from the console


    def lock_harry_exercise():
        with open("harry_e.txt", "a") as f:
            f.write(f"\n{datetime.datetime.now()}\n")
            f.write(input())


    def lock_rohan_exercise():
        with open("rohan_e.txt", "a") as f:
            f.write(f"\n{datetime.datetime.now()}\n")
            f.write(input())


    def lock_hammad_exercise():
        with open("hammad_e.txt", "a") as f:
            f.write(f"\n{datetime.datetime.now()}\n")
            f.write(input())


    def lock_harry_nutrition():
        with open("harry_n.txt", "a") as f:
            f.write(f"\n{datetime.datetime.now()}\n")
            f.write(input())


    def lock_rohan_nutrition():
        with open("rohan_n.txt", "a") as f:
            f.write(f"\n{datetime.datetime.now()}\n")
            f.write(input())


    def lock_hammad_nutrition():
        with open("hammad_n.txt", "a") as f:
            f.write(f"\n{datetime.datetime.now()}\n")
            f.write(input())


    if person == "hy":
        if rl == "r":
            if en == "e":
                retrieve_harry_exercise()
            elif en == "n":
                retrieve_harry_nutrition()
        elif rl == "l":
            if en == "e":
                lock_harry_exercise()
            elif en == "n":
                lock_harry_nutrition()

    elif person == "rn":
        if rl == "r":
            if en == "e":
                retrieve_rohan_exercise()
            elif en == "n":
                retrieve_rohan_nutrition()
        elif rl == "l":
            if en == "e":
                lock_rohan_exercise()
            elif en == "n":
                lock_rohan_nutrition()

    elif person == "hd":
        if rl == "r":
            if en == "e":
                retrieve_hammad_exercise()
            elif en == "n":
                retrieve_hammad_nutrition()
        elif rl == "l":
            if en == "e":
                lock_hammad_exercise()
            elif en == "n":
                lock_hammad_nutrition()

    else:
        print("Wrong Input!")
