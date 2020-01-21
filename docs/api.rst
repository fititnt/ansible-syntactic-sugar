.. include:: Includes.txt

##################
a2s APIs
##################

.. warning::

  a2s still an apha release. This page is not complete.


.. contents:: Table of Contents of APIs

.. raw:: html

  <hr />

.. _ref-standard-apis:

*************
Standard APIs
*************



`a2s_copies`
============

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/copy/main.yml>

`a2s_crons`
===========

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/cron/main.yml>

`a2s_directories`
=================

- **Short Description**: *Manange directories*
- **Ansible Modules**:
  - `file_module <https://docs.ansible.com/ansible/latest/modules/file_module.html>`_
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  module. `state` value will default `directory`. Other missing values will be
  ommited.


.. code-block:: yaml
  :caption: a2s_directories_example.yml
  :name: a2s_directories_example
  :linenos:

  # Create directories. a2s_directories_default allows create custom variables
  # like (var1 in item.var1) or reuse one variable (like owner in item.owner)
  a2s_directories_default:
    path: "/var/www/html/{{ item.var1 }}/"
    owner: "{{ item.var1 }}"
    group: "www-data"

  a2s_directories:
    - path: /var/www/html
      recurse: yes
      owner: root
      group: root
      var1: null
    - var1: "app"
    - var1: "site-a"
    - var1: "site-b"
    - var1: "cdn-site-a"
    - var1: "cdn-site-b"


`a2s_etchosts`
==============

- **Short Description**: *List of strings to be added on /etc/hosts file. The
  current implementation will not will not replace older values.*
- **Ansible Modules**:
  - None. This is a custom implementation.
- **Type of values**: List of strings.

.. code-block:: yaml

  a2s_etchosts:
    - "127.0.0.1  site-a.local"
    - "198.51.100.0  example.org example.com"

Note: `a2s_etchosts` is very likely to be improved before a2s stable release.

`a2s_fetches`
=================

- **Short Description**: *Fetch files from remote machines and storing them
  locally in a file tree, organized by hostname.*
- **Ansible Modules**:
  `fetch_module <https://docs.ansible.com/ansible/latest/modules/fetch_module.html>`_
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  module. Missing values will be ommited.
- **Special defaults override**: `a2s_fetches_default`

.. code-block:: yaml
  :caption: a2s_fetches_example.yml
  :name: a2s_fetches_example
  :linenos:

  a2s_fetches_default:
    dest: /backup/
  a2s_fetches:
    - src: /etc/ssh/ssh_host_rsa_key # File required on a new node to keep the fingerprint
    - src: /home/root/.ssh/id_rsa
    - src: /home/root/.ssh/id_rsa.pub

  ## For each host, files will be downloaded prefixed with inventory name
  ## Paths will be respected. E.g for node "host.example.com" you get:
  # /backup/host.example.com/etc/ssh/ssh_host_rsa_key
  # /backup/host.example.com/home/root/.ssh/id_rsa
  # /backup/host.example.com/home/root/.ssh/id_rsa.pub


`a2s_files`
=================

- **Short Description**: *Manange files. Exlusive feature: Allows create file
  content from string*
- **Ansible Modules**:
  `file_module <https://docs.ansible.com/ansible/latest/modules/file_module.html>`_
  and `win_file_module <https://docs.ansible.com/ansible/latest/modules/win_file_module.html>`_
  or, if `a2s_files[n]content` is defined,
  `copy_module <https://docs.ansible.com/ansible/latest/modules/copy_module.html>`_
  and  `win_copy_module <https://docs.ansible.com/ansible/latest/modules/copy_file_module.html>`_
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  module. Other missing values will be ommited.
- **Special defaults override**: `a2s_files_default`

You can consider `a2s_files` with the same parameters of Ansible file_module &
win_file_module. The only exception to this rule is if you define a non-empty
value to `a2s_files[n]content`: in this case `a2s_files` will use Ansible
copy_module & win_copy_module.


.. code-block:: yaml
  :caption: a2s_files_example.yml
  :name: a2s_files_example
  :linenos:

  a2s_files_default:
    group: "www-data"

  a2s_files:
    - path: "/var/www/html/app/index.html"
      content: "Hello world, app!"
      owner: "app"

`a2s_groups`
============

- **Short Description**: *group – Add or remove groups / win_group – Add and
  remove local groups*
