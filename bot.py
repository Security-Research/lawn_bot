import os

def exe(com):
    os.system(com)
def commit(msg):
    msg='commit -m '+msg
    exe(msg)
def push():
    msg='git push'
    exe(msg)


