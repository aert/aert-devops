import os
from fabric.api import *
from fabric.contrib.files import append, comment, uncomment, sed
from fabtools import require
from decorators import task_with_pkg_log
from fabric.contrib.project import rsync_project


@task_with_pkg_log
def setup_master():
    ''' Install and configure salt master at specified host '''
    require.deb.packages(['salt-master'])
    require.directory('/srv/salt', owner='aert', use_sudo=True)

    master_conf = "/etc/salt/master"
    append(master_conf, "file_roots:", use_sudo=True)
    append(master_conf, "  base:", use_sudo=True)
    append(master_conf, "    - /srv/salt", use_sudo=True)

    require.service.restarted('salt-master')


@task
def setup_minion_keurgui():
    ''' Configure a salt minion bound to @keurgui '''
    minion_conf = '/etc/salt/minion'
    sed(minion_conf, '#master: salt', 'master: aert.zapto.org',
        use_sudo=True, backup='')

    salt_id = prompt('Salt ID: ', validate=r'\w+')
    sed(minion_conf, '#id:', 'id: {0}'.format(salt_id),
        use_sudo=True, backup='')
    
    require.service.restarted('salt-minion')


@task
def push_file_roots():
    ''' Push salt file_root to master '''
    dir_file_roots = 'salt/file_roots/'
    dir_pillar_roots = 'salt/pillar_roots/'
    
    rsync_project(local_dir=dir_file_roots, remote_dir="/srv/salt/",
                  delete=True)

    rsync_project(local_dir=dir_pillar_roots, remote_dir="/srv/pillar/",
                  delete=True)

@task
def highstate(filter_="*"):
    ''' salt '<filter>' state.highstate '''

    sudo("salt '{0}' state.highstate".format(filter_))


@task
def push_and_highstate(filter_="*"):
    ''' salt '*' test.ping '''
    push_file_roots()
    highstate(filter_)
