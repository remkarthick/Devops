# Check if WSL has a running server

```
wsl -l -v
```
Output:
  NAME      STATE           VERSION
* Alpine    Running         2


# Start Alpine/Ubuntu

```
wsl -d Alpine
```
or
```
wsl -d Ubuntu

```

# Stop Ubuntu

```
wsl --terminate Ubuntu
```

# Install JDK Dependency

```
sudo mkdir /downloads
sudo chmod 777 downloads
cd /downloads
wget https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25.0.3%2B9/OpenJDK25U-jdk_x64_linux_hotspot_25.0.3_9.tar.gz
**/downloads#** tar -xzf OpenJDK25U-jdk_x64_linux_hotspot_25.0.3_9.tar.gz
**/downloads# **ls
OpenJDK25U-jdk_x64_linux_hotspot_25.0.3_9.tar.gz  jdk-25.0.3+9
**/downloads#** sudo mkdir /opt/openjdk25
**/downloads#** sudo chmod 777 /opt/openjdk25
**/downloads#** sudo mv jdk-25.0.3+9 /opt/openjdk25
**/downloads#** cd /opt/openjdk25/
**/opt/openjdk25#** ls
jdk-25.0.3+9
**/opt/openjdk25#** mv ./jdk-25.0.3+9 jdk-25
export JAVA_HOME=/opt/openjdk25/jdk-25
export PATH=$JAVA_HOME/bin:$PATH
echo 'export JAVA_HOME=/opt/openjdk25/jdk-25'>> ~/.profile
echo 'export PATH=$JAVA_HOME/bin:$PATH'>> ~/.profile
source ~/.profile
```

# Download  and install Keycloak

```
cd /downloads
wget https://github.com/keycloak/keycloak/releases/download/26.6.1/keycloak-26.6.1.tar.gz
ls
tar -xzf keycloak-26.6.1.tar.gz
ls
sudo mkdir /opt/keycloak
sudo chmod 777 /opt/keycloak
mv keycloak-26.6.1 /opt/keycloak
```

# Start Keycloak in Linux

```
cd /opt/keycloak/keycloak-26.6.1/bin
nohup ./kc.sh start-dev>keycloak.log 2>&1 &
```

# Check running keycloak

```
ps -ef|grep keycloak
```


# Stop Keycloak

```
pkill -f kc.sh
```

# Simplified Script

## Create a new file "start-keycloak.sh" inside /opt/keycloak
```
#!/bin/bash

KEYCLOAK_HOME="/opt/keycloak/keycloak-26.6.1"
LOG_FILE="$KEYCLOAK_HOME/keycloak.log"

echo "Starting Keycloak..."
nohup "$KEYCLOAK_HOME/bin/kc.sh" start-dev > "$LOG_FILE" 2>&1 &

echo "Keycloak started in background. Logs: $LOG_FILE"
```


## Create a new file "stop-keycloak.sh" inside /opt/keycloak
```
pkill -f kc.sh
```

## Change the execution rights of the file

```
chmod 777 start-keycloak.sh
chmod 777 stop-keycloak.sh
```

# Make Keycloak to listen to all adapters instead of just loopback ip and localhost
--not working
Stop Keycloak and run the below command

```
nohup /opt/keycloak/keycloak-26.6.1/bin/kc.sh start-dev --hostname-strict=false --http-host=0.0.0.0 > keycloak.log 2>&1 &
```

--http-host=0.0.0.0 → listen on all interfaces (not just localhost)
--hostname-strict=false → allows access via hostname/IP (not just exact configured hostname)


# Default URL 

```
https://localhost:8443
```

# Default User

```
admin
```

# After Creating realm, how to check the login

Note: kkrealm is the name of the realm

```
https://localhost:8443/realms/kkrealm/account
```

# Well known configuration url for OIDC

```
https://localhost:8443/realms/kkrealm/.well-known/openid-configuration

```

# SAML IDP Metadata
Select Realm --> Realm Settings -> Genaral -> Endpoints 

```
https://kk-lubuntu-vbox:8443/realms/kkrealm/protocol/saml/descriptor
```

