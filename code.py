import json,time
import os

import subprocess

import os
import json,time

lib_dir = ".tmp"
#file_list = os.listdir(lib_dir)

import os
import json,time
from utils.out import warning,u_print,critical,analysis,bold_print
from utils.parsing import finder

def similarity():
    msg = '\n\n'+"*" * 10 + " 2. LoadFile 에 대한 연계 분석 " + "*" * 10
    bold_print(msg)

    lib_dir = ".tmp"
    file_list = os.listdir(lib_dir)
    node_pool=[]
