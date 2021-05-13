from utils.parsing import get_app_list
from core.run import run_app
from utils.out import info,warning,critical,analysis
from core.lib_analysis import lib_analysis,similarity
from core.tracing import tracing
#commands()
import os,subprocess,signal
import sys
import json,time
from core.tracing import tracing_analysis
from core.dy_tracing import dy_tracing_analysis

from core.manager import init
from core.resource import resource_usage, res_analysis
import threading
from tqdm import trange

def prog(times):
    analysis('Estimated time :'+str(times*0.9) +'s')
    progress(times)
    #tv = threading.Thread(target=(progress), args=(times,))
    #tv.start()

def progress(times):
    for i in trange(times*90):
        time.sleep(0.01)


def execute(sec):
    init()
    app_list = (get_app_list())
    # testing_app 에 있는 파일을 .py를 짤라서 cgroups에 등록해줘야함 중복될 수 있으니.. 잘 정리 #
    for app_name in app_list:
        pid = run_app(app_name,sec)
        time.sleep(0.5)
        info("Executed","Appname - {0} ({1}) ".format(app_name,pid))
        t = threading.Thread(target=resource_usage,args=(app_name,pid,))
        t.start()
        #resource_usage(app_name,pid)

    prog(30)

    res_analysis()
    #time.sleep(30)
    lib_analysis()
    time.sleep(1)
    similarity()
    time.sleep(1)
