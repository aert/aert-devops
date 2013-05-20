base:
  '*':
    - base
  'desk_*':
    - desktop
  'cloud_*':
    - server.apache.server
    #- server.zabbix.agent
  'cloud_khin':
    - _machines.cloud_khin
  'desk_keurgui':
    - _machines.desk_keurgui
  'vagrant':
    - _machines.vagrant
