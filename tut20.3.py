#ACCESSING FILES WITH "WITH BLOCK"
with open("saleha.txt") as f:
    print(f.readlines())
#we need not to close the file in the with block, it will close
#automatically

f=open("saleha.txt")
print(f.read())
f.close()