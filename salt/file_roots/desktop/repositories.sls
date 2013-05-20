gvfs-ppa:
  cmd.run:
    - name: "add-apt-repository ppa:langdalepl/gvfs-mtp && apt-get update"
    - unless: "[ -f /etc/apt/sources.list.d/langdalepl-gvfs-mtp-{{ grains['oscodename'] }}.list ]"

webupd8-ppa:
  cmd:
    - run
    - name: "add-apt-repository ppa:nilarimogard/webupd8 && apt-get update"
    - unless: "[ -f /etc/apt/sources.list.d/nilarimogard-webupd8-{{ grains['oscodename'] }}.list ]"
    - require_in:
      - pkg: webupd8-pkgs

webupd8-pkgs:
  pkg.installed:
    - pkgs:
      - minitube
      - musique
      - audacious
      
