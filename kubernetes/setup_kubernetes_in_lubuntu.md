# Make Full Screen of Lubuntu VM

> In Virtual Box where you have installed Lubuntu Open "Devices ->Install Guest Additions CD Image"

- Open terminal and change ditectory to the Guest Additions folder

> ex. cd /media/kk/VBox_GAs_7.0.4

`
sudo apt-get update
`

`
sudo apt-get install -y gcc make perl
`

`
sudo ./VBoxLinuxAdditions.run
`

`
reboot
`

# Install Open SSH in Lubuntu

> Check if ssh.service is running

`
sudo systemctl status ssh
`

> Install if its not available

`
sudo apt install openssh-server
`
> Check again
sudo systemctl status ssh

