# ansible-syntactic-sugar ("a2s") - v0.5.0-alpha

[![Ansible Role](https://img.shields.io/ansible/role/45694)](https://galaxy.ansible.com/fititnt/syntactic_sugar)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/45694)](https://galaxy.ansible.com/fititnt/syntactic_sugar)
[![Build Status](https://travis-ci.com/fititnt/ansible-syntactic-sugar.svg?branch=master)](https://travis-ci.com/fititnt/ansible-syntactic-sugar)

**[not-production-ready] `a2s` is a non-official optionated cross-platform
Ansible role that acts as _syntactic sugar_ for 1) some [ansible modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html),
2) <s>populate sample content</s><sup>(now on [ansible-faker](https://github.com/fititnt/ansible-faker))</sup>
and 3) install some common software to help with quick tests and 4) even
explain/implement [how to run only a subset of an Ansible role](#a2s_only)**.

> **Warning: this is a pre-release**. Variable naming conventions may change.
Feedback is welcome!

**Why?**

The main initial reason (in fact, the initial name was AP-ALB-Extras) was allow
users of [AP-ALB](https://github.com/fititnt/ap-application-load-balancer)
implement with less YAML lines of code common tasks on nodes that not act only
as load balancer and may have apps installed on them. For example, while AP-ALB
abstract proxy rules to HAProxy & OpenResty, it does not abstract create users,
groups & folders from a node. This role does this type of _extra_ task.

It was renamed to _"syntactic sugar"_ since what it does is not exclusive to
AP-ALB and most of what is implemented is possible to do using ad-hoc or single
tasks scripts and yet, different from most Ansible roles, it is not specialized
to a single final task.

**Quick info about compatibility with other roles and how this role try to play nice**

1. One idea behind a2s is be able to _"a2s_autoinstall"_ repositories and
   non-explicitly dependencies _on demand_, but both cases are disabled by
   default.
2. All variables are namespaced, prefixed with `a2s_`; when they end with 's'
   and uses a name similar to an Ansible module, is likely that it acepts a list
   of options availible on the Ansible module equivalent **but** are tolerant
   to add a option that the underlining module does not support
   - e.g [`a2s_users`](#a2s_users) vs [Ansible user](https://docs.ansible.com/ansible/latest/modules/user_module.html)
     \+ [Ansible win_user](https://docs.ansible.com/ansible/latest/modules/win_user_module.html)
3. (TODO: add more topics)

<!--
Tip: while a2s allows autoinstall some requeriments, both
`a2s_autoinstall_repositories` and `a2s_autoinstall_dependencies` are disabled
by default.

The main initial reason was to allow non-experts build inventories powerfull
enough to deploy some features not available on [AP-ALB](https://github.com/fititnt/ap-application-load-balancer)
with less lines of YAML. Another reason is that on average most community roles
support less platforms than AP-ALB
-->


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
        - [`a2s_directories`](#a2s_directories)
        - [`a2s_groups`](#a2s_groups)
        - [`a2s_etchosts`](#a2s_etchosts)
        - [`a2s_hostname`](#a2s_hostname)
        - [`a2s_install_adminer` <sup>a2s_betatesting</sup>](#a2s_install_adminer-supa2s_betatestingsup)
        - [`a2s_install_composer` <sup>a2s_betatesting</sup>](#a2s_install_composer-supa2s_betatestingsup)
        - [`a2s_install_composers` <sup>a2s_betatesting</sup>](#a2s_install_composers-supa2s_betatestingsup)
        - [`a2s_install_php` <sup>a2s_betatesting</sup>](#a2s_install_php-supa2s_betatestingsup)
        - [`a2s_users`](#a2s_users)
        - [`a2s_users[n]authorized_keys`](#a2s_usersnauthorized_keys)
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
            - [`a2s_only`](#a2s_only)
    - [Internal variables](#internal-variables)
- [Dependencies](#dependencies)
- [Example Playbooks](#example-playbooks)
    - [Minimal Playbook](#minimal-playbook)
    - [_Run only these APIs_ playbook example](#_run-only-these-apis_-playbook-example)
    - [Playbook using all Public APIs](#playbook-using-all-public-apis)
    - [Playbook full example with Continuos Integration and testinfra](#playbook-full-example-with-continuos-integration-and-testinfra)
- [License](#license)

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

#### `a2s_directories`
- **Short Description**: _file – Manage <s>files</s> directories and <s>file</s>
  directories properties_
- **Ansible Modules**:
  - [file](https://docs.ansible.com/ansible/latest/modules/file_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  module. `state` value will default `directory`. Other missing values will be
  ommited.
- **Examples**
  - Example 1:
    ```yaml
    a2s_directories:
      - path: /var/www/my-app
        owner: app
        group: www-data
        mode: '0755'
      - path: /var/www/my-old-app-folder-to-delete
        state: absent
    ```

#### `a2s_groups`
- **Short Description**: _group – Add or remove groups / win_group – Add and
  remove local groups_
- **Ansible Modules**:
  - [group](https://docs.ansible.com/ansible/latest/modules/group_module.html)
  - [win_group](https://docs.ansible.com/ansible/latest/modules/win_group_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  modules. Missing values will be ommited.
- **Examples**
  - Example 1:
    ```yaml
    a2s_groups:
      - name: "www-data"
      - name: "haproxy"
      - name: "user-to-remove"
        state: "absent"
  ```

#### `a2s_etchosts`
- **Short Description**: _List of strings to be added on /etc/hosts file. The
  current implementation will not will not replace older values._
- **Ansible Modules**:
  - None. This is a custom implementation.
- **Type of values**: List of strings.
- **Examples**
  - Example 1:
    ```yaml
    a2s_etchosts:
      - "127.0.0.1  site-a.local"
      - "198.51.100.0  example.org example.com"
    ```

Note: `a2s_etchosts` is very likely to be improved before a2s stable release.

#### `a2s_hostname`
- **Short Description**: _hostname – Manage hostname, enforcing
  [RFC822](https://www.w3.org/Protocols/rfc822/ format to avoid fail_
- **Ansible Modules**:
  - [hostname](https://docs.ansible.com/ansible/latest/modules/hostname_module.html)
- **Type of values**: Dictionary. Same values of Ansible module hostname.

To add to /etc/hosts, check [`a2s_etchosts`](#a2s_etchosts).

#### `a2s_install_adminer` <sup>a2s_betatesting</sup>
- Default: `undefined`
- Type of value: Dictionary (name, state)
- Examples of values: `{{ a2s__adminer }}`

> Install adminer

Variable `{{ a2s__adminer }}` are a _syntactic sugar_ for the default parameters

#### `a2s_install_composer` <sup>a2s_betatesting</sup>
- **Short Description**: _Install [composer](https://getcomposer.org/) required
  by [Ansible composer](https://docs.ansible.com/ansible/latest/modules/composer_module.html)
  by default on global path_
- **Ansible Modules**:
  - None
- **Type of values**: Boolean, Dictionary

All these examples have the same effect (install on global scope)

```yaml
a2s_install_composer: true
```
```yaml
a2s_install_composer: "{{ a2s__composer }}"
```
```yaml
a2s_install_composer:
  - path: /usr/local/bin
    user: root
```

#### `a2s_install_composers` <sup>a2s_betatesting</sup>
- **Short Description**: _Install [composer](https://getcomposer.org/) required
  by [Ansible composer](https://docs.ansible.com/ansible/latest/modules/composer_module.html)
  for more than one user_
- **Ansible Modules**:
  - None
- **Type of values**: List of Dictionaries

```yaml
a2s_install_composers:
  - "{{ a2s__composer }}" # Global, as root
  - path: '/home/user1/bin'
    user: user1
  - path: '/home/user2/bin'
    user: user2
```

#### `a2s_install_php` <sup>a2s_betatesting</sup>
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

#### `a2s_users`
- **Short Description**: _user – Manage user accounts / win_user – Manages local
  Windows user accounts_
- **Ansible Modules**:
  - [user](https://docs.ansible.com/ansible/latest/modules/user_module.html)
  - [win_user](https://docs.ansible.com/ansible/latest/modules/win_user_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  modules. Missing values will be ommited.

#### `a2s_users[n]authorized_keys`
- **Short Description**: _authorized_key – Adds or removes an SSH authorized key_
- **Ansible Modules**:
  - [authorized_key](https://docs.ansible.com/ansible/latest/modules/authorized_key_module.html)
- **Type of values**: list of dictionaries accepted by the underlining Ansible
  modules. Missing required `user` (`a2s_users[n]authorized_keys[m]user`) will
  default to `name` (`a2s_users[n]name`). Other missing values will be ommited

<!--

-- ### Devel APIs
Different of [Public APIs](#public-apis), the **Devel APIs**, even if may be
used to bootstrap very quickly some system that defaults would aready be great,
do not have the same compromises with **backward compatibility** of non-major
releases (aka a new release of A2S may remove a feature)

[Public APIs](#public-apis)

-- #### `a2s_devel_nginx_*`

-->

### Sample Content

Since ansible-syntactic-sugar v0.4.0-alpha, sample content was moved to a
dedicated role, [ansible-faker](https://github.com/fititnt/ansible-faker).

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
##### `a2s_only`
- **Short Description**: _Allow run only a subset of a a2s_
- **Ansible Modules**:
  - None. Uses simple `when` trick to overcome tags limitation
- **Type of values**: list of a2s public APIs
- **Example**: see [_Run only these APIs_ playbook example](#_run-only-these-apis_-playbook-example).

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
    - { role: fititnt.syntactic_sugar }
```

### _Run only these APIs_ playbook example

a2s have so many features that you play may become bigger. As explained in
[Ansible Playbook Tags](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html)
the Ansible default behavior do not allow run only a subset of a Role withtout
using --tags / --skip-tags from command line:

> _"There is no way to ‘import only these tags’; you probably want to split into
  smaller roles/includes if you find yourself looking for such a feature."_

**BUT with a2s you can!**. We provide one workaround using an special variable
`a2s_only`. The best way to use is not define `a2s_only` on your inventory, but
only when importing this role.

```yaml
# On this a2s example, even if your inventory have more than a2s_groups and
# a2s_users defined and not using command line --tags, only a subset of a2s will
# run
- hosts: all
  - role: fititnt.syntactic_sugar
    vars:
      a2s_only:
        - a2s_groups
        - a2s_users
```

### Playbook using all Public APIs

```yaml
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

[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](UNLICENSE)

To the extent possible under law, [Emerson Rocha](https://github.com/fititnt)
has waived all copyright and related or neighboring rights to this work to
[Public Domain](UNLICENSE).
