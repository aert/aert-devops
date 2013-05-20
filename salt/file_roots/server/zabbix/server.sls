include:
  - server.zabbix.agent
  - server.zabbix.server_db
  - server.apache.server

# Zabbix server unconfigured
# --------------------------

zabbix-server-mysql:
  pkg:
    - installed

/etc/zabbix/zabbix_server.conf:
  file.managed:
    - source: salt://server/zabbix/files/zabbix_server.conf
    - template: jinja
    - require:
      - pkg: zabbix-server-mysql

# Zabbix server configuration
# ---------------------------

zabbix-db-setup:
  cmd:
    - run
    - name: mysql -u zabbix --password={{ pillar.zabbix_server_dbpassword }} zabbix < /usr/share/zabbix-server/mysql.sql && mysql -u zabbix --password={{ pillar.zabbix_server_dbpassword }} zabbix < /usr/share/zabbix-server/data.sql && date > {{ pillar.checks }}/zabbix-server-data
    - unless: test -f {{ pillar.checks }}/zabbix-server-data
    - require:
      - pkg: python-mysqldb
      - pkg: zabbix-server-mysql
      - mysql_database.present: zabbix
      - mysql_grants.present: zabbix-grants

# Zabbix Front-End
# ----------------

zabbix-frontend-php:
  pkg:
    - installed
    - require:
      - pkg: zabbix-server-mysql
      - pkg: pkgs-www

zabbix-frontend-preseed:
  file.managed:
    - name: {{ pillar.preseeds_dir }}/zabbix-frontend.preseed
    - source: salt://server/zabbix/files/zabbix-frontend.preseed
    - template: jinja
  cmd:
    - run
    - name: debconf-set-selections {{ pillar.preseeds_dir }}/zabbix-frontend.preseed && date > {{ pillar.checks }}/zabbix-frontend-preseed
    - unless: test -f {{ pillar.checks }}/zabbix-frontend-preseed
    - require: 
      - file: {{ pillar.preseeds_dir }}/zabbix-frontend.preseed
    - require_in:
      - pkg: zabbix-frontend-preseed
  
