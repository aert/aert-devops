pkg-base:
  pkg.installed:
    - pkgs:
      - vim
      - git
      - htop
      - byobu
      - screen
      - debconf-utils
      - update-notifier-common

{{ pillar.checks }}:
  file.directory:
    - user: root
    - group: root
    - mode: 700
    - makedirs: True
    - order: 0

{{ pillar.devop_dir }}:
  file.directory:
    - user: root
    - group: root
    - mode: 700
    - makedirs: True
    - order: 0

{{ pillar.preseeds_dir }}:
  file.directory:
    - user: root
    - group: root
    - mode: 700
    - makedirs: True
    - order: 0

