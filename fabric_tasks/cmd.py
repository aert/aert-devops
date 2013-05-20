from fabric.api import *
from fabric.contrib.files import comment, uncomment, sed
from fabtools import require, deb
from decorators import task_with_pkg_log


@task
def reboot():
    "Reboot"
    sudo('reboot')

@task
def run(cmd):
    "runs arbitrary command"
    run(cmd)

@task
def sudo(cmd):
    "runs arbitrary sudo command"
    sudo(cmd)

@task
def uname():
    "> uname -a"
    run('uname -a')
 
@task_with_pkg_log
def upgrade():
    "Updates & Upgrades"
    with settings(hide('stdout')):
        deb.update_index()
    deb.upgrade()

