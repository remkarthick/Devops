# Installing Hashicorp Vault

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

# Create a Secrets Engine to store credentials

1. Navigate to the Vault URL.
2. Go to Secrets Engine and click Enable new engine.
3. Choose Generic -> KV as the engine type.
4. Click Create secret and specify the path as jenkins.
5. Add a new key named user and assign it a value.
6. Add another key named pass and assign it a value.

## To view the above details from the command line:

Ensure the Vault server address is set as an environment variable (if not already configured):
```
export VAULT_ADDR='http://localhost:8200'
```

Execute the following command to retrieve the secret:
```
vault kv get -mount="kv" "jenkins"
```

Here, kv refers to the secrets engine mount, and jenkins is the secret path.

Example:
<img width="572" height="321" alt="image" src="https://github.com/user-attachments/assets/92d6d272-2c90-4365-802b-c8142a0d0ddb" />

