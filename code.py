import threading
import os
import time
import json


import os
from utils.parsing import finder
import json
from utils.out import u_print,analysis,bold_print
from core.dy_tracing import ltracing
def tracing_analysis():
    msg='\n\n'+"*"*10+" 3. System call에 대한 연계 분석 "+"*"*10
    bold_print(msg)
    lib_dir='analysis'
    file_list = os.listdir(lib_dir)
    node_pool=[]
    json_list=[]
    for f_name in file_list:
        if finder(f_name, '.syscall.result'):
            with open(lib_dir + "/" + f_name) as json_file:
                json_data = json.load(json_file)
                for node in json_data:
                    if not str(node) in node_pool:
