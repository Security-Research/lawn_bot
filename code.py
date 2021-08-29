
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def u_print(obj):
    msg="{0}".format(obj)
    print(bcolors.OKGREEN + msg + bcolors.ENDC)

def bold_print(obj):
    msg="{0}".format(obj)
    print(bcolors.BOLD + msg + bcolors.ENDC)

def info(obj,sub):
    msg="[Info] {0} : {1}".format(obj,sub)
    print(bcolors.OKBLUE + msg + bcolors.ENDC)

