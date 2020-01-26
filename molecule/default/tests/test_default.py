import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python3_package_installed(host):
    assert host.package("python3").is_installed


def test_python3_binary_exists(host):
    assert host.file('/usr/bin/python3').exists


def test_python3_binary_file(host):
    assert host.file('/usr/bin/python3').is_file


def test_python3_binary_which(host):
    assert host.check_output('whereis python3') == '/usr/bin/python3'
