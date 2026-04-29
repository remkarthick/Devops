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

# Download Keycloak

```
wget https://github.com/keycloak/keycloak/releases/download/26.6.1/keycloak-26.6.1.tar.gz
```

# Start Keycloak in Linux

cd /opt/keycloak/keycloak-26.0.7/bin

```
./kc.sh start
```

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

