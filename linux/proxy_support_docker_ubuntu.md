# Set Proxy for Docker

1. Create a new directory docker.service.d

`sudo mkdir -p /etc/systemd/system/docker.service.d`


2. Add the below contents to the above file http-proxy.conf


`sudo vi /etc/systemd/system/docker.service.d/http-proxy.conf`

```
[Service]
Environment="HTTP_PROXY=http://proxy_server_name:port"
Environment="HTTPS_PROXY=http://proxy_server_name:port"
```

3. Edit resolv.conf 

`sudo vim /etc/resolv.conf`

4.  Add the below lines above the existing nameserver

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

5. Reload the daemon and restart docker

```
sudo systemctl daemon-reload
sudo systemctl restart docker
```

6. Verify if proxy is in docker environment

`sudo systemctl show --property=Environment docker`


7. Check if docker run is working

`sudo docker run hello-world`

