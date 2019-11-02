# ap-application-load-balancer-extras - v0.1-alpha
[draft] Ansible Role with extra optimal features for the
**[Águia Pescadora Application Load Balancer ("AP-ALB")](https://github.com/fititnt/ap-application-load-balancer)**.

The main objective of this role is add some functionality (for example, very
simple configuration of PHP, Python, Java, Tomcat, ...) using a sintax that
reuse variables of the core role, ap-application-load-balancer, and at least
for some very basic cases or very fast bootstraping do not need use others well
know dedicated Ansible Roles.

If you really heavily on some of these extra features consider search for
<https://github.com/topics/ansible-role>.

Requirements
------------

<!--
Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->

- **Ubuntu Server 18.04 LTS**

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
-->

Depends on [ap-application-load-balancer](https://github.com/fititnt/ap-application-load-balancer).

Example Playbook
----------------

Look at [documentation.md](documentation.md) for more details.

<!--

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

-->

```yml

# This is just a draft

- name: "eticaai_data_warehouse"
  hosts: all
  remote_user: root
  vars:
    application_load_balancer_name: "Etica.AI/DW"
    application_load_balancer_forcedebug: yes

    #application_load_balancer_forceignore_extra_php: false
    #alb_extra_php_php56_enabled: true
    #alb_extra_php_php56_state: absent
    #alb_extra_php_php70_enabled: true
    #alb_extra_php_php70_state: absent
    #alb_extra_php_php71_enabled: true
    #alb_extra_php_php71_state: absent
    #alb_extra_php_php72_enabled: true
    #alb_extra_php_php73_enabled: true
    #alb_extra_php_php74_enabled: true
    #alb_extra_php_php74_state: absent

    application_load_balancer_apps:

      - app_uid: "ftp"
        app_domain: "ftp.dw.etica.ai"
        app_root: "/data/public"
        app_forcehttps: yes
        app_alb_strategy: "files-local"

      - app_uid: "minio"
        app_domain: "minio.dw.etica.ai"
        app_forcehttps: yes
        app_alb_strategy: "proxy"
        app_alb_proxy: "http://127.0.0.1:9091"

  roles:
    - ap-application-load-balancer-extras
    - ap-application-load-balancer
```

License
-------

Public Domain

Author Information
------------------

Emerson Rocha <rocha(at)ieee.org>. Organization: [Etica.AI](https://etica.ai).
