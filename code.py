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
    json_list=[]
    for f_name in file_list:
        if finder(f_name, '.lib.json'):
            with open(lib_dir + "/" + f_name) as json_file:
                json_data = json.load(json_file)
            for node in json_data:
                if not str(node) in node_pool:
                    node_pool.append(node)
            json_list.append(f_name)
    #msg = '동적 라이브러리 분석 결과\n'+'-'*100+'\n'
    app_list=[]
    for app in json_list:
        app_list.append(app.replace(".lib.json",''))
    msg="{0} 이 Load File 갯수는 총 {1} 개입니다.".format(app_list,len(node_pool)) #최종수정 다시해보기 100%라고 나옴 b.py이상한앤데..
    u_print(msg)
    msg= '-'*100
    u_print(msg)
    #u_print('Load File:' + str(node_pool.))

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
            msg="{0} 과 {1} 앱의 Load file 유사도는 {2} % 입니다.".format(base_file.replace(".lib.json",''),target_file.replace(".lib.json",''),round(percent,2))
            analysis(msg)

    u_print('-' * 100 + '\n')

def lib_analysis():
    lib_dir=".tmp"
    file_list = os.listdir(lib_dir)
    #print(file_list)
    msg = "분석 된 App의 갯수는 " + str(len(file_list)) + "개 입니다."
    #print(msg)
    for f_name in file_list:
        #print(f_name)
        #print(finder(f_name,'.json'))
        if finder(f_name,'.json'):
            strFormat = '%-20s%-10s%-40s\n'
            strOut = strFormat % ('Timestamp', 'Node', 'Name')
            strOut += "-" * 100 + "\n"

            with open(lib_dir + "/" + f_name) as json_file:
                json_data = json.load(json_file)
            for node in json_data:
                strOut += strFormat % (str(int(time.time())), node, json_data[node])
            with open("analysis/" + str(f_name.replace(".lib.json", '')) + ".lib.result", "w", encoding='UTF-8') as f:
                #print(strOut) //출력용
                f.write(strOut)


def get_lib(app_name,pid):
    time.sleep(1)
    new_pid=int(pid)+2#bug ! +
    data=''
    data=subprocess.check_output("lsof -w -p " + str(new_pid),shell=True)
    #os.system("lsof -w -p " + str(new_pid))
    data=str(data).split('\\n')
