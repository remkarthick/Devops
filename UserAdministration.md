# Commands for User Administration

## Add a User

> sudo useradd -m <user_name>
  
`-m will create a home directory as well for the specified user`

## Delete a User

> sudo userdel -r <user_name>
   
`-r will remove home directory and mail spool`

## Logout a specific user
  
> sudo pkill -9 -u <user_name>

## Get the id, primary group and other groups of a user
  
> sudo id <user_name_optional>
> Note : Also, groups (or) groups <user_name> will display the groups of logged in user/specified user

## Get All Groups in the System
  
> sudo cat /etc/group
> (or)
> sudo getent group

## Add User to a Group
  
> sudo usermod -aG <group_name> <user_name>


  ### Add User to a sudo Group
  
  > sudo usermod -aG sudo <user_name>




