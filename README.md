# Ansible for Raspberry PI

This Ansible project provides initial setting for RaspberryPI.

## check communication acknowledgement from remote

```bash
ansible -i inventories/<hoge> raspberrypi -m ping (--ask-pass)
```

## dryrun playbook

```bash
ansible-playbook -i inventories/<hoge> raspi3modelb.yml -C (--ask-pass)
```

## run playbook

```bash
ansible-playbook -i inventories/<hoge> raspi3modelb.yml (--ask-pass)
```
