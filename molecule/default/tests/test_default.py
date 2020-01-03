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
    assert host.group("cdns").exists
    # assert host.group("group1").exists


def test_users(host):
    assert host.user("cdn-site-a").exists
    assert host.user("cdn-site-b").exists
    assert "cdns" in host.user("cdn-site-a").groups
    assert "cdns" in host.user("cdn-site-b").groups


def test_sample_concent_cdns(host):
    fa = host.file('/home/cdn-site-a/public_html/index.html')
    assert fa.exists
    assert fa.user == 'cdn-site-a'
    assert fa.group == "cdns"

    fb = host.file('/home/cdn-site-b/public_html/index.html')
    assert fb.exists
    assert fb.user == 'cdn-site-b'
    assert fb.group == "cdns"
