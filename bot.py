import os
import datetime,time
from glob import glob

def add(target):
    os.system('git add '+target)

def exe(com):
    os.system(com)

def commit(msg):
    msg='git commit -m '+msg
    exe(msg)
def push():
    msg='git push --force'
    exe(msg)

def work():
    target_file=get_dir('/tmp/pycharm_project_280/target_dir/app_thermometer')
    d_len=len(target_file)
    rand_value=random.randrange(0,d_len)
    target=target_file[rand_value]
    print(target)
    f=open(target,'r')
    data=f.readlines()
    d_len=len(data)
    rand_value=random.randrange(0,d_len)
    code=''
    for i in range(0,rand_value):
        #print(data[i])
        code+=data[i]
    #print(code)
    f.close()
    f=open('code.py','w')
    f.write(code)
    f.close()


def nd_commit(date):
    msg='git commit --amend --no-edit --date \"'+str(date)+'"'
    exe(msg)

def get_dir(path):
    file_list = glob(str(path)+"/**", recursive=True)
    py_list = []
    for target in file_list:
        if target.find(".py") >= 0 and target.find("init") < 0:
            py_list.append(target)
    return py_list

import random


def start(before_day):
    day=before_day
    get_time=int(time.time())
    now=get_time-(24*60*60*day)
    now_date=datetime.datetime.fromtimestamp(now)
    for i in range(0,day):
        now = now+(24*60*60)
        now_date = datetime.datetime.fromtimestamp(now)
        work()
        add('code.py')
        commit('test')
        nd_commit(now_date)
        push()
start(365)