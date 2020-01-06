# ansible-syntactic-sugar ("a2s") - v0.4.0-alpha

[![Ansible Role](https://img.shields.io/ansible/role/45694)](https://galaxy.ansible.com/fititnt/syntactic_sugar)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/45694)](https://galaxy.ansible.com/fititnt/syntactic_sugar)
[![Build Status](https://travis-ci.com/fititnt/ansible-syntactic-sugar.svg?branch=master)](https://travis-ci.com/fititnt/ansible-syntactic-sugar)

**[not-production-ready] `a2s` is a non-official optionated cross-platform
Ansible role that acts as _syntactic sugar_ for some [ansible modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html),
populate sample content and install some common software to help with quick tests**.
The main initial reason was to allow build inventories to
[AP-ALB](https://github.com/fititnt/ap-application-load-balancer)
with much less lines of YAML without need to add several independent roles.

> **Warning: this is a pre-release**. A stable version may never be released
with this exact name. Variable naming conventions are likely to change
drastically.

<!--
**[not-production-ready] AP-ALB Extras is a well tested cross-platform Ansible
role that implements non-core and testing features for
[AP-ALB Role](https://github.com/fititnt/ap-application-load-balancer), but as
independent role it can be used by other proposes.**

Note: this project may eventually be renamed.
-->


---

<!-- TOC depthFrom:2 -->

- [Requirements](#requirements)
- [Role Variables](#role-variables)
    - [Public APIs](#public-apis)
        - [`a2s_groups`](#a2s_groups)
        - [`a2s_etchosts`](#a2s_etchosts)
        - [`a2s_hostname`](#a2s_hostname)
        - [`a2s_users`](#a2s_users)
        - [`a2s_users[n]authorized_key`](#a2s_usersnauthorized_key)
        - [`a2s_php_install`](#a2s_php_install)
    - [Devel APIs](#devel-apis)
        - [`a2s_devel_nginx_*`](#a2s_devel_nginx_)
    - [Sample Content](#sample-content)
    - [Special APIs](#special-apis)
        - [`a2s_autoinstall_dependencies`](#a2s_autoinstall_dependencies)
        - [`a2s_autoinstall_repositories`](#a2s_autoinstall_repositories)
        - [`a2s_betatesting`](#a2s_betatesting)
        - [a2s_default_*](#a2s_default_)
            - [`a2s_default_user`](#a2s_default_user)
            - [`a2s_default_group`](#a2s_default_group)
            - [`a2s_default_directory_mode`](#a2s_default_directory_mode)
            - [`a2s_default_file_mode`](#a2s_default_file_mode)
    - [Internal variables](#internal-variables)
- [Dependencies](#dependencies)
- [Example Playbooks](#example-playbooks)
    - [Minimal Playbook](#minimal-playbook)
    - [Playbook using all Public APIs](#playbook-using-all-public-apis)
    - [Playbook full example with Continuos Integration and testinfra](#playbook-full-example-with-continuos-integration-and-testinfra)
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

### Public APIs


#### `a2s_groups`
> Create operational system groups.

**List of groups to add/remove.** Values from Ansible modules
[group](https://docs.ansible.com/ansible/latest/modules/group_module.html)
and [win_group](https://docs.ansible.com/ansible/latest/modules/win_group_module.html)

```yaml
a2s_groups:
  - name: "www-data"
  - name: "haproxy"
```

#### `a2s_etchosts`
> List of strings to be added on /etc/hosts file.

**List of strings**. Example:

```yaml
a2s_etchosts:
  - "127.0.0.1  site-a.local"
  - "198.51.100.0  example.org example.com"
```

#### `a2s_hostname`
> Set hostname respecting [RFC822](https://www.w3.org/Protocols/rfc822/). Uses
[Ansible hostname module](https://docs.ansible.com/ansible/latest/modules/hostname_module.html).

To add to /etc/hosts, check [`a2s_etchosts`](#a2s_etchosts).

#### `a2s_users`
> Create operational system users.

**List of users to add/remove.** Values from Ansible modules
[user](https://docs.ansible.com/ansible/latest/modules/user_module.html)
and [win_user](https://docs.ansible.com/ansible/latest/modules/win_user_module.html)

#### `a2s_users[n]authorized_key`
**Adds or removes an SSH authorized key for the user.** Values from Ansible modules
[authorized_key](https://docs.ansible.com/ansible/latest/modules/authorized_key_module.html)

This option is just an syntax sugar to, on same definition about an user to add
to the system, if you sent a key named `authorized_key`, it will call the
Ansible authorized_key_module. If you omit `a2s_users[n]authorized_key.user`
it will use the `a2s_users[n].name` as default.

#### `a2s_php_install`
- Default: `undefined`
- Type of value: List of Strings; List of Objects (name, state)
- Examples of values: `{{ a2s__php74 }}`,  `{{ a2s__php73 }}`,
  `{{ a2s__php72 }}`, `['php-fpm', 'php-common']` <sup>(assumes state: present)</sup>
  `[{name: 'php-fpm', state: 'present'}, name: 'php-mssql', state: 'absent']`

> Install a list of PHP packages on the system

Variables `a2s__php74`, `a2s__php73`, `a2s__php72`... are a _syntactic sugar_
to install common packages to run Wordpress, Joomla, Drupal and laravel.

In Ansible is possible append arrays values with `+` (objects you use
`| combine()`), e.g `a2s_php_install: "{{ a2s__php74 + ['php7.4-dev', 'php7.4-ldap'] }}"`

### Devel APIs
Different of [Public APIs](#public-apis), the **Devel APIs**, even if may be
used to bootstrap very quickly some system that defaults would aready be great,
do not have the same compromises with **backward compatibility** of non-major
releases (aka a new release of A2S may remove a feature)

[Public APIs](#public-apis)

#### `a2s_devel_nginx_*`

### Sample Content
### Special APIs

#### `a2s_autoinstall_dependencies`
- Default: `false`

Some A2S public APIs may require packages that already are not automaticaly
installed with Ansible. With this option set to true/yes A2S will install for
you.

#### `a2s_autoinstall_repositories`
- Default: `false`

Some A2S public APIs may require dependencies that are not available on some
versions of operational systems without installation of some external
repositories. With this option set to true/yes A2S will autoinstall for
you.

<!--
--- ### Defaults

See [defaults/main.yml](defaults/main.yml).

The variables on this file, different from the ones of _Internal variables_
that have a more strong suggestion based on Operational System, may extend
features of the _Public APIs_.

-->

#### `a2s_betatesting`
- Default: `false`

To keep master branch resonable stable (even if is end users areexpected to use
official releases), some APIs will require set `a2s_betatesting: true`.

These APIs are likely to not support all targeted OSs and not have full
integrations testing.

#### a2s_default_*
The default values from `a2s_default_*` exist to provide consistence
across operational systems and will be used in some places if you did not
explicitly provide a value.

<!--
> **backward compatibility notice**: the values from `a2s_default_*`
> **may** be updated betwen minor versions ("MINOR" on the `MAJOR.MINOR.PATCH`
> format of [SemVer](https://semver.org/) intead of just majors versions of the
> AP-ALB-Extras. If you have strong requeriments, we recommend you to either
> enforce values on your playbooks OR (if want every place to explicitly not
> depend on these defaults) set then to invalid values so any missing try will
> raise imediate errors.

> **Security notice**: these defaults (similar to the default permissions
> permissions of commands like `mkdir`) may be insecure in some contexts. Even
> if you customize them, user/owner and groups are likely depend of the more
> specific case.
-->

##### `a2s_default_user`
##### `a2s_default_group`
##### `a2s_default_directory_mode`
##### `a2s_default_file_mode`

### Internal variables

For internal variables based on OS, check [vars/README.md](vars/README.md).

## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
-->

**None.**

This role does not depend on other Ansible roles. Not even the
[ap-application-load-balancer](https://github.com/fititnt/ap-application-load-balancer).

## Example Playbooks

### Minimal Playbook

> Note: If you run this role without explicitly
> use any [Public APIs](#public-apis) (variables starte with `a2s_` that
> are not defaults) this Ansible role will make no changes on your system.

```yaml
# Note: this playbook will run without errors, but will not make changes. You
#       need to specify variables
- hosts: all
  roles:
    - { role: fititnt.ansible-syntactic-sugar }
```

### Playbook using all Public APIs

```yaml
- hosts: all
  remote_user: root
  vars:

    a2s_groups:
      - name: group1
      - name: group2

    a2s_users:
      - name: user1
      - name: user2
        groups:
          - group2
      - name: fititnt
        authorized_key:
          key: https://github.com/fititnt.keys

    a2s_sample_content_static_sites:
      - path: /home/user2/public_html
        user: user2

    # a2s_iswindows: true # Uncomment next variable only for Windows hosts.
  roles:
    - { role: fititnt.ap-application-load-balancer-extras }
```
### Playbook full example with Continuos Integration and testinfra

Check the contents of [molecule/default/playbook.yml](molecule/default/playbook.yml)
and our Travis-CI panel at <https://travis-ci.com/fititnt/ap-application-load-balancer-extras>.

If you are not developing an interface that other people depend on or have a
very serius infrastructure or several people making changes, well written
Ansible playbooks may already be great. If this is not sufficient, check our
testinfra tests file at
[molecule/default/tests/test_default.py](molecule/default/tests/test_default.py).

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
