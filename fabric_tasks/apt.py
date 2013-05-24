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

@task
def update():
    ''' Update pkg list '''
    sudo('apt-get update')

@task
def upgrade_security():
    ''' Upgrade only security updates '''
    print(yellow('Security Upgrade :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    sudo('apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list && apt-get update')

@task
def distupgrade_security():
    ''' Dist-Upgrade only security updates '''
    print(yellow('Security Upgrade :', bold=True))
    run('grep security /etc/apt/sources.list > /tmp/security.list')
    sudo('apt-get dist-upgrade -oDir::Etc::Sourcelist=/tmp/security.list && apt-get update')

@task
def upgrade_all():
    ''' Upgrade all updates '''
    print(yellow('Upgrade All:', bold=True))
    sudo('apt-get upgrade && apt-get update')


