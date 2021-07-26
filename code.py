
import time

for i in range(0,10000000):
    time.sleep(0.2)
    print(i)
    f=open("/tmp/testest",'w')
    f.write('2313')
