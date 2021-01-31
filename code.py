
import subprocess,threading,time

import os,signal
from utils.parsing import finder
import json
from utils.out import bold_print,u_print,analysis


def dy_tracing_analysis():
    msg="\n\n"+"*"*10+" 4. Dynamic Lib 에 대한 연계 분석 "+"*"*10
    bold_print(msg)
