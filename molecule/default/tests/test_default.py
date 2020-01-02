import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root' or f.group == 'wheel'


def test_groups(host):
    assert host.group("group1").exists
    assert host.group("group1").exists


def test_users(host):
    assert host.user("user1").exists
    assert host.user("user2").exists
    assert "group2" in host.user("user2").groups
