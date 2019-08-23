import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PYTHON3_DEBIAN_BINARY_PATH = '/usr/bin/python3'
PYTHON3_DEBIAN_PACKAGE = 'python3'
PYTHON3_EL_BINARY_PATH = '/usr/bin/python36'
PYTHON3_EL_PACKAGE = 'python36'


def test_python3_package_installed(host):
    host.package("PYTHON3_DEBIAN_PACKAGE").is_installed or \
      host.package("PYTHON3_EL_PACKAGE").is_installed


def test_python3_binary_exists(host):
    host.file('PYTHON3_DEBIAN_BINARY_PATH').exists or \
      host.file('PYTHON3_EL_BINARY_PATH').exists


def test_python3_binary_file(host):
    host.file('PYTHON3_DEBIAN_BINARY_PATH').is_file or \
      host.file('PYTHON3_EL_BINARY_PATH').is_file


def test_python3_binary_whereis(host):
    host.check_output('whereis python3') == PYTHON3_DEBIAN_BINARY_PATH or \
      host.check_output('whereis python36') == PYTHON3_EL_BINARY_PATH