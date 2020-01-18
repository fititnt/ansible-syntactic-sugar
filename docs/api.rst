.. include:: Includes.txt

##################
a2s APIs
##################

.. error::

  This documentation is incomplete and with obvious markup issues. May take
  some time to finish the migration from GitHub page README.md to ReadTheDocs
  and also fix some issues with Sphinx (like how to improve the usability of
  the navigation bar) (fititnt, 2020-01-18 03:27 BRT)

********************
Overview of a2s APIs
********************

a2s, released as Ansible role, when not restricted with special variables, will
convert the instructions of your Ansible inventory defined on variables started
with `a2s_`.

With some exceptions, most of the time, you can expect that:

- **Naming**

  - `a2s_APINAMEs` that end with letter `s` accept a list of values, all the
    others may accept a single value, that may be a string, boolean or a
    dictionaly (e.g. an "object" like `{ key: 'valye', key2: 'value2 }`)

- **Standard APIs reuse same Ansible documentation**

  - If you know that the `APINAME` on an `a2s_APINAME(s)` is have and exact
    Ansible core module, this a2s API will implement the same parameters from the
    official API
  - a2s by default will ignore instead of fail if a param that does not exist on
    the underlinging Ansible module was defined. Please pay attention to wrong
    paramenters names.

- **Idempotent by default**

  - Using a2s will have at least the the same idempotency of the Ansible underlining
    modules (which already is very good)
  - *"An operation is idempotent if the result of performing it once is exactly
    the same as the result of performing it repeatedly without any intervening
    actions.* -- `Ansible Glossary for idempotency <https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-idempotency>`_

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
- **Examples**


.. code-block:: yaml

  a2s_directories:
    - path: /var/www/my-app
      owner: app
      group: www-data
      mode: '0755'
    - path: /var/www/my-old-app-folder-to-delete
      state: absent

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
  modules. Missing values will be ommited.


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


***********
Devel APIs
***********

No documented Devel APIs at this moment.