#HEALTH MANAGEMENT SYSTEM- EXERCISE 5

def mangmnt():
    print("select 1 if you want to log and select 2 if you want to retrieve")
    inp=input()
    print("select the person name. Select 1 for harry\n2 for rohan\n3 for hammad")
    inp2=input()
    print("select 1 to write diet and 2 to write exercise")
    inp3=input()
    if inp==1:
        if inp2==1:
            if inp3==1:
             f=open("harry.txt","a")
             diet=input("write the diet")
             f.write=str(getdate())

