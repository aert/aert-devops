from fabric.api import *

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

