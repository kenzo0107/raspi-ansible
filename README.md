# Ansible for Raspberry PI

This Ansible project provides initial setting for RaspberryPI.

## set inventory

inventories/init
```bash
[raspberrypi]
raspberry.local

[raspberrypi:vars]
ansible_port=22
ansible_user=pi
```

## Initial set up

### Install sshpass

```
macOS$ brew install hudochenkov/sshpass/sshpass
```

### ping raspberrypi via ansible

```console
// dry-run
$ ansible -i inventories/init raspberrypi -m ping --ask-pass -C
SSH password: <enter your password>

// run
$ ansible -i inventories/init raspberrypi -m ping --ask-pass
```

## run ansible-playbook with password

```
// dry-run
$ ansible-playbook -i inventories/init raspberrypi.yml --ask-pass -C

$ ansible-playbook -i inventories/init raspberrypi.yml --ask-pass
```


## set ssh_config and ansible.cfg

* ssh_config. ex:
```
Host my-raspberrypi-zero-wh
  User pi
  Port 20002
  HostName 192.168.11.xx
  IdentityFile ~/.ssh/Tanaka/id_rsa_raspi
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null
```

* ansible.cfg

```
[defaults]
interpreter_python=/usr/bin/python3 # pip コマンドを python3 で実行する

[ssh_connection]
ssh_args = -F ssh_config
```

## run ansible-playbook after set up private key

```console
// dry-run
$ ansible-playbook raspberrypi.yml -C

$ ansible-playbook raspberrypi.yml
```
