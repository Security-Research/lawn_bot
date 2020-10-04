import os
import subprocess
support_interpreter='/usr/bin/python3'
import threading
import time
from utils.out import info,warning,critical
from core.lib_analysis import get_lib
from core.tracing import tracing
from core.dy_tracing import ltracing
kill_time=10

def poll(target,pg):
    #warning("Analysis",""+str(target))
    while pg.poll() == None:
        out = pg.stdout.readline()
        time.sleep(kill_time)
        #critical("kill",pg.pid)
        #pg.kill()
        break


def run_app(target,sec):
    kill_time=sec
    cmd=support_interpreter+' testing_app/'+str(target)
    # os.popen()#예정 #get pid
    pg = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT,
                          universal_newlines=True, shell=True)
    t = threading.Thread(target=(poll), args=(target,pg,))
