from os.path import join, dirname
from fabric.api import *
from fabric.contrib.files import comment, uncomment, sed
from fabtools import require
from decorators import task_with_pkg_log

@task_with_pkg_log
def base():
  "Installs & configures Git / EtcKeeper / DenyHosts"
  
  with settings(hide('stdout')):
    # Require 
    require.deb.packages([
        'etckeeper',
        'git',
        'denyhosts',
    ])

    # git
    sudo('git config --global user.name "DevOp"')
    sudo('git config --global user.email admin@{}'.format(env.host))

    # etckeeper
    conf_file = '/etc/etckeeper/etckeeper.conf'
    comment(conf_file, 'VCS="bzr"', use_sudo=True, backup='') 
    uncomment(conf_file, 'VCS="git"', use_sudo=True, backup='') 

    sudo('etckeeper init')
    sudo('etckeeper commit "Initial commit."')

    # denyhosts
    conf_file = '/etc/denyhosts.conf'
    comment(conf_file, 'BLOCK_SERVICE\s*=\s*sshd', use_sudo=True, backup='') 
    uncomment(conf_file, 'BLOCK_SERVICE\s*=\s*ALL', use_sudo=True, backup='') 
    sed(conf_file, 'DENY_THRESHOLD_INVALID\s*=\s*5'
        , 'DENY_THRESHOLD_INVALID = 3', use_sudo=True, backup='')
    sed(conf_file, 'DENY_THRESHOLD_VALID\s*=\s*10'
        , 'DENY_THRESHOLD_VALID = 3', use_sudo=True, backup='')
    sed(conf_file, 'DENY_THRESHOLD_ROOT\s*=\s*1'
        , 'DENY_THRESHOLD_ROOT = 3', use_sudo=True, backup='')

    sudo('etckeeper commit "Auto-config DenyHosts.conf."')

@task_with_pkg_log
def base_salt_minion():
  "Installs Salt Minion"

  with settings(hide('stdout')):
    require.deb.packages([
			'python-software-properties',
			'debconf-utils',
		])

  require.deb.ppa('ppa:saltstack/salt')

  with settings(hide('stdout')):
    #deb.update_index()
    require.deb.package('salt-minion')

@task_with_pkg_log
def dev_python():
  "Installs pip and  fabtools"

  with settings(hide('stdout')):
    # Require
    require.deb.packages([
        'python-pip',
    ])

    require.python.package('fabtools', use_sudo=True)

@task
def vim_config(user=''):
    "Set up vimrc and install bundles."
    if not user:
        user = env.user

    require.deb.package('vim')
    require.deb.package('exuberant-ctags')
    run('rm -rf ~/.vim')
    run('mkdir -p ~/.vim/{bundle,colors}')

    files_dir = join(dirname(__file__), 'files', 'vim')
    fvimrc = join(files_dir, '_vimrc')
    fsolarized = join(files_dir, 'colors', 'solarized.vim')
    fsmyck = join(files_dir, 'colors', 'smyck.vim')

    require.file('~/.vimrc', source=fvimrc)
    require.file('~/.vim/colors/solarized.vim', source=fsolarized)
    require.file('~/.vim/colors/smyck.vim', source=fsmyck)

    run('git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle')
    run('vim +BundleInstall +qall')

