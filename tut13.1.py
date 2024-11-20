#quiz
#to check if a list has number in it if yes then check if it is greater than 6
from unicodedata import numeric

list1=[12]
for items in list1:
    if items.is_integer():
        print("yes")
    else:
        print("no")
if items>6:
    print("yes")
else:
    print("no")


#as per video
items=[int,float,22, 4 ,66 ,8,44,4,77,9]
for item in items:
    #typecasting because the items in the list is numeric and we are checking the numeric
    #condition otherwise it will throw an error
    if str(item).isnumeric() and item>6:
        print(item)



