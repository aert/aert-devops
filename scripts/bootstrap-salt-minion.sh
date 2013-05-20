
install_ubuntu_1204_deps() {
    sed -i -e 's#http://us.#http://fr.#g' /etc/apt/sources.list
    apt-get update
    apt-get -y install python-software-properties 
    add-apt-repository -y 'deb http://fr.archive.ubuntu.com/ubuntu/ precise universe' 
    add-apt-repository -y ppa:saltstack/salt
}

install_ubuntu_1204_post() {
    add-apt-repository -y --remove 'deb http://fr.archive.ubuntu.com/ubuntu/ precise universe'

}

install_ubuntu_stable() {
    apt-get -y install salt-minion

}

