import os
import socket
from fabric.api import *
from fabric.contrib.files import append, comment, uncomment, sed
from fabtools import require
from decorators import task_with_pkg_log
from fabric.contrib.project import rsync_project


PRIVATE_DIR_ENCRYPTED = '~/Private/.Encrypted'
PRIVATE_DIR_DECRYPTED = '~/Private/Decrypted'


@task_with_pkg_log
def private_setup():
    ''' Install and configure EncFS for ~/Private/* '''
    require.deb.packages(['encfs'])
    run('mkdir -p {}'.format(PRIVATE_DIR_ENCRYPTED))
    run('mkdir -p {}'.format(PRIVATE_DIR_DECRYPTED))

    run('encfs {} {}'.format(PRIVATE_DIR_ENCRYPTED, PRIVATE_DIR_DECRYPTED))
    private_umount()


@task
def private_mount():
    ''' Mounts ~/Private/Decrypted'''
    run('encfs {} {}'.format(PRIVATE_DIR_ENCRYPTED, PRIVATE_DIR_DECRYPTED))


@task
def private_umount():
    ''' Unmounts ~/Private/Encrypted'''
    run('fusermount -u {}'.format(PRIVATE_DIR_DECRYPTED))


@task
def push_my_private():
    ''' Push locally encrypted to host '''
 
    current_host = socket.gethostname()
    if current_host != 'k73ta':
        raise Exception

    remote = '/srv/backups/private/aert'

    rsync_project(local_dir=PRIVATE_DIR_ENCRYPTED,
                  remote_dir=remote, delete=True)

