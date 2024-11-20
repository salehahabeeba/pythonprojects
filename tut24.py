#PATTERN PRINTING
print("pattern printing")
row=int(input("Enter how many rows you want to print\n"))
val=int(input("Enter 1 for true and 0 for false\n"))
bool_val=bool(val)
if val==1:
    for i in range(0,row+1):
        print("*"*i)
elif val==0:
    for i in range(row,0,-1):
        print("*"*i)
else:
    print("Please enter valid input")