import subprocess, getpass, os
from pwd import getpwnam
from utils.exception import CgroupsException,BASE_CGROUPS
from core.user import create_cgroups, get_user_info
import logging

CONTROL = [
    'cpu',
    'memory',
]

logger = logging.getLogger(__name__)
CPU_DEFAULT = 1024
MEMORY_DEFAULT = 1


class Cgroup(object):
    def __init__(self, cgroups_name, target='all', user='syscore'):
        self.cgroups_name = cgroups_name
        self.user = user
        self.target = ''
        self.u_cgroups = {}
        self.target = [c for c in target if c in CONTROL]
        system = os.listdir(BASE_CGROUPS)

        for h in self.target:  #
            if h not in system:
                exit(-1)
            user_cgroup = os.path.join(BASE_CGROUPS, h, self.user)
