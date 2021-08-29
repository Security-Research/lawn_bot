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
