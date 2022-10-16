# enable ssh in newly installed ubuntu/lubuntu

## Check the ssh status
sudo systemctl status ssh

## If not available then install open ssh server
sudo apt install openssh-server

## After installation check the status of ssh
sudo systemctl status ssh

## Open firewall port in Linux(Ubuntu) for ssh and reload the firewall config
sudo ufw allow ssh (or)
sudo ufw allow 22
sudo ufw reload

# Error Handling on ssh

When trying to start ssh, we get the below error

sudo systemctl start ssh

## Error :
Job for ssh.service failed because the control process exited with error code.
See "systemctl status ssh.service" and "journalctl -xe" for details.

### Try running the command to trace the error

sudo sshd -T

## Error:
sshd: no hostkeys available -- exiting.

### Solution:

sudo ssh-keygen -A

### Now Start the SSH

sudo systemctl start ssh
