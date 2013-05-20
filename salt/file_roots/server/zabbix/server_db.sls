include:
  - server.mysql.server


# Db creation & grants
# --------------------

zabbix-db:
  mysql_database:
    - present
    - name: zabbix
  mysql_user:
    - present
    - name: zabbix
    - host: localhost
    - password: {{ pillar.zabbix_server_dbpassword }}
  require:
    - pkg: python-mysqldb

zabbix-grants:
  mysql_grants:
    - present
    - grant: all privileges
    - database: zabbix.*
    - user: zabbix
    - require:
        - mysql_user.present: zabbix

