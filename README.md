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
