from fabric.api import *
from fabric_tasks.decorators import task_with_pkg_log
from fabric_tasks import hosts as h
from fabric_tasks import setup, secure, apt
from fabric_tasks import ssh, cmd, salt

