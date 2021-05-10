import argparse

from core.report import report
from core.manager import reset
from core.execute import execute


def isint(a):

    if int(a):
        return 1
    else:
        return 0

def get_arguments():
    return [
    ("--start", "Start a Thermometer deamon"),
    ("--reporter", "Get a reporter"),
    ("--reset","Reset a Thermometer deamon")
    ]
