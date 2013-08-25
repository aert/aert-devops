from fabric.api import *

@task
def master():
  "use {{cookiecutter.master_host}}"
  env.user = '{{cookiecutter.master_user}}'
  env.hosts = ['{{cookiecutter.master_host}}']

@task
def minion():
  "use {{cookiecutter.minion_host}}"
  env.user = '{{cookiecutter.minion_user}}'
  env.hosts = ['{{cookiecutter.minion_host}}']
