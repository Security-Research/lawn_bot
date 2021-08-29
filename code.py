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
    elif type=='WARN':
        logger.info('{0}'.format(msg))

def get_user_info(user):
    try:
        user_system = getpwnam(user)
    except KeyError:
        raise CgroupsException("User %s doesn't exists" % user)
    else:
        uid = user_system.pw_uid
        gid = user_system.pw_gid
    return uid, gid


def create_cgroups(user, script=True):
    #logger.info('Creating cgroups sub-directories for  %s' % user)

    try:
        hierarchies = os.listdir(BASE_CGROUPS)
    except OSError as e:
        if e.errno == 2:
            msg = "cgroups filesystem is not mounted on{0}".format(BASE_CGROUPS)  # cgroups 제어 검증 에러
            raise CgroupsException(msg)
        else:
            raise OSError(e)
    #logger.info('Hierarchies availables: {0}'.format(hierarchies))
    for hierarchy in hierarchies:
        user_cgroup = os.path.join(BASE_CGROUPS, hierarchy, user) #경로와 제어 권한 정보를 유저명과 합침
        #print(user_cgroup)
        if not os.path.exists(user_cgroup):
            try:
                os.mkdir(user_cgroup) #폴더생성
            except:
