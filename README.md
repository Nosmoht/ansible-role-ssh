ssh
==========

- [Introduction](#introduction)
- [Variables](#variables)
- [Usage](#usage)

# Introduction
Use this role to:
- update the SSH package
- configure SSH daemon options
- ensure (create, update or remove) user accounts and deploy public SSH key in authorized_keys retrieved from Git server

__NOTE:__ By default the role ensures that root login via SSH is forbidden.

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
| ssh_sshd_config | List of name/value pairs to ensure | - name: PermitRootLogin\n  value: 'no' |

# Usage
As some tasks require root privileges one should invoke the role with become
using either sudo or su.

Update SSH package
```yaml
---
- hosts: servers
  become: true
  become_method: sudo
  become_user: root
  roles:
  - role: ssh
    ssh_package_state: latest
```

Create a user within group wheel and fetch the public SSH keys from Github.com
```yaml
---
- hosts: servers
  become: true
  become_method: sudo
  become_user: root
  roles:
  - role: ssh
    ssh_git_url: https://github.com
    ssh_users:
    - name: pinky
```

Create user pinky but use the public SSH key of user brain
```yaml
---
- hosts: servers
  become: true
  become_method: sudo
  become_user: root
  roles:
  - role: ssh
    ssh_git_url: https://github.com
    ssh_users:
    - name: pinky
      git_name: brain
```

Create some admin users using an internal Git server to fetch keys and use _admin_
as primary group
```yaml
---
- hosts: servers
  become: true
  become_method: sudo
  become_user: root
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
  become: true
  become_method: sudo
  become_user: root
  roles:
  - role: ssh
    ssh_users:
    - name: jens
      state: absent
```

Ensure SSH daemon configuration
```yaml
---
- hosts: servers
  become: true
  become_method: sudo
  become_user: root
  roles:
  - role: ssh
    ssh_sshd_config:
    - name: PermitEmptyPasswords
      value: 'no'
    - name: Protocol
      value: 2
```
