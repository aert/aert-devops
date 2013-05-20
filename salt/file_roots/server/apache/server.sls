
pkgs-www:
  pkg.installed:
    - pkgs:
      - apache2
      - php5
      - php5-mysql
      - php5-gd
      - php5-curl
      - php5-mcrypt
      - curl
      - libcurl3

# -- PHP CONFIG
/etc/php5/apache2/php.ini:
  file.managed:
    - source: salt://server/apache/files/php.ini
    - require:
      - pkg: pkgs-www

