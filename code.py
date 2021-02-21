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
