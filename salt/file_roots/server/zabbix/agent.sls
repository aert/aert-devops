zabbix-agent:
  pkg:
    - installed

/etc/zabbix/zabbix_agentd.conf:
  file.managed:
    - source: salt://server/zabbix/files/zabbix_agentd.conf
    - template: jinja
    - require:
      - pkg: zabbix-agent
