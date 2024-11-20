#FILE WRITING w
# f=open("saleha2.txt","w")
# f.write("hey saleha! How are you?")
# f.close()

#FILE APPENDING a
# f=open("saleha2.txt","a")
# f.write("\nI am fine")
# f.close()

#READ AND WRITE r+
f=open("saleha2.txt","r+")
print(f.read())
f.write("\nthank you!")
f.close()