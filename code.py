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
