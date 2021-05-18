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
