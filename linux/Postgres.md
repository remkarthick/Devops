# Password Reset in Postgres

1. Login as root
2. Switch as postgres user
`su - postgres`
3. Type the command `psql` to enter into sql mode.
4. Update the password by issuing the sql statement
`alter user postgres with password '<password>';`

# Restart Postgres

`sudo systemctl restart postgresql`

# Check if Postgres is running

`sudo systemctl status postgresql`

Will display postgresql.service as "active (exited)" because it was the parent wrapper , to find the "active (running)" service use the below command

`sudo systemctl status postgresql*`

# Which port Postgres running on 

`pg_lsclusters`

# Unable to connect to Postgres from a different machine

In `/etc/postgresql/16/main/postgresql.conf` set the below property

```
#listen_addresses = '*'		# what IP address(es) to listen on;
					# comma-separated list of addresses;
					# defaults to 'localhost'; use '*' for all
					# (change requires restart)
```


In `/etc/postgresql/16/main/pg_hba.conf` modify the below

```
# IPv4 local connections:
host    all             all             0.0.0.0/0            scram-sha-256
# IPv6 local connections:
host    all             all             ::0/0                 scram-sha-256
```

Restart postgres for teh configuration change to take effect
