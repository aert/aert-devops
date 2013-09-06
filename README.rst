Fabric Tasks & Ansible Playbooks
''''''''''''''''''''''''''''''''

Introduction
************
 
Notable features :

* Debian packaging : update/list/upgrade
* Salt : minion setup
* EncFS : private dir mount/umount/backup
* Fabric custom decorators
* Ansible playbooks : Denyhost, Etckeeper, Nginx, ...

Requirements 
************
 
Run and tested on Python 2.7.

Installation
************
 
#. Install requirements:: 

     $ pip install -e requirement.txt

Usage
*****
 
Ansible
=======

#. Add Hosts
#. Launch ansible playbook

Exemples
--------

* Install desktop::

    $ cd playbooks
    $ sudo ansible-playbook -i hosts/localhost -c local site_desktop.yml -v
 
Fabric
======

Commands list::

  $ fab -l

Usage::

  $ fab -H <host1,host2> <command>

Tests 
*****
 
#. Start Vagrant::

     $ vagrant up

#. Setup with Fabric::

     $ fab h.vagrant setup.vagrant 

#. Launch ansible playbook or Fabric task

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

Those who wish to contribute directly to the project can contact me at dev.aert@gmail.com to talk about getting repository access granted.



