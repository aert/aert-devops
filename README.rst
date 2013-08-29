Fabric Tasks & Ansible Configuration
''''''''''''''''''''''''''''''''''''

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

Installation
************
 
#. Install requirements:: 

     pip install -e requirement.txt

#. Add Hosts
#. Launch ansible playbook

Tests 
*****
 
#. Start Vagrant::

     vagrant up
     vagrant ssh

#. Upgrade Debian (mandatory)::

     sudo -i && apt-get update && apt-get dist-upgrade

#. Quit Vagrant & install your ssh-key to root::

     ssh-copy-id root@192.168.111.223

#. Launch ansible playbook

More Information 
****************
 
* GitHub : http://github.com/aert/aert-devops
* Documentation : https://github.com/aert/aert-devops/wiki
 
License 
*******
 
This project is licensed under the MIT license.

Support 
*******
 
* Issue Tracking : https://github.com/aert/aert-devops/issues
* Pull Request : https://github.com/aert/aert-devops/pulls

Those who wish to contribute directly to the project can contact me at devaert@gmail.com to talk about getting repository access granted.



