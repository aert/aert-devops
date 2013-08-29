from fabric.api import *


@task
def vagrant():
    "Use Vagrant for testing"
    env.user = 'vagrant'
    env.hosts = ['192.168.111.223']

    # retrieve the IdentityFile:
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1].replace('"', '')  # parse IdentityFile
