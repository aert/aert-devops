from fabric.api import *
from fabric_tasks.decorators import task_with_pkg_log
from fabric_tasks import hosts
from fabric_tasks import setup, secure, apt
from fabric_tasks import ssh, cmd, salt
import fabfile_local as h

@task
def uname():
  "> uname -a"
  run('uname -a')
  
