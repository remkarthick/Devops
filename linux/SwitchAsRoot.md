# Methods to Switch as a Root User in Linux

> Difference between sudo and su

| sudo | su |
|-|-|
|superuser do| switch user |
| runs your commands with elevated prvileges | to switch as another user |
| will ask your password | will ask the specified users password |

> Provided below are the methods you can use to switch as a root user

## Method 1

```
su
```
Enter the password for the root

## Method 2

```
su -
```
Enter the password for the root

> using - with su will help you bring up the roots's environment variables such as path as well.  
> not using - will bring only the privileges of the root user 

## Method 3

```
sudo su -
```
Enter the password for your account



## Method 4

```
sudo -u root -s
```
Enter the password for your account
> u - user  
> s - shell support



## Method 5

```
sudo -i
```
Enter the password for your account



