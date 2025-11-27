# Installig Hashicorp Vault

Refer : `https://developer.hashicorp.com/vault/install`

For ubuntu

```
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vault
```

# Configure Environment Variable

Refer : `https://developer.hashicorp.com/vault/docs/commands`

```
export VAULT_ADDR='http://localhost:8200'
```

# Check if vault is running

```
vault status
```

# Start the vault server

```
vault server -dev
```

* This will start a inmemory vault which should not be used for production use
* You will get an unseal key and root token. The root token which you can use to login to the local vault http://localhost:8200

```
Unseal Key: <some token>
Root Token: <some other token>
```
