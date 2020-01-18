.. include:: Includes.txt

##################
a2s philosophy
##################

.. note::

  This page is a draft. Will change later.


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


*******************
Antipatterns of a2s
*******************

.. note::

  Undocumented at this moment.
