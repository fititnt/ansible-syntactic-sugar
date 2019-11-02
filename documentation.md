# ap-application-load-balancer-extras documentation

## PHP

- Source repository: 
  - **ppa:ondrej/php**
  - <https://launchpad.net/~ondrej/+archive/ubuntu/php>
  - Why? Good default. Flexible. Allows running multiple PHP versions on same
    host.

### Important files

- _albextras_php_php74_
  - /etc/php/7.4/fpm/php.ini
  - /etc/php/7.4/fpm/php-fpm.conf
  - /etc/php/7.4/fpm/pool.d/
    - /etc/php/7.4/fpm/pool.d/www.conf
    - /etc/php/7.4/fpm/pool.d/YourPHP-FPM-WorkerHere.conf
- _albextras_php_php73_
  - /etc/php/7.3/fpm/php.ini
  - /etc/php/7.3/fpm/php-fpm.conf
  - /etc/php/7.3/fpm/pool.d/
    - /etc/php/7.3/fpm/pool.d/www.conf
    - /etc/php/7.3/fpm/pool.d/YourPHP-FPM-WorkerHere.conf
- _albextras_php_php72_
  - /etc/php/7.2/fpm/php.ini
  - /etc/php/7.2/fpm/php-fpm.conf
  - /etc/php/7.2/fpm/pool.d/
    - /etc/php/7.2/fpm/pool.d/www.conf
    - /etc/php/7.2/fpm/pool.d/YourPHP-FPM-WorkerHere.conf
- _albextras_php_php71_
  - /etc/php/7.1/fpm/php.ini
  - /etc/php/7.1/fpm/php-fpm.conf
  - /etc/php/7.1/fpm/pool.d/
    - /etc/php/7.1/fpm/pool.d/www.conf
    - /etc/php/7.1/fpm/pool.d/YourPHP-FPM-WorkerHere.conf
- _albextras_php_php56_
  - /etc/php/5.6/fpm/php.ini
  - /etc/php/5.6/fpm/php-fpm.conf
  - /etc/php/5.6/fpm/pool.d/
    - /etc/php/5.6/fpm/pool.d/www.conf
    - /etc/php/5.6/fpm/pool.d/YourPHP-FPM-WorkerHere.conf
