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
