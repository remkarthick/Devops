# How to run docker commands without sudo

## Check if a group named docker already exists

cat /etc/group|grep docker

## Create a docker group if it doesn't already exist

sudo groupadd docker

## Add the current user `$USER` to the docker group

sudo gpasswd -a $USER docker
(or)
sudo gpasswd -a kk docker
