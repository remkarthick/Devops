# Add a User

> sudo useradd -m <user_name>
  
`-m will create a home directory as well for the specified user`

# Delete a User

> sudo userdel -r <user_name>
   
`-r will remove home directory and mail spool`

# Logout a specific user
  
> sudo pkill -9 -u <user_name>
