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
- **Short Description**: _Install [adminer](https://www.adminer.org/), "Database
  management in a single PHP file"_
- **Default**: `undefined`
- **Type of value**: Dictionary (name, state)
- **Examples of values**: `{{ a2s__adminer }}`

Variable `{{ a2s__adminer }}` are a _syntactic sugar_ for the default parameters

#### `a2s_install_composer`
- **Short Description**: _Install [composer](https://getcomposer.org/) required
  by [Ansible composer](https://docs.ansible.com/ansible/latest/modules/composer_module.html)
  by default on global path_
- **Ansible Modules**:
  - None. Custom implementation.
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
    force: false # true force reinstall
    version: '' # use custom version to install
    php: 'php' # php binary to use. If is not 'php' customize here
```

#### `a2s_install_composers`
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

#### `a2s_mysql_dbs`

> TODO: document a2s_mysql_dbs (fititnt, 2020-01-13 06:01 BRT)

#### `a2s_mysql_users`

> TODO: document a2s_mysql_users (fititnt, 2020-01-13 06:01 BRT)

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
##### `a2s_except`
- **Short Description**: _Restrict a subset of a a2s to not run even if
  variables are defined_
- **Ansible Modules**:
  - None. Uses simple `when` trick to overcome tags limitation
- **Type of values**: list of a2s public APIs
- **Example**: see [_Run only these APIs_ playbook example](#_run-only-these-apis_-playbook-example).

##### `a2s_only`
- **Short Description**: _Allow run only a subset of a a2s_
- **Ansible Modules**:
  - None. Uses simple `when` trick to overcome tags limitation
- **Type of values**: list of a2s public APIs
- **Example**: see [_Run only these APIs_ playbook example](#_run-only-these-apis_-playbook-example).
