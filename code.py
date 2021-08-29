from utils.parsing import get_app_list
from core.run import run_app
from utils.out import info,warning,critical
from core.cgroups import Cgroup
from utils.out import warning,u_print,critical,analysis,bold_print
import os
from utils.parsing import finder
import time
import json


def resource_usage(app_name,pid):

    cg=Cgroup(app_name)
    cg.add_process(app_name,pid)
    usage_list={'cache':[], 'rss':[],'usage':[], 'failcnt':[],'pgpgin':[], 'pgpgout':[]}

    cnt =0
    for i in range(10):
        usage_list['cache'].append(cg.get_memory_stat(app_name,'cache')) #byte
        usage_list['rss'].append(cg.get_memory_stat(app_name,'rss')) #byte
        usage_list['usage'].append(cg.get_memory_info(app_name,'usage_in_bytes')) #byte
        usage_list['failcnt'].append(cg.get_memory_info(app_name, 'usage_in_bytes')) #cnt
        usage_list['pgpgin'].append(cg.get_memory_stat(app_name,'pgpgin')) #cnt
        usage_list['pgpgout'].append(cg.get_memory_stat(app_name,'pgpgout')) #cnt
        cnt += 1
        time.sleep(1)
    usage_list['max_usage']=cg.get_memory_info(app_name,'max_usage_in_bytes')

    #print(usage_list)

    with open(".tmp/" + app_name + ".res.json", "w", encoding='UTF-8') as json_file:
        json.dump(usage_list, json_file)

    #json
    res_dic = {}
    for key in usage_list.keys():
        if key=='cache' or key=='rss' or key=='usage':
            tmp=sum(usage_list[key])//cnt//1024
        elif key=='max_usage':
            tmp=usage_list[key]//1024
        else:
            tmp=sum(usage_list[key])//cnt
        res_dic[key] = tmp
    #print(res_dic)

    with open("analysis/" + app_name + ".res.result", "w", encoding='UTF-8') as json_file:
        json.dump(res_dic, json_file)

def res_analysis():
    msg = '\n' + "*" * 10 + " 1. Resource 에 대한 분석 " + "*" * 10
    bold_print(msg)

    lib_dir = "analysis/"
    file_list = os.listdir(lib_dir)

    for f_name in file_list:
        #usage_pool = {}
        if finder(f_name, '.res.result'):
            app=f_name.replace('.res.result','')
