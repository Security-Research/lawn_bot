import os
from utils.out import info,critical



def createFolder(directory):
    try:
        if not os.path.exists(directory):

            os.mkdir(directory)
            info("Created directory",directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def removeFolder(directory):
    try:
        if os.path.exists(directory):
            os.rmdir(directory)
            critical("Remove directory", directory)
    except:
        print('Error: Removing directory. ' + directory)
def chmod():
    os.system('chmod 777 core/syscall')
def init():
    createFolder('.tmp')
    createFolder('analysis')
    chmod()

def reset():
    removeFolder('.tmp')
