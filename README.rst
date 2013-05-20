Fabric Tasks & Salt States
''''''''''''''''''''''''''

Introduction
************
 
This is the reporsitory of my Fabric and Salt configuration. 

Notable features :

* Debian packaging : update/list/upgrade
* Salt : minion setup
* EncFS : private dir mount/umount/backup
* Fabric custom decorators

Requirements 
************
 
This code has been run and tested on Python 2.7.

Master Deps 
===========
 
* Fabric
* FabTools for package requirement
* EncFS (optional)
 
Slaves Deps
===========
 
* Git
* Salt
* EtcKeeper
* Denyhosts

Installation
************
 
Install requirements::
 
  pip -e requirement.txt
 
Add Hosts:

.. code-block:: python

   # vim fabfile_local.py
   from fabric.api import *
   
   @task
   def my_host():
     "use my_host"
     env.user = '<USER>'
     env.hosts = ['<HOST>']
 
Start using::
 
  fab -l

Tests 
*****
 
Salt config can be run in dry-run mode.
More to come.

More Information 
****************
 
* GitHub : http://github.com/aert/aert-devops
* Documentation : https://github.com/aert/aert-devops/wiki
 
API Documentation
=================
 
Task list are available through Fabric::
 
  fab -l
 
TODO : Salt doc

Example Usage
*************
 
The following shows how to list available updates from remote server::
 
  fab h_remoteserver apt.update
  fab h_remoteserver apt.list

License 
*******
 
This project is licensed under the MIT license.

Support 
*******
 
* Issue Tracking : https://github.com/aert/aert-devops/issues
* Pull Request : https://github.com/aert/aert-devops/pulls

Those who wish to contribute directly to the project can contact me at devaert@gmail.com to talk about getting repository access granted.


