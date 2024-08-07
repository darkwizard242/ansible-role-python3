[![build-test](https://github.com/darkwizard242/ansible-role-python3/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-python3/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-python3/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-python3/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/python3) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-python3&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-python3) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-python3&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-python3) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-python3&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-python3) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-python3?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-python3?color=orange&style=flat-square)

# Ansible Role: python3

Role to install [python3](https://www.python.org/) package on **Debian/Ubuntu** and **EL** systems. These are the default versions available in repositories and may change based on whatever is available on the default OS repositories.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
python3_app_debian_package: python3
python3_app_el_package: python3
python3_desired_state: present
```

### Variables table:

Variable                   | Description
-------------------------- | -----------------------------------------------------------------------------------------------------------------------------
python3_app_debian_package | Defines the app to install on Debian based systems i.e. **python3**
python3_app_el_package     | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **python3**
python3_desired_state      | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **python3** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.python3
```

For customizing behavior of role (i.e. installation of latest **python3** package instead of ensure it is installed ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.python3
  vars:
    python3_desired_state: latest
```

For customizing behavior of role (i.e. installation of **python3** package in regards to EL systems) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.python3
  vars:
    python3_app_el_package: python3
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-python3/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
