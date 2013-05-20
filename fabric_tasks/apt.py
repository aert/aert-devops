import os
from fabric.api import *
from fabric.colors import red, green, yellow, cyan, magenta

@task
def apt_list():
    print(yellow('All Updates :', bold=True))
    run('apt-get upgrade -s | grep -v ^Conf')

    print(yellow('Security Updates :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    run('apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list -s | grep -v ^Conf')

@task
def apt_update():
    sudo('apt-get update')

@task
def apt_upgrade_security():
    print(yellow('Security Upgrade :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    sudo('apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list && apt-get update')

@task
def apt_distupgrade_security():
    print(yellow('Security Upgrade :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    sudo('apt-get dist-upgrade -oDir::Etc::Sourcelist=/tmp/security.list && apt-get update')

@task
def apt_upgrade_all():
    print(yellow('Upgrade All:', bold=True))
    sudo('apt-get upgrade && apt-get update')

@task
def reboot():
    print(yellow('Reboot !', bold=True))
    sudo('reboot')


