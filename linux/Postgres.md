# Password Reset in Postgres

1. Login as root
2. Switch as postgres user
`su - postgres`
3. Type the command `psql` to enter into sql mode.
4. Update the password by issuing the sql statement
`alter user postgres with password '<password>';`

# Check if Postgres is running

`sudo systemctl status postgresql`

Will display postgresql.service as "active (exited)" because it was the parent wrapper , to find the "active (running)" service use the below command

`sudo systemctl status postgresql*`
