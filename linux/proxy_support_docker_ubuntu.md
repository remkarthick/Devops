# Set Proxy for Docker

1. Create a new directory for docker.service.d

sudo mkdir -p /etc/systemd/system/docker.service.d

2. Create a new file inside the above folder

sudo vi /etc/systemd/system/docker.service.d/proxy.conf

3. Add the below contents to the above file proxy.conf

[Service]
Environment="HTTP_PROXY=http://rb-proxy-apac.bosch.com:8080"
Environment="HTTPS_PROXY=http://rb-proxy-apac.bosch.com:8080"
Environment="NO_PROXY="localhost,127.0.0.1,::1"


4. Reload the daemon

sudo systemctl daemon-reload
