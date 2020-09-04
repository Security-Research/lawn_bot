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


def add_arguments():
    parser=argparse.ArgumentParser(description="Thermometer by syscore")
    for argument in get_arguments():
        parser.add_argument(argument[0], help=argument[1], action="store_true")
    parser.add_argument("-s", action='store', dest='sec', help='running second',default=10)

    return parser.parse_args()

def commands():
    args = add_arguments()
    sec=args.sec
    if args.start:
        if not isint(sec):
