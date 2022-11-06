# Vagrant Commands Guide

## Check the vagrant version
```
vagrant --version
```

## Get help in vagrant
```
vagrant --help
```
> ex. 
```
vagrant init --help
```
> will give you help for the vagrant init command


## Initialize the current directory to be a Vagrant environment 

```
vagrant init centos/7
```
> before running this command you have to move to a directory where you want to create the Vagrantfile

> this command will create a Vagrantfile if it doesn't already exist.

> here 'centos/7' is a vagrant box, you can find a list of such boxes in https://app.vagrantup.com/boxes/search


```
vagrant init -m centos/7
```
> -m will reate a Vagrantfile that is minimal without any instructional comments

```
vagrant init -f centos/7
```
> -f will replace the existing Vagrant file with a new file

## Starts and configuring the guest machine

```
vagrant up
```

> Other attributes

```
vagrant up <name>
```

```
vagrant up <id>
```
> you can start the guest vm from any folder using the "id". you can get the id using the below command.

```
vagrant global-status
```

## SSH into the vagrant instance

```
vagrant ssh
```


## Get the status

```
vagrant status <name|id>
```
> get the state of the guest machine


```
vagrant global-status --prune
```
> get the state of all active Vagrant environments on the system from the cache(instead of from the actual run time, this is why we use prune to remove the inactive entries). 


## Suspend , Resume, Halt,  Destroy and Remove

> suspend is similar to a sleep mode, if you need to make changes to the vagrant file you can put it in suspend mode ->make changes and then resume it.

```
vagrant suspend <name|id>
```
> suspended box can be resumed using the vagrant resume command

```
vagrant resume <name|id>
```

> Halt command is used to shutdown / poweroff

```
vagrant halt <name|id>
```

> The destroy command is used to remove the guest vm image from vagrant

```
vagrant destroy <name|id>
```

> The remove command is used to remove the box itself from vagrant. You can get the box name using teh vagrant box list command

> if you remove the box and try to use the image that uses the removed box, then the vaggarnt will download  the box again from the internet.
```
vagrant remove <box_name>
```


## List all the vagrant boxes available

```
vagrant box list
```

## Check if the box is out dated and update it

>to check if the box is outdated
```
vagrant box outdated
```
> to update the box
```
vagrant box update
```

## Add a box to vagrant, but do not create Vagrant file

```
vagrant box add ubuntu/trusty64
```
> this command downloads ubuntu/trusty64 box and keeps it ready for future use. When you need to use you can do so by create a new folder and run vagrant init ubuntu/trusty64 and vagrant up. This time instead of downloading from internet, it will use the already downloaded box.

## To Add a box to vagrant from a specific url

```
vagrant box add <box_name> <url>

```

