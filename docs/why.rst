.. include:: Includes.txt

#################################
Why a2s may be useful for you
#################################

.. warning::

  a2s still an apha release. This page is not complete.


.. contents:: Table of Contents of APIs

.. raw:: html

  <hr />


****************************************
Who are likely to NOT need `a2s`
****************************************

Who don't need to deploy changes on servers
============================================

.. warning::

  This pages assumes that you or already work or want to learn how to automate
  IT and already have some experience on how to do without automation. A great
  example if you are someone who would be able implement alone (ok use help of
  search engines) tutorials like `How To Install WordPress with LAMP on Ubuntu 18.04 <https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lamp-on-ubuntu-18-04>`_
  but now want to abstract/automate this.

  If you already use software that someone else configure the operational
  system for you, it's very likely that **at this moment** `a2s` may not be
  useful.

Who don't need (and do not want learn) how to automate IT
==========================================================

Ansible can be used even for who does not work as sysadmin, DevOps or
IT infrastructure in general and, compared to alternatives, may actually save
your time even if you don't work full time on a position that benefits from
automation.

> TODO: comment more about (fititnt, 2020-01-21 02:53 BRT)

*************************
I'm new to IT automation
*************************

> TODO: comment more about (fititnt, 2020-01-21 01:26 BRT)

Ansible is a friendly IT automation tool
==========================================

  *"It turned out our group of 15 or so people spent about six months trying to
  automate OpenStack with Puppet, and I spent a lot of time banging my head into
  a desk. (Later, once AnsibleWorks was founded, one of our Solutions Architects
  built content to automate OpenStack, similar in scale, in a single week, by
  himself!)"*

   --Michael DeHaan - In `The origins of Ansible <https://www.ansible.com/blog/2013/12/08/the-origins-of-ansible>`_



*************************
I'm new to Ansible
*************************

.. tip::

  Even if you are very skilled, know some basic automation ("bash history",
  docker, etc or even Chef/Puppet/Saltstack) **but are in a hurry to implement
  an infrastructure in production** (think like have just a 2~5 days), in
  special if this infrastructure it not simple (could be replaced later if you
  on a code refactoring), dont use `a2s`.

  Ok, you can use, but `a2s` starting point. `a2s` can make some implementations
  simpler, in ones related to filesystem and users/groups manangement.

  But in a very short time to learn both Ansible and implement something complex
  like (here just as example) clusters of FreeIPA, GlusterFS & Galera Cluster
  (MariaDB/MySQL) you may find ready to use Ansible Roles *near plug and play*.
  Check out https://galaxy.ansible.com/.


`a2s` as jack of all trades Ansible Role
==========================================


`a2s` have great examples of common tasks
==========================================

*******************************
I'm a experienced Ansible user
*******************************

`a2s` only when you have no better option
==========================================

`a2s` ...
==========================================

***********************************
I'm a Ansible extensions developer
***********************************


a2s is dedicated to public domain
==================================

In short: while atribution is welcome from ansible users (most because it may
help to find documentation) you as open source contributor is free to take take
parts of a2s source code without mention.


`a2s` ...
==========================================