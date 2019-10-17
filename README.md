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

## initial set up

```bash
// dry-run
$ ansible -i inventories/init raspberrypi -m ping --ask-pass -C
SSH password: <enter your password>

// run
$ ansible -i inventories/init raspberrypi -m ping --ask-pass
```
