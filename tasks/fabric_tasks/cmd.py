from fabric.api import *

@task
def reboot():
    "Reboot"
    sudo('reboot')

@task
def myrun(cmd):
    "runs arbitrary command"
    run(cmd)

@task
def mysudo(cmd):
    "runs arbitrary sudo command"
    sudo(cmd)

@task
def uname():
    "> uname -a"
    run('uname -a')
