# -*- mode: ruby; -*-
require 'etc'

Vagrant.configure("2") do |config|
  config.vm.define :web do |web|
    # Puppetlabs Debian 7.0rc1 x86_64, VBox 4.2.10, No Puppet or Chef
    web.vm.box = "wheezy-rc1"
    web.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/debian-70rc1-x64-vbox4210-nocm.box"

    # Network
    web.vm.network :private_network, ip: "192.168.111.223"
    web.vm.hostname = "vagrant.aert-devops.org"
    web.vm.network :forwarded_port, guest: 80, host: 8080, auto_correct: true
    web.vm.network :forwarded_port, guest: 5432, host: 5432

    # Customize the box
    web.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--memory", 512]
    end
  end
end

