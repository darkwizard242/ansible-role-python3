import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE1 = 'python3'
PACKAGE2 = 'python36'
PACKAGE_BINARY = '/usr/bin/python3'


def test_python3_package_installed(host):
    """
    Tests if python3/python36 is installed.
    """
    assert host.package(PACKAGE1).is_installed or \
        host.package(PACKAGE2).is_installed


def test_python3_binary_exists(host):
    """
    Tests if python3 binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_python3_binary_file(host):
    """
    Tests if python3 binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_python3_binary_which(host):
    """
    Tests the output to confirm python3's binary location.
    """
    assert host.check_output('which python3') == PACKAGE_BINARY
