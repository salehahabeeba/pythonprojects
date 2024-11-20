#RECURSIVE AND ITERATIVE METHOD
#RECURSIVE=IF ELSE , ITERATIVE=FOR LOOPS
#finding the factorial of number with iterative and recursive method
# def fun_iterative(n):
#     fac = 1
#     for i in range(n):
#
#         fac= fac * (i+1)
#     return fac
# number=int(input("enter your number"))
# print(fun_iterative(number))
#
# def fun_recursive(n):
#     if n==1:
#      return 1
#     else:
#         return n * fun_recursive(n-1)
# number2=int(input("enter your number"))
# print(fun_recursive(number2))

#finding fibonacci of numbers
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number3=int(input("enter your number"))
print(fibonacci(number3))