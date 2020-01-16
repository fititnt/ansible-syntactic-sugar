Example Playbooks
=================================


Minimal Playbook
-------------

.. admonition:: a2s_

   Note: If you run this role without explicitly
   use any [Public APIs](#public-apis) (variables starte with `a2s_` that
   are not defaults) this Ansible role will make no changes on your system.


.. code-block:: yaml

  # Note: this playbook will run without errors, but will not make changes. You
  #       need to specify variables
  - hosts: all
    roles:
      - { role: fititnt.syntactic_sugar }


*Run only these APIs* playbook example
-------------

a2s have so many features that you play may become bigger. As explained in
[Ansible Playbook Tags](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html)
the Ansible default behavior do not allow run only a subset of a Role withtout
using --tags / --skip-tags from command line:


    *"There is no way to ‘import only these tags’; you probably want to split into
    smaller roles/includes if you find yourself looking for such a feature."*

    -- `Ansible Playbook Tags <https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html>`_

**BUT with a2s you can!**. We provide one workaround using an special variable
`a2s_only`. The best way to use is not define `a2s_only` on your inventory, but
only when importing this role.

.. code-block:: yaml

  # On this a2s example, even if your inventory have more than a2s_groups and
  # a2s_users defined and not using command line --tags, only a subset of a2s will
  # run
  - hosts: all
    role: fititnt.syntactic_sugar
      vars:
      a2s_only:
          - a2s_groups
          - a2s_users


.. code-block:: yaml

  # Instead of using a2s_only, is possible to specify what a2s apis to not run.
  # On this example ones related to database are skipped
  - hosts: all
    role: fititnt.syntactic_sugar
      vars:
        a2s_except:
          - a2s_mysql_dbs
          - a2s_mysql_users


Playbook using all Public APIs
-------------

.. code-block:: yaml

  - hosts: all
    remote_user: root
    vars:

      a2s_directories:
        - path: /var/www/my-app
          owner: app
          group: www-data
          mode: '0755'
        - path: /var/www/my-old-app-folder-to-delete
          state: absent

      a2s_groups:
        - name: group1
        - name: group2

      a2s_users:
        - name: user1
        - name: user2
          groups:
            - group2
        - name: fititnt
          authorized_keys:
            key: https://github.com/fititnt.keys

      # a2s_iswindows: true # Uncomment next variable only for Windows hosts.
    roles:
      - { role: fititnt.syntactic_sugar }


Playbook full example with Continuos Integration and testinfra
-------------

Check the contents of [molecule/default/playbook.yml](molecule/default/playbook.yml)
and our Travis-CI panel at <https://travis-ci.com/fititnt/ap-application-load-balancer-extras>.

If you are not developing an interface that other people depend on or have a
very serius infrastructure or several people making changes, well written
Ansible playbooks may already be great. If this is not sufficient, check our
testinfra tests file at
[molecule/default/tests/test_default.py](molecule/default/tests/test_default.py).
