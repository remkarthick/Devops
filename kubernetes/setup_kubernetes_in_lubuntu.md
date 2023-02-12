# Make Full Screen of Lubuntu VM

> In Virtual Box where you have installed Lubuntu Open "Devices ->Install Guest Additions CD Image"

- Open terminal and change ditectory to the Guest Additions folder

> ex. cd /media/kk/VBox_GAs_7.0.4

`
sudo apt-get update 
(or)
sudo apt update
`

`
sudo apt-get install -y gcc make perl
(or)
sudo apt install -y gcc make perl
`

`
sudo ./VBoxLinuxAdditions.run
`

`
reboot
`

# Install Open SSH in Lubuntu

> Check if ssh.service is running

`
sudo systemctl status ssh
`

> Install if its not available

`
sudo apt install openssh-server
`
> Check again
sudo systemctl status ssh

> Open Firewall Port ( If Firewall is enabled)

`
sudo ufw allow 22
`
`
sudo ufw reload
`

- now using port forwarding, you will be able to access ssh from your local machine
![image](https://user-images.githubusercontent.com/36703610/218302571-35d1bb31-6179-41ae-a165-8d6414fecb61.png)

# Install Kubernetes

> Always refer to below link for installation of kubernetes
> https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

> install curl if its not available
`
sudo apt install curl

`

> create a folder to temporarily store the kubectl download
`
cd /home/kk
mkdir kubectl
cd kubectl
`

> download the latest version of kubectl to current folder
`
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
`
> verify if the downloaded file is valid

`
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
`

`
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
`
- kubectl: OK


> move to the /usr/local/bin using the below command

`
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
`
- -o  = owner, -g = group ownership,  -m = permission mode
-  install is used to copy files and set attributes
