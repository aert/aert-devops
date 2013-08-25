from fabric.api import *

@task
def master():
  "use host.com"
  env.user = 'username'
  env.hosts = ['host.com']

@task
def minion():
  "use host.com"
  env.user = 'username'
  env.hosts = ['host.com']