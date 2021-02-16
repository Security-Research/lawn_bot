
import os
def get_app_list():
    path_dir='./testing_app'
    file_list = os.listdir(path_dir)
    python_list=[]
    for file_name in file_list:
        if finder(file_name,'.py') and not finder(file_name,'__init__'):
