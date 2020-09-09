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
            self.u_cgroups[h] = user_cgroup
        create_cgroups(cgroups_name, script=False)
        self.cgroups = {}

        for h, user_cgroup in self.u_cgroups.items():
            cgroup = os.path.join(user_cgroup, self.cgroups_name)
            if not os.path.exists(cgroup):
                os.mkdir(cgroup)
            self.cgroups[h] = cgroup

    def _get_file(self, hierarchy, file_name):
        return os.path.join(self.cgroups[hierarchy], file_name)
