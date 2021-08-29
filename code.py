
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
                json_data = json.load(json_file)
                for node in json_data:
                    if not str(node) in node_pool:
                        node_pool.append(node)
                json_list.append(f_name)
        # msg = '동적 라이브러리 분석 결과\n'+'-'*100+'\n'
    app_list=[]
    for app in json_list:
        app_list.append(app.replace(".dy_trace.result",''))
    msg = "{0} 이 호출한 Dynamic Lib  갯수는 총 {1} 개입니다.".format(app_list, len(node_pool))  # 최종수정 다시해보기 100%라고 나옴 b.py이상한앤데..
    u_print(msg)
    msg = '-' * 100
    u_print(msg)
    u_print('dy call list:'+str(node_pool))
    for target in range(0,len(json_list)-1):
        for a_target in range(target+1, len(json_list)):
            base_file=(json_list[target])
            target_file=(json_list[a_target])
            with open(lib_dir + "/" + base_file) as json_file:
                base_data = json.load(json_file)
            with open(lib_dir + "/" + target_file) as json_file:
                target_data = json.load(json_file)
            count=1
            target_data_list = []
            if (len(base_data)) < (len(target_data)):
                for t in target_data:
                    target_data_list.append(t)
                for base in base_data:
                    if base in (target_data_list):
                        count += 1
                percent=count/len(target_data)*100
            else:
                for t in base_data:
                    target_data_list.append(t)
                for base in target_data:
                    if base in (target_data_list):
                        count += 1

                percent=count/len(base_data)*100
            msg="{0} 과 {1} 앱의 Dynamic Lib 유사도는 {2} % 입니다.".format(base_file.replace(".dy_trace.result",''),target_file.replace(".dy_trace.result",''),round(percent,2))
            analysis(msg)

    u_print('-' * 100 + '\n')
    pass
