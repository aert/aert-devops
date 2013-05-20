from functools import wraps
from fabric.api import *
from fabric.tasks import WrappedCallableTask
from fabtools import require
from datetime import datetime

log_dir = "/srv/devop/log/pkg_changes"

def task_with_pkg_log(task_function):

  @wraps(task_function)
  def wrapper(*args, **kwargs):
    task_name = task_function.__name__

    # Before
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    before_file_path = "{}/{}-{}-before.txt".format(log_dir, timestamp, task_name)
    cmd = "zcat -f /var/log/dpkg.log* | grep \"\\ install\\ \" > %s" % before_file_path
  
    require.directory(log_dir, owner='root', use_sudo=True)
    sudo(cmd)

    result = task_function(*args, **kwargs)

    # After
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    after_file_path = "{}/{}-{}-after.txt".format(log_dir, timestamp, task_name)
    cmd = "zcat -f /var/log/dpkg.log* | grep \"\\ install\\ \" > %s" % after_file_path
    sudo(cmd)
    
    return result
    
  return WrappedCallableTask(wrapper)
