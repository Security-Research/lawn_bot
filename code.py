from ctypes import *
import time
while(True):

    #load the shared object file
    adder = CDLL('./testing_app/adder.so')

    #Find sum of integers
