.. include:: Includes.txt

##################
Philosophy
##################

.. note::

  `a2s` still a pre-release. But a TL;DR: to explain the idea behind is *"`a2s`
  be to Ansible what jQuery is to JavaScript"*. So it means:

  - `a2s` still YAML and still Ansible.

    - It should not require Python knowledge for one averange Pull Request with
      a new feature.
    - Ideally should be easy to reuse parts of this code by others.

  - `a2s` **"most common data structure"** is a List **"of something"** to be
    executed in order

    - If **"this something"** is an abstraction to an Ansible Module

      - The name should be plural form
      - The same way Ansible modules may implement parameter aliases (e.g. `file_module
        have dest and name as aliases for path <https://docs.ansible.com/ansible/latest/modules/file_module.html>`_)
        , `a2s` may implement entire API aliases (e.g a2s_directories, a2s_links
        are alises to file_module).
      - We point to the official documentation instead of repeating all options,
        and (if any) document what a2s add to the underlining API.
      - if uses more than one API, both documentation and execution should
        mention.

    - If **"this something"** is a very customized implementation, it should
      explain all options. And very likely warn the user if is an API that could
      be changed on a next major version

  - `a2s` should be *"be otimized for humans"* and simpler usages.

    - It does not means that more than simpler usages cannot be otimized, but
      they may require read more documentation, in special ones related on how
      to run just part of the `a2s` per play run.
    - What may be more complex than simple to medium implementation is out of
      scope and we recommend users to use dedicated Ansible roles.

  - `a2s` should be namespaced to avoid conflict with Ansible underling modules,
    with other Ansible Roles and maybe even with more than one version of itself
    (or someone elses fork) installed.

    - *How* this could be done, we're open to ideas.
    - `a2s` should respect `SemVer <https://semver.org/>`_ and may have major
      versions more often than most averange software.


..
  (This is a source code comment)
  - `a2s` can be less strict than Ansible modules if this makes more easy to use
  - `a2s` license is Public Domain.


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
