import os
from fabric.api import *
from fabric.colors import red, green, yellow, cyan, magenta

@task
def list():
    ''' List Available Updates '''
    print(yellow('All Updates :', bold=True))
    run('apt-get upgrade -s | grep -v ^Conf')

    print(yellow('Security Updates :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    run('apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list -s | grep -v ^Conf')

def update():
    ''' Update pkg list '''
    sudo('apt-get update')

def upgrade_security():
    ''' Upgrade only security updates '''
    print(yellow('Security Upgrade :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    sudo('apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list && apt-get update')

def distupgrade_security():
    ''' Dist-Upgrade only security updates '''
    print(yellow('Security Upgrade :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    sudo('apt-get dist-upgrade -oDir::Etc::Sourcelist=/tmp/security.list && apt-get update')

def distupgrade_all():
    ''' Dist-Upgrade'''
    sudo('apt-get dist-upgrade')

@task
def update_distupgrade_reboot_all():
    ''' Dist-Upgrade & Reboot'''
    sudo('apt-get update && apt-get dist-upgrade && reboot')

@task
def update_upgrade_all():
    ''' Upgrade'''
    sudo('apt-get update && apt-get upgrade')

def upgrade_all():
    ''' Upgrade all updates '''
    print(yellow('Upgrade All:', bold=True))
    sudo('apt-get upgrade && apt-get update')


