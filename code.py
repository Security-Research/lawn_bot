#! /usr/python3
# -*- coding:utf-8 -*-

import os,sys
import logging
from pwd import getpwnam

from utils.exception import CgroupsException,BASE_CGROUPS

logger = logging.getLogger(__name__)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logstream = logging.StreamHandler()
logstream.setFormatter(formatter)
logger.addHandler(logstream)
logger.setLevel(logging.INFO)
def log(type,msg):
    if type=='INFO':
        logger.info('{0}'.format(msg))
