from ctypes import *
import time
while(True):

    #load the shared object file
    adder = CDLL('./testing_app/adder.so')

    #Find sum of integers
    res_int = adder.add_int(4,5)
    msg="Sum of 4 and 5 = " + str(res_int)
    print(msg)

    #Find sum of floats
