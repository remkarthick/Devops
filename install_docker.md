# 1. Uninstall

## Uninstall old versions of docker

`sudo apt-get remove docker docker-engine docker.io containerd runc`

## Uninstall the Docker Engine, CLI, containerd, and Docker Compose packages

`sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-ce-rootless-extras`

## Remove Images, containers, volumes, or custom configuration files on your host

sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd



# 2. Download Docker

Go to https://download.docker.com/linux/ubuntu/dists/

## Select your Ubuntu version in the list.

### You can check the ubuntu version using the below command

`lsb_release -a`

## Go to pool/stable/ and select the applicable architecture

### You can check the machine architecture using the below command

`dpkg --print-architecture`


## Download the following deb files for the Docker Engine, CLI, containerd, and Docker Compose packages

containerd.io_<version>_<arch>.deb
docker-ce_<version>_<arch>.deb
docker-ce-cli_<version>_<arch>.deb
docker-compose-plugin_<version>_<arch>.deb

# 3. Install the deb files

```
 sudo dpkg -i ./containerd.io_<version>_<arch>.deb \
  ./docker-ce_<version>_<arch>.deb \
  ./docker-ce-cli_<version>_<arch>.deb \
  ./docker-compose-plugin_<version>_<arch>.deb
```

The Docker daemon should start automatically.

# 4. Verify

`sudo docker run hello-world`
