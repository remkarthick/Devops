# How to run docker commands without sudo

## Create a docker group if it doesn't already exist

sudo groupadd docker

## Add the current user `$USER` to the docker group

sudo gpasswd -a $USER docker
(or)
sudo gpasswd -a kk docker
