#if else and elif
var1=5
var2=56
print("enter your number ")
var3=int(input())
#put colon after every if, elif and else statements. elif is used to
#come out of the ifelse ladder otherwise it will check all the statements
#even if it is true in the first statement
if var3>var2:
    print("the given number is greator")
elif var3==var2:
    print("the given number is equal ")
else:
    print("the given number is lesser")

#use of in and not in keyword
list1=[5,4,3,2]
#do not use double quotes if using in keyword to return a boolean value
print(5 in list1)
if 5 in list1:
    print("the given number is in list")
print(15 not in list1)
if 15 not in list1:
    print("the number is not in the list")
