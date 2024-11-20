#USE OF JOIN FUNCTION
lis=["Saleha","Habeeba","Gulafshan","Tahera","Saniya","Afra"]
#to add and after every element in the list , originally we use for loop
for item in lis:
     print(item, "and",end=" ")
print("other friends")

#but it is too much work instead we can use join
a=" and ".join(lis)
print(a,"and other friends")