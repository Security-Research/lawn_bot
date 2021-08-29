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
