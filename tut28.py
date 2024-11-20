#TIME MODULE
import time
from time import localtime

# initial=time.time()
# i=0
# while(i<45):
#     print("this is saleha")
#     i+=1
# print("time taken by while loop",time.time()-initial,"seconds")
#
#
# initial2=time.time()
# k=0
# for k in range(45):
#     print("hey yooo!")
#     k+=1
# print("time taken by for loop",time.time()-initial2,"seconds")

#TIME.SLEEP() FUNCTION
time.sleep(2)
print("hello! hey there")

#LOCAL TIME
localtime=time.asctime(time.localtime(time.time()))
print(localtime)