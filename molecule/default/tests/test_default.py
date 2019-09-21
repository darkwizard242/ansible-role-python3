import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PYTHON3_BINARY_PATH = '/usr/bin/python3'
PYTHON3_PACKAGE = 'python3'


def test_python3_package_installed(host):
    host.package("PYTHON3_PACKAGE").is_installed


def test_python3_binary_exists(host):
    host.file('PYTHON3_BINARY_PATH').exists


def test_python3_binary_file(host):
    host.file('PYTHON3_BINARY_PATH').is_file


def test_python3_binary_whereis(host):
    host.check_output('whereis python3') == PYTHON3_BINARY_PATH
