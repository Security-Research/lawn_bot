
import subprocess,threading,time

import os,signal
from utils.parsing import finder
import json
from utils.out import bold_print,u_print,analysis


def dy_tracing_analysis():
    msg="\n\n"+"*"*10+" 4. Dynamic Lib 에 대한 연계 분석 "+"*"*10
    bold_print(msg)
    lib_dir='analysis'
    file_list = os.listdir(lib_dir)
    node_pool=[]
    json_list=[]
    for f_name in file_list:
        if finder(f_name, '.dy_trace.result'):
            with open(lib_dir + "/" + f_name) as json_file:
