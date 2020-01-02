# ap-application-load-balancer-extras - v0.2.0-alpha
[not-production-ready] Ansible Role with extra optimal features for the
**[AP Application Load Balancer ("AP-ALB")](https://github.com/fititnt/ap-application-load-balancer)**.

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

## Role Variables

<!--
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
-->

See [defaults/main.yml](defaults/main.yml).

For internal variables based on OS, check [vars/README.md](vars/README.md).

### `albextras_groups`
**List of groups to add/remove.** Values from
[group](https://docs.ansible.com/ansible/latest/modules/group_module.html)
and [win_group](https://docs.ansible.com/ansible/latest/modules/win_group_module.html)

### `albextras_sample_content_cdns`
**List of paths to deploy sample content of [files/videos](files/videos) and [files/images](files/images)**.
Values from [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

### `albextras_sample_content_static_sites`
**List of paths to deploy sample content of [files/static-site](files/static-site)**.
Values from [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

### `albextras_sample_content_phps`
**List of paths to deploy sample content of [files/php](files/php)**.
Values from [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html).

### `albextras_users`
**List of users to add/remove.** Values from
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
