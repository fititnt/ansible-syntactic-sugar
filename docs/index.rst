.. Ansible Syntactic Sugar ("a2s") documentation master file, created by
   sphinx-quickstart on Thu Jan 16 03:38:44 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ansible Syntactic Sugar ("a2s") documentation
===========================================================

.. image:: https://img.shields.io/ansible/role/45694
    :alt: Ansible Role
    :target: https://galaxy.ansible.com/fititnt/syntactic_sugar
.. image:: https://img.shields.io/ansible/quality/45694
    :alt: Ansible Quality Score
    :target: https://galaxy.ansible.com/fititnt/syntactic_sugar
.. image:: https://travis-ci.com/fititnt/ansible-syntactic-sugar.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.com/fititnt/ansible-syntactic-sugar

"`a2s`" is a non-official `Syntactic Sugar <https://en.wikipedia.org/wiki/Syntactic_sugar>`_
for `Ansible <https://www.ansible.com/>`_, which without extensions already is
an *"Simple, agentless IT automation that anyone can use"*.

If you are new to Ansible, we recommend read our :ref:`installation-guide`.
TL;DR:


.. code-block:: bash

  # "a2s is installable as an Ansible role and is distributed over Ansible Galaxy
  ansible-galaxy install fititnt.syntactic_sugar


.. important::

  By design a2s explicitly choose not respect some Ansible best practices
  related to large scale projects and may implement features that would never
  be accepted on the Ansible standard modules because would be redundant with
  more lines of code. We may explicitly warn you in some cases, and even help
  you on how to migrate from a2s to more enterprise approach.


..
  Note to self: here style guides
  https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   installation
   philosophy
   api
   playbooks
   alternatives
   basic
   admonition


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`