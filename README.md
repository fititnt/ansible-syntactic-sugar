# ansible-syntactic-sugar ("a2s") - v0.6.0-alpha

[![Ansible Role](https://img.shields.io/ansible/role/45694)](https://galaxy.ansible.com/fititnt/syntactic_sugar)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/45694)](https://galaxy.ansible.com/fititnt/syntactic_sugar)
[![Build Status](https://travis-ci.com/fititnt/ansible-syntactic-sugar.svg?branch=master)](https://travis-ci.com/fititnt/ansible-syntactic-sugar)

**![Maturity: Technology Preview](https://img.shields.io/badge/Maturity-technology--preview-informational)
`a2s` is a non-official Ansible role that acts as _[syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)_
for [Ansible](https://www.ansible.com/), which without extensions already is
an _"Simple, agentless IT automation that anyone can use"_**.

<!--
By design typical
usage with `a2s` is idempotent and tend to be more cross-platform and less
verbose than alternatives, but have a drawback of not be otimized for more
complex setups.
-->


<!--
`a2s` is a non-official `Syntactic Sugar <https://en.wikipedia.org/wiki/Syntactic_sugar>`_
for `Ansible <https://www.ansible.com/>`_, which without extensions already is
an *"Simple, agentless IT automation that anyone can use"*.

for 1) some [ansible modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html),
2) <s>populate sample content</s><sup>(now on [ansible-faker](https://github.com/fititnt/ansible-faker))</sup>
and 3) install some common software to help with quick tests and 4) even
explain/implement [how to run only a subset of an Ansible role](#a2s_only_apis)**.

-->

> **Warning: this is a Technology Preview release**. While it's used on
non-public projects by it's initial maintainer, it may eventually accept
suggestions that could improve it's base design.

## Documentation

<!--
 References on how to style Sphinix
   - https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html
   - https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html#headings
   - https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/InlineCode.html
-->


Please check <https://ansible-syntactic-sugar.readthedocs.io/>. <s>The contents of
this README file will eventually be migrated</s> The migration starded, but will
take some time to learn/implement a different documentation engine.

Since this project still as pre-release, the documentation may not be the main
focus.

## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
-->

**None.**

This role does not depend on other Ansible roles. Not even the
[ap-application-load-balancer](https://github.com/fititnt/ap-application-load-balancer).

## Example Playbooks

Please check <https://ansible-syntactic-sugar.readthedocs.io/>.

## License

[![Public Domain](https://i.creativecommons.org/p/zero/1.0/88x31.png)](UNLICENSE)

To the extent possible under law, [Emerson Rocha](https://github.com/fititnt)
has waived all copyright and related or neighboring rights to this work to
[Public Domain](UNLICENSE).
