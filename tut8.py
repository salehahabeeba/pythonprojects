#string functions
mystr=("saleha is a good girl")
print(mystr)
#string lenght
print(len(mystr))
print(mystr[4])
#string slicing
print(mystr[0:6])
print(mystr[:])
print(mystr[0:])
print(mystr[:21])
#slicing and skipping
print(mystr[0:7:2])
print(mystr[::2])
print(mystr[::])
print(mystr[::3378])
#working with negative indices
print(mystr[-1:])
print(mystr[:-1])
#when using negative for skipping it will reverse the string
print(mystr[::-1])
print(mystr[::-2])
#strings  functions
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("girl"))
print(mystr.count("a"))
print(mystr.capitalize())
print(mystr.find("good"))
print(mystr.upper())
print(mystr.replace("saleha","habeeba"))


