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

    def set_cpu_limit(self, limit=None):
        if 'cpu' in self.cgroups:
            value = self._format_cpu_value(limit)
            cpu_shares_file = self._get_file('cpu', 'cpu.shares')
            with open(cpu_shares_file, 'w+') as f:
                f.write('%s\n' % value)
        else:
            exit(-1)

    #memory
    def get_memory_info(self,app_name,info):
        usage = 0
        with open('/sys/fs/cgroup/memory/' + str(app_name) + '/memory.'+info, 'r+') as f:
            data = f.readline()
            usage = int(data)
        return usage

    def get_memory_stat(self,app_name,info):
        f=open('/sys/fs/cgroup/memory/' + str(app_name) + '/memory.stat', 'r+')
        lines=f.readlines()
        for line in lines:
            line=line.strip('\n')
            data=line.split(' ')
            if info==data[0] :
                return int(data[1])


    # CPU
    def _format_cpu_value(self, limit=None):
        if limit is None:
            value = CPU_DEFAULT
        else:
            limit = limit / 100
            value = int(round(CPU_DEFAULT * limit))
        return value

    def set_memory_limit(self, limit=None, unit='megabytes'):
        if 'memory' in self.cgroups:
            value = self._format_memory_value(unit, limit)
            memory_limit_file = self._get_file(
                'memory', 'memory.limit_in_bytes')

            with open(memory_limit_file, 'w+') as f:
                f.write('%s\n' % value)
        else:
            exit(-1)

    def _format_memory_value(self, unit, limit=None):
        units = ('b', 'kb', 'mb', 'gb')
        if unit not in units:
            exit(-1)
        if limit is None:
            value = MEMORY_DEFAULT
        else:
            try:
                limit = int(limit)
            except ValueError:
                exit(-1)
            else:
                if unit == 'b':
                    value = limit
                elif unit == 'kb':
                    value = limit * 1024
                elif unit == 'mb':
