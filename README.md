ssh
==========

- [Introduction](#introduction)
- [Variables](#variables)
- [Usage](#usage)

# Introduction
Main prupose of this role is to update the SSH package as well as setting up
user accounts and provide SSH keys in authorized_keys.

As SSH service must run to use Ansible on a remote host the installation is not
really useful.

# Variables

| Name | Description | Default |
|:-----|:------------|:--------|
| ssh_package_name | Package name to install/update | openssh-server |
| ssh_package_state | Package state | installed |
| ssh_service_name | Service name | sshd |
| ssh_service_state | Service state | started |
| ssh_service_enabled | Service enabled? | true |
| ssh_default_user_group | Default primary group of created users | wheel |
| ssh_default_user_state | Default state of created user | present |
| ssh_git_url | URL of Git server used to fetch public keys | https://github.com |
| ssh_users | Dictionary containing user information | [] |

# Usage

Update SSH package
```yaml
---
- hosts: servers
  roles:
  - role: ssh
    ssh_package_state: latest
```

Create a user within group wheel and fetch the public SSH keys from Github.com
```yaml
---
- hosts: servers
  roles:
  - role: ssh
    ssh_users:
    - name: pinky
```

Create some admin users using an internal Git server to fetch keys and use _admin_
as primary group
```yaml
---
- hosts: servers
  roles:
  - role: ssh
    ssh_git_url: http://git.example.com
    ssh_default_user_group: admin
    ssh_users:
    - name: brain
    - name: snowball  
```

Ensure a user does not exist
```yaml
---
- hosts: servers
  roles:
  - role: ssh
    ssh_users:
    - name: jens
      state: absent
```
