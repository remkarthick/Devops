# How to bring Full Screen to a Virtual Box installed Centos 7

> Install kernel-devel

`
sudo yum install kernel-devel
`

> Install gcc, make and perl (if you try to run the VBoxLinuxAdditions.run before this you will get error mentioning to install gcc, make and perl)

`
sudo yum gcc make perl
`

> Go to the VBox Guest Additions media folder and run the VBoxLinuxAdditions.run file

`
cd /run/media/<username>/VBox_GAs_6.1.26
sudo ./VBoxLinuxAdditions.run
`

> Rebooot your system

`
reboot
`
