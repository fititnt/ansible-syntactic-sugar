.. include:: Includes.txt

.. Ansible Syntactic Sugar ("a2s") documentation master file, created by
   sphinx-quickstart on Thu Jan 16 03:38:44 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

################################################
Ansible Syntactic Sugar ("`a2s`") documentation
################################################

.. image:: https://img.shields.io/ansible/role/45694
    :alt: Ansible Role
    :target: https://galaxy.ansible.com/fititnt/syntactic_sugar
.. image:: https://img.shields.io/ansible/quality/45694
    :alt: Ansible Quality Score
    :target: https://galaxy.ansible.com/fititnt/syntactic_sugar
.. image:: https://travis-ci.com/fititnt/ansible-syntactic-sugar.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.com/fititnt/ansible-syntactic-sugar

.. |image-maturity-technology-preview| image:: https://img.shields.io/badge/Maturity-technology--preview-informational
    :alt: Maturity: Technology Preview

|image-maturity-technology-preview| `a2s` is a non-official `Syntactic Sugar <https://en.wikipedia.org/wiki/Syntactic_sugar>`_
for `Ansible <https://www.ansible.com/>`_, which without extensions already is
an *"Simple, agentless IT automation that anyone can use"*.

*************
Installation
*************

If you are new to Ansible, we recommend read our :doc:`installation`. TL;DR:

.. code-block:: bash

  # "a2s is installable as an Ansible role and is distributed over Ansible Galaxy
  ansible-galaxy install fititnt.syntactic_sugar

*************
Quickstart
*************

And then, look at our :doc:`api` and :doc:`playbooks`. TL;DR:

.. code-block:: yaml
  :caption: playbook-basic.yml
  :name: playbook
  :linenos:

  # TODO: improve this quickstart example (fititnt, 2020-01-17 01:11 BRT)
  # $ ansible-playbook -i myserver.com, playbook-basic.yml

  - hosts: all
    remote_user: root
    vars:

      # Create operational system group (if already does not exist)
      a2s_groups:
        - name: 'www-data'

      # Create operational system users
      a2s_users:
        - name: app
          groups: ['www-data']

      # Create/delete directories
      a2s_directories:
        - path: /var/www/my-app
          owner: app
          group: www-data
        - path: /var/www/my-old-app-folder-to-delete
          state: absent

      # Install PHP with packages that allow run popular softwares like
      # Drupal, Joomla, Wordpress & Laravel
      a2s_install_php:
        - php7.4-fpm
        - php7.4-common
        - php7.4-mbstring
        - php7.4-mysql
        - php7.4-bcmath
        - php7.4-curl
        - php7.4-gd
        - php7.4-xml
        - php-imagick

      # Uncomment next variable only for Windows hosts.
      # a2s_iswindows: true
    roles:
      - { role: fititnt.syntactic_sugar }

But playbook-basic.yml, while may help you to undestand a2s (or even Ansible)
may be less powerfull than a2s offer. One tricky that a2s uses to avoid be too
optionated on defaults is simply create an equivalent to most ``a2s_APINAME`` as
``a2s_APINAME_defaults`` and suggest you to keep near your  `a2s_APINAME`
definitions:

.. code-block:: yaml
  :caption: playbook.yml
  :name: playbook
  :linenos:

  # TODO: improve this quickstart example (fititnt, 2020-01-17 01:11 BRT)
  # $ ansible-playbook -i myserver.com, playbook.yml

  - hosts: all
    remote_user: root
    vars:

      # Create operational system group (if already does not exist)
      a2s_groups:
        - name: 'www-data'

      # Create operational system users (with some defaults)
      a2s_users_defaults:
        groups: ['www-data']

      a2s_users:
        - name: app
        - name: drupal-site
        - name: joomla-site
        - name: laravel-site
        - name: wordpress-site
        - name: fititnt
          authorized_keys:
            - key: https://github.com/fititnt.keys

      # Create folders (with some defaults)
      # "{{ item.myspecialvar }}" is an example of valid default
      a2s_directories_defauts:
        path: "/var/www/{{ item.myspecialvar }}"
        owner: "{{ item.myspecialvar }}"
        group: www-data
        mode: '0755'
        state: present

      a2s_directories:
        - path: /var/www/my-app
          owner: app
        - path: /var/www/my-old-app-folder-to-delete
          state: absent
        - myspecialvar: "drupal-site"
        - myspecialvar: "joomla-site"
        - myspecialvar: "laravel-site"
        - myspecialvar: "wordpress-site"


      # Install PHP with packages that allow run popular softwares like
      # Drupal, Joomla, Wordpress & Laravel
      a2s_install_php: "{{ a2s__php74 }}"

      # Uncomment next variable only for Windows hosts.
      # a2s_iswindows: true
    roles:
      - { role: fititnt.syntactic_sugar }

.. important::

  a2s by design have to explicitly choose not respect some specific Ansible best
  practices related to large scale projects to allow implement more even more
  concise Infrastructure As Code. An notable anti-pattern is a2s allowing you
  bootstrap some features that would be better be done to additional Asible Role
  with :ref:`a2s_templates`.

  a2s by design may implement implement features that would never
  be accepted on the Ansible standard modules because would be redundant with
  more lines of code or would be better implemented by external extensions.

  We may explicitly warn you in some cases, and even help you on how to migrate
  from a2s to more enterprise approach. We by default namespace our rules using
  `a2s_` to make it easier.

.. admonition:: Dedicated to the public domain

  The a2s codebase is dedicated to public
  domain to estimulate your creativity and allow sub parts of a2s be reused
  freely.



..
  Note to self: here style guides
  https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   why
   installation
   philosophy
   api
   constant
   playbooks
   todo
   alternatives


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
