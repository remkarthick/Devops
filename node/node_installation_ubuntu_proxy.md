# Download Node For Linux

> https://nodejs.org/dist/v18.13.0/node-v18.13.0-linux-x64.tar.xz

# Copy the downloaded file to /opt directory and extract it
```
sudo tar -xvf node-v18.13.0-linux-x64.tar.xz 
```

# Rename node-v18.13.0-linux-x64 directory name to node
```
sudo mv node-v18.13.0-linux-x64 node
```
# Add the node's bin folder to the path in the .profile file
```
sudo nano ~/.profile
```
> .profile

```
if [ -d "/opt/node/bin" ] ; then
        PATH="$PATH:/opt/node/bin"
fi

```

# Reopen the terminal and check if node is working

```
node -v
npm -v
npx -v
```

# Set proxy for node

npm config set proxy http://proxy-host-name:port


> optional :
> npm config set https-proxy  https://proxy-host-name:port

