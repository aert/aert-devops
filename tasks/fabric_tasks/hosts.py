from fabric.api import *

@task
def vagrant():
  "Use Vagrant for testing"
  env.user = 'vagrant'
  env.hosts = ['192.168.33.10']
  
  # retrieve the IdentityFile:
  result = local('vagrant ssh-config | grep IdentityFile', capture=True)
  env.key_filename = result.split()[1] # parse IdentityFile