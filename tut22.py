#GLOBAL AND LOCAL VARIABLES AND THE USE OF global KEYWORD
# l=33 #global variable
# def function(n):
#
#     l=5 #local variable
#     print(n,"i have printed")
#     print(l)
#
# function("hey!")
# print(l)

# def function(n):
#     global l #global keyword is used to change the value of global variable
#     l = 99
#     print(n, "i have printed")
#     print(l)


# function("hey!")
# print(l)

#GLOBAL VARIABLES FOR NESTED FUNCTIONS
def saleha():
    x=34
    def rohan():
        global x
        x=55 #it will become the value of global variable  because it is not  defined. 34
        #is not the value of global variable because global variable should be outside the
        #functions
    print("before",x)
    rohan()
    print("after",x)

saleha()
print(x)