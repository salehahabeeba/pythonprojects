#MAP
numbers=["2","3","5","6","8","9"]

# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
#
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])

#instead of for loop we can use Map to typecast it into integers
# numbers=list(map(int,numbers))
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])

#we can also use it with defined functions

# num=[2,4,6,8,9]
#
# def sq(a):
#     return a*a
# square=list(map(sq, num))
# print(square)

#************OR**************


# square=list(map(lambda x : x*x, num))
# print(square)


# #FILTER
#
# number=[2,4,6,8,9]
#
# def greatorr(num):
#     return num>5
# print(greatorr(9))
#from the above we cant print the list given

# gr_than=list(filter(greatorr,number))
# print(gr_than)


#REDUCE
from functools import reduce

numbers=[2,4,6,8,9]

num=
for i in numbers:
    num=num+i
print(num)
#to summate instead of for loop we can use reduce

red=reduce(lambda x,y:x+y,numbers)
print(red)