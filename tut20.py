#ACCESSING THE FILES IO BASICS
# r"=open file for reading(default)
# "w"=open file for writing
# "x"= create file if not exist
# "a"= add more content to a file
# "b"= binary mode
# "+"= read and write mode
# 't'= text mode.(default)
 
# f=open("saleha.txt","r")
# content=f.read()
# print(content)
# content=f.readline()
# print(content)
#      (or)
#print(f.readline())
#
# content=f.readline()
# print(content)
#
# content=f.readline()
# print(content)
#to read in binary form rb
# f=open("saleha.txt","rb")
# content=f.readlines()
# print(content)
# f.close() # it is imp to close a file

# to read in text mode rt
# f=open("saleha.txt","rt")
# content=f.readlines()
# print(content)

# we can give agruments in read functions
f=open("saleha.txt","rt")
# content=f.read(3)
# content=f.read(30)
content=f.read(3445)

print(content)
f.close()