.. _installation-guide:

Installation guides
=================================

Python
-------

.. note::

  Maybe you already have Python installed on your system. And even if you don't
  have maybe by installing Ansible your package mananger will install python for
  you.


.. tip::

  If you system already does not have python installed, but you could choose
  between python 2 or python 3, **please select python 3**. Ansible actually can
  work on python 2, but it's older.

  Since you already is installing python 3, if some guide guide explain how to
  install pip3, its may be a good idea do it. Neither Ansible or a2s require
  pip eventually you may want to install pip and acidentaly install pip for
  python 2 instead of `pip3` because most guides may teach you do with the older
  one.

You can check how to install python via the `official Python documentation <https://docs.python.org/3/using/index.html>`_.
But maybe is easier to just look on your prefered search engine for "how to
install python 3 on *name of my operational system*",

Ansible
-------

.. note::

  TODO: we should document some basic explanation on how to install Ansible

Check the `complete guide on how to install Ansible <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>`_.

Ansible Galaxy
-------

.. note::

  TODO: we should document some basic explanation on how to install Ansible Galaxy

Ansible Syntactic Sugar ("a2s")
-------

`a2s` is installable as one Ansible role. You can install the lastest version
with the command:

.. code-block:: bash

  ansible-galaxy install fititnt.syntactic_sugar

Note: Ansible roles does not automatic update without you explicitly force this.
This behavior may actually not be a bad default behavior.