- **Ansible Modules**:
  - [group](https://docs.ansible.com/ansible/latest/modules/group_module.html)
  - [win_group](https://docs.ansible.com/ansible/latest/modules/win_group_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  modules. Missing values will be ommited.
- **Examples**

.. code-block:: yaml

  a2s_groups:
    - name: "www-data"
    - name: "haproxy"
    - name: "user-to-remove"
      state: "absent"

`a2s_hostname`
==============

- **Short Description**: *hostname – Manage hostname, enforcing
  [RFC822](https://www.w3.org/Protocols/rfc822/ format to avoid fail*
- **Ansible Modules**:
  - [hostname](https://docs.ansible.com/ansible/latest/modules/hostname_module.html)
- **Type of values**: Dictionary. Same values of Ansible module hostname.

To add to /etc/hosts, check [`a2s_etchosts`](#a2s_etchosts).


`a2s_mysql_dbs`
===============

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/mysql/main.yml>


`a2s_mysql_users`
=================

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/mysql/main.yml>

.. _a2s_templates:

`a2s_templates`
===============

.. note::

  Undocumented at this moment. Check source code at
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/template/main.yml>


`a2s_users`
===========

- **Short Description**: *user – Manage user accounts / win_user – Manages local
  Windows user accounts*
- **Ansible Modules**:
  - [user](https://docs.ansible.com/ansible/latest/modules/user_module.html)
  - [win_user](https://docs.ansible.com/ansible/latest/modules/win_user_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  modules. Missing values will try `a2s_users_default`, then will be ommited.
- **Special defaults override**: `a2s_users_default`

.. code-block:: yaml
  :caption: a2s_users_example.yml
  :name: a2s_users_example
  :linenos:

  a2s_users_default:
    create_home: no
    groups: ["www-data"]

  a2s_users:
    - name: "app"
    - name: "site-a"
    - name: "site-b"
    - name: "cdn-site-a"
      groups: ["cdns", "www-data"]
    - name: "cdn-site-b"
      groups: ["cdns", "www-data"]
    - name: "php-demo"
    - name: "fititnt"
      create_home: yes
      authorized_keys:
        - key: https://github.com/fititnt.keys


`a2s_users[n]authorized_keys`
=============================

- **Short Description**: *authorized_key – Adds or removes an SSH authorized key*
- **Ansible Modules**:
  - [authorized_key](https://docs.ansible.com/ansible/latest/modules/authorized_key_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  modules. Missing required `user` (`a2s_users[n]authorized_keys[m]user`) will
  default to `name` (`a2s_users[n]name`). Other missing values will be ommited

***********
Extra APIs
***********

`a2s_install_adminer`
=====================


`a2s_rclone`
=================

***********
Devel APIs
***********

`a2s_devel_nginx`
=================

Install NGinx with `a2s_devel_nginx: true`. Used for testing.

.. note::

  This is an internal feature and may not be documented because is not planned
  to be used for end users. The source code is at:
  <https://github.com/fititnt/ansible-syntactic-sugar/blob/master/tasks/devel-nginx/main.yml>


Example:

.. code-block:: yaml

  - hosts: all
    remote_user: root
    vars:

      a2s_devel_nginx: true

    roles:
      - { role: fititnt.syntactic_sugar }

***********
Installers
***********

`a2s_install_adminer`
=====================

- **Short Description**: *Install [adminer](https://www.adminer.org/), "Database
  management in a single PHP file"*
- **Default**: `undefined`
- **Type of value**: Dictionary (name, state)
- **Examples of values**: `{{ a2s__adminer }}`

Variable `{{ a2s__adminer }}` are a *syntactic sugar* for the default parameters


`a2s_install_composer`
======================

- **Short Description**: *Install [composer](https://getcomposer.org/) required
  by [Ansible composer](https://docs.ansible.com/ansible/latest/modules/composer_module.html)
  by default on global path*
- **Ansible Modules**:
  - None. Custom implementation.
- **Type of values**: Boolean, Dictionary

All these examples have the same effect (install on global scope)

.. code-block:: yaml

  a2s_install_composer: true


.. code-block:: yaml

  a2s_install_composer: "{{ a2s__composer }}"


.. code-block:: yaml

  a2s_install_composer:
    - path: /usr/local/bin
      user: root
      force: false # true force reinstall
      version: '' # use custom version to install
      php: 'php' # php binary to use. If is not 'php' customize here


`a2s_install_composers`
=======================

- **Short Description**: *Install [composer](https://getcomposer.org/) required
  by [Ansible composer](https://docs.ansible.com/ansible/latest/modules/composer_module.html)
  for more than one user*
- **Ansible Modules**:
  - None
- **Type of values**: List of Dictionaries

.. code-block:: yaml

  a2s_install_composers:
    - "{{ a2s__composer }}" # Global, as root
    - path: '/home/user1/bin'
      user: user1
    - path: '/home/user2/bin'
      user: user2


`a2s_install_php`
=================
- Default: `undefined`
- Type of value: List of Strings; List of Objects (name, state)
- Examples of values: `{{ a2s__php74 }}`,  `{{ a2s__php73 }}`,
  `{{ a2s__php72 }}`, `['php-fpm', 'php-common']` <sup>(assumes state: present)</sup>
  `[{name: 'php-fpm', state: 'present'}, name: 'php-mssql', state: 'absent']`

> Install a list of PHP packages on the system

Variables `a2s__php74`, `a2s__php73`, `a2s__php72`... are a *syntactic sugar*
to install common packages to run Wordpress, Joomla, Drupal and laravel.

In Ansible is possible append arrays values with `+` (objects you use
`| combine()`), e.g `a2s_php_install: "{{ a2s__php74 + ['php7.4-dev', 'php7.4-ldap'] }}"`


*******************
Groups of a2s APIs
*******************

a2s-devel
===========

a2s-extra
===========

database
===========

files
===========

notifications
=============

packaging-languages
===================

packaging-os
===================

system
===================

*********************
Control a2s workflow
*********************


`a2s_except_apis`
======================

`a2s_except_apis_groups`
========================

`a2s_only_apis`
================

`a2s_only_apis_groups`
======================
