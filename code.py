import os
from utils.parsing import finder
from utils.out import bold_print,u_print,critical
import json
def read_analysis(obj,app_name):
    lib_dir='analysis'
    data=''
    data += '-' * 100 + '\n'
    if obj == 'res':
        with open('.tmp' + "/" + app_name + '.res.json') as json_file:
            json_data = json.load(json_file)
        for v in json_data:
            name = v
            msg="{0} - {1}\n".format(name,json_data[name])
            data+=msg
    if obj=='file':
        with open(lib_dir + "/" + app_name+'.lib.result') as json_file:
            data=json_file.read(1000200000)
    if obj=='system':
        with open('.tmp' + "/" + app_name+'.syscall') as json_file:
            data=json_file.read(1000200000)
    if obj == 'dy':
        with open('.tmp' + "/" + app_name + '.ltrace') as json_file:
            data = json_file.read(1000200000)

    if obj=='all':
        data += "*" * 10 + " 1.Resource" + "*" * 10+'\n'
        data+='-'*100+'\n'
        with open('.tmp' + "/" + app_name + '.res.json') as json_file:
            json_data = json.load(json_file)
        for v in json_data:
            name = v
            msg="{0} - {1}\n".format(name,json_data[name])
            data+=msg
        with open(lib_dir + "/" + app_name+'.lib.result') as json_file:
            #data+='Loaded File \n'
            data += "*" * 10 + "\n\n 2.Loaded File " + "*" * 10+'\n'
            data += '-' * 100 + '\n'
            data+=json_file.read(1000200000)
        with open('.tmp' + "/" + app_name+'.syscall') as json_file:
            data += "*" * 10 + "\n\n 3.System call " + "*" * 10+'\n'
            data += '-' * 100 + '\n'
            data+=json_file.read(1000200000)
        with open('.tmp' + "/" + app_name + '.ltrace') as json_file:
            #data += 'Dynamic Lib call \n'
            data += "*" * 10 + "\n\n 4.Dynamic Lib call " + "*" * 10 + '\n'
            data += '-' * 100 + '\n'
            data += json_file.read(1000200000)
    data += '-' * 100 + '\n'
    print(data)
def report():
    lib_dir='./analysis'
    file_list = os.listdir(lib_dir)
    app_list=[]
    for f_name in file_list:
        if finder(f_name, '.dy_trace.result'):
            app_name=(f_name.replace(".dy_trace.result",''))
            app_list.append(app_name)
    print(app_list)
    msg = '\n'+"*" * 10 + " 현재 분석된 앱 아래와 같습니다." + "*" * 10
    bold_print(msg)
    i=1
    for app in (app_list):
        msg='[{0}]\t{1}'.format(i,app)
        i+=1
        u_print(msg)
    try:
        select=int(input('분석 할 대상을 선택해주세요: '))
        msg='선택 된 앱 '+(app_list[int(select)-1])
        app_name=(app_list[int(select)-1])
        u_print(msg)
        msg="[0] All\t\t[1] Resource\t\t[2] Loaded File\t\t[3] System call\t\t[4] Dynamic Lib call"
        u_print(msg)
        select=int(input('분석 할 항목을 선택해주세요: '))

        if finder(select,0):
            read_analysis('all', app_name)
            pass
        elif finder(select,1): #resource
            read_analysis('res', app_name)
            pass
        elif finder(select,2): #load
            read_analysis('file',app_name)
            pass
        elif finder(select,3): #systemcall
            read_analysis('system', app_name)
