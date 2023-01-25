# How To enable proxy support in apt package manager for Ubuntu/Lubuntu?

1. Modify/ Create a file apt.conf in /etc/apt/ directory

 `sudo vi /etc/apt/apt.conf`
 
 2. Add the proxy information to teh file
```
Acquire::http::Proxy "http://proxyservername:proxyserverport";
Acquire::https::Proxy "http://proxyservername:proxyserverport";
```
