#exercise- FAULTY CALCULATOR
#design a calculator which will solve all the problems except
#45*3=555, 56+9=77, 56/6=4
a=int(input("enter the first number\n"))
b=int(input("enter the second number\n"))
print("choose the operator from= +,-,*,/")
c=input()
if c=='*':
   if a==45 and b==3:
    print(555)
   else:
    print(a*b)
elif c=='+':
    if a==56 and b==9:
        print(77)
    else:
        print(a+b)
elif c == '/':
    if a==56 and b==6:
            print(4)
    else:
        print(a/b)
elif c=='-':
  print(a-b)
else:
    print("enter valid operator")

