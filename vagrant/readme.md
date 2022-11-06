# Vagrant Commands Guide

## Check the vagrant version
```
vagrant --version
```


## Initialize the current directory to be a Vagrant environment 

```
vagrant init centos/7
```
> before running this command you have to move to a directory where you want to crea

> this command will create a Vagrantfile if it doesn't already exist.

> here 'centos/7' is a vagrant box, you can find a list of such boxes in https://app.vagrantup.com/boxes/search


`
vagrant init -m centos/7
`
> -m will reate a Vagrantfile that is minimal without any instructional comments

`
vagrant init -f centos/7
`
> -f will replace the existing Vagrant file with a new file

## Starts and configuring the guest machine

`
vagrant up
`

> Other attributes

`
vagrant up <name>
`

`
vagrant up <id>
`
> you can start the guest vm from any folder using the "id". you can get the id using the below command.

`
vagrant global-status
`


## Get the status

`
vagrant status <name|id>
`
> get the state of the guest machine


`
vagrant global-status --prune
`
> get the state of all active Vagrant environments on the system from the cache(instead of from the actual run time, this is why we use prune to remove the inactive entries). 


## Suspend , Halt and Destroy

`
vagrant suspend <name|id>
`
> Similar to a sleep mode

`
vagrant halt <name|id>
`
> Same as shutting down / poweroff

`
vagrant destroy <name|id>
`
> Removes the guest vm image from vagrant



