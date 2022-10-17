# Vagrant Commands Guide

## Check the vagrant version
`
vagrant --version
`


## Initialize the current directory to be a Vagrant environment 

`
vagrant init centos/7
`
> this command will create a Vagrantfile if it doesn't already exist.


`
vagrant init -m centos/7
`
> -m will reate a Vagrantfile that is minimal without any instructional comments

`
vagrant init -f hashicorp/precise64
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
> you can get the id using the command

`
vagrant global-status
`
> you can start the guest vm from any folder using the <id>

## Get the status

`
vagrant status <name|id>
`

> get the status of the guest machine

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



