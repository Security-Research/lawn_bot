import os
from utils.out import info,critical



def createFolder(directory):
    try:
        if not os.path.exists(directory):
