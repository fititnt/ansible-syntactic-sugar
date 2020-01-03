# ap-application-load-balancer-extras - v0.2.0-alpha

[not-production-ready] Ansible Role with extra optimal features for the
**[AP Application Load Balancer ("AP-ALB")](https://github.com/fititnt/ap-application-load-balancer)**.

---

<!-- TOC depthFrom:2 -->

- [Requirements](#requirements)
- [Role Variables](#role-variables)
    - [Defaults](#defaults)
    - [Internal variables](#internal-variables)
    - [Public APIs](#public-apis)
        - [`albextras_groups`](#albextras_groups)
        - [`albextras_sample_content_cdns`](#albextras_sample_content_cdns)
        - [`albextras_sample_content_static_sites`](#albextras_sample_content_static_sites)
        - [`albextras_sample_content_phps`](#albextras_sample_content_phps)
        - [`albextras_users`](#albextras_users)
- [Dependencies](#dependencies)
- [Example Playbook](#example-playbook)
    - [Minimal Playbook](#minimal-playbook)
    - [Using all Public APIs](#using-all-public-apis)
    - [Complex example](#complex-example)
        - [Complete Continuos Integration example](#complete-continuos-integration-example)
        - [molecule/default/tests/test_default.py](#moleculedefaultteststest_defaultpy)
- [License](#license)
    - [ap-application-load-balancer-extras](#ap-application-load-balancer-extras)
    - [files/static-site](#filesstatic-site)

<!-- /TOC -->

---

<!--
The main objective of this role is add some functionality (for example, very
simple configuration of PHP, Python, Java, Tomcat, ...) using a sintax that
reuse variables of the core role, ap-application-load-balancer, and at least
for some very basic cases or very fast bootstraping do not need use others well
know dedicated Ansible Roles.

If you really heavily on some of these extra features consider search for
<https://github.com/topics/ansible-role>.
-->

## Requirements

<!--
Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->

**None.**

This role does not require anything over the averange for an Ansible role.

## Role Variables

<!--
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
-->

### Defaults

See [defaults/main.yml](defaults/main.yml).

The variables on this file, different from the ones of _Internal variables_
that have a more strong suggestion based on Operational System, may extend
features of the _Public APIs_.

### Internal variables

For internal variables based on OS, check [vars/README.md](vars/README.md).

### Public APIs

#### `albextras_groups`
**List of groups to add/remove.** Values from Ansible modules
[group](https://docs.ansible.com/ansible/latest/modules/group_module.html)
and [win_group](https://docs.ansible.com/ansible/latest/modules/win_group_module.html)

#### `albextras_sample_content_cdns`
**List of paths to deploy sample content of [files/videos](files/videos) and [files/images](files/images)**.
Values from Ansible module [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

#### `albextras_sample_content_static_sites`
**List of paths to deploy sample content of [files/static-site](files/static-site)**.
Values from Ansible module [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

#### `albextras_sample_content_phps`
**List of paths to deploy sample content of [files/php](files/php)**.
Values from Ansible module [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

#### `albextras_users`
**List of users to add/remove.** Values from Ansible modules
[user](https://docs.ansible.com/ansible/latest/modules/user_module.html)
and [win_user](https://docs.ansible.com/ansible/latest/modules/win_user_module.html)


## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
-->

**None.**

This role does not depend on other Ansible roles. Not even the
[ap-application-load-balancer](https://github.com/fititnt/ap-application-load-balancer).

## Example Playbook

### Minimal Playbook

> Note: If you run this role without explicitly
> use any [Public APIs](#public-apis) (variables starte with `albextras_` that
> are not defaults) this Ansible role will make no changes on your system.

```yaml
# Note: this playbook will run without errors, but will not make changes. You
#       need to specify variables
- hosts: all
  roles:
    - { role: fititnt.ap-application-load-balancer-extras }
```

### Using all Public APIs

```yaml
- hosts: all
  remote_user: root
  vars:

    albextras_groups:
      - name: group1
      - name: group2

    albextras_users:
      - name: user1
      - name: user2
        groups:
          - group2

    albextras_sample_content_static_sites:
      - path: /home/user2/public_html
        user: user2

    # albextras_iswindows: true # Uncomment next variable only for Windows hosts.
  roles:
    - { role: fititnt.ap-application-load-balancer-extras }
```

### Complex example
#### Complete Continuos Integration example

Check the contents of [molecule/default/playbook.yml](molecule/default/playbook.yml)
and our Travis-CI panel at <https://travis-ci.com/fititnt/ap-application-load-balancer-extras>.

If you are not developing an interface that other people depend on or have a
very serius infrastructure or several people making changes, well written
Ansible playbooks may already be great. If this is not sufficient, check our
testinfra tests file at
[molecule/default/tests/test_default.py](molecule/default/tests/test_default.py).

#### molecule/default/tests/test_default.py




## License
This Ansible role have content from several places with different licenses and
authors.

### ap-application-load-balancer-extras

[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](UNLICENSE)

To the extent possible under law, [Emerson Rocha](https://github.com/fititnt)
has waived all copyright and related or neighboring rights to this work to
[Public Domain](UNLICENSE).

### files/static-site
**Code licensed MIT, docs CC BY 3.0.**

[files/static-site/index.html](files/static-site/index.html) and it's assets are
Sample Content from Bootstrap documentation. Source:
<https://v4-alpha.getbootstrap.com/examples/jumbotron/>
