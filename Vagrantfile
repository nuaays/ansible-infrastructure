# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "debian-8.2"
  config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_debian-8.2_chef-provisionerless.box"
  # SSH hardcoded for Ansible, remember to change in inventory also
  config.ssh.insert_key = false
  config.vm.network :forwarded_port, guest: 22, host: 4001, id: 'ssh', auto_correct: false
  config.vm.network :forwarded_port, guest: 8080, host: 8080, id: 'nginx', auto_correct: false
  #config.vm.synced_folder ".", "/vagrant", disabled: true
end
