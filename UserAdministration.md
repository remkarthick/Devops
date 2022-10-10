# Commands for User Administration

## Add a User

```
sudo useradd -m <user_name>
```
  
> -m will create a home directory as well for the specified user


## Delete a User

```
sudo userdel -r <user_name>
```
   
> -r will remove home directory and mail spool

## Logout a specific user
  
```
sudo pkill -9 -u <user_name>
```

## Get the id, primary group and other groups of a user
  
```
sudo id <user_name_optional>
```

> Note : Also, groups (or) groups <user_name> will display the groups of logged in user/specified user

## Get All Groups in the System
  
```
sudo cat /etc/group
```
(or)
```
sudo getent group
```

## Add User to a Group
  
```
sudo usermod -aG <group_names> <user_name>
```

> a - append  
> G - supplementary groups list

example : (the below command will add the user to the sudo group/sudoers list)
```
sudo usermod -aG sudo <user_name>
```

Additionally the  **gpasswd** command also will add user to a group

```
sudo gpasswd -a <user_name> <group_name>
```
> a - add user to group    

## Change the user's primary group

```
sudo usermod -g <group_name> <user_name>
```
> g - primary group

## Remove User from a Group
  
```
sudo gpasswd -d <user_name> <group_name>
```
> d - remove user from group    

## Create a new Group
  
```
sudo groupadd <group_name>
```
> Note : you can use **sudo groupdel <group_name>** to delete a preexisting group.  






