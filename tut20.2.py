#TELL() AND SEEK() FUNCTIONS
#TELL WILL TELL WHERE IS OUR FILE POINTER f
f=open("saleha.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())

#SEEK IS USED TO CHOOSE FROM WHERE WE WANT TO READ THE FILE
print(f.seek(25))
print(f.readline())
f.close()
