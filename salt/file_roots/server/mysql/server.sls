mysql-server:
  pkg:
    - installed
    - require:
      - pkg: python-mysqldb

python-mysqldb:
  pkg:
    - installed

mysql-server-preseed:
  file.managed:
    - name: {{ pillar.preseeds_dir }}/mysql-server.preseed
    - source: salt://server/mysql/files/mysql-server.preseed
    - template: jinja
    - makedirs: True
  cmd:
    - run
    - name: debconf-set-selections {{ pillar.preseeds_dir }}/mysql-server.preseed && date > {{ pillar.checks }}/mysql-server-preseed
    - unless: test -f {{ pillar.checks }}/mysql-server-preseed
    - order: 100
    - require: 
      - file: {{ pillar.preseeds_dir }}/mysql-server.preseed
    - require_in:
      - pkg: mysql-server
