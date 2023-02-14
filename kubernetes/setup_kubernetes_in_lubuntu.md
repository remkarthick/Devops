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

# Install kubectl

> Always refer to below link for installation of kubernetes
> https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

> install curl if its not available

`
sudo apt install -y curl
`

> create a folder to temporarily store the kubectl download

`
cd ~/Downloads && mkdir kubectl && cd kubectl
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
- Output should be  kubectl: OK


> move to the /usr/local/bin using the below command

`
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
`
- -o  = owner, -g = group ownership,  -m = permission mode
-  install is used to copy files and set attributes

> check if kubectl is working

`
kubectl version --client --output=json
`

# Install kind

> referred from https://kubernetes.io/docs/tasks/tools/ & https://kind.sigs.k8s.io/docs/user/quick-start#installation

```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

> check if its working

`
kind version
`

# For user to access shared folder from windows to linux

share a folder from your host machine to the guest machine.

From linux vm the shared folder will be available in /media/sf_shared . To access the shared folder in linux, you must add your user to the group named vboxsf( obtained by running "ls -l /media/sf_shared")


```
sudo usermod -aG vboxsf kk
```

vboxsf is the group name which has access to shared folder, kk is the user name

> created a link in your linux desktop for the shared folder for ease of use

`
ln -s /media/sf_shared ~/Desktop/shared
` 

# Install Docker

> Manual Installation

Refer https://github.com/remkarthick/Devops/blob/main/docker/02.Install_Docker.md

# Setting Local Cluster to Learn Kubernetes using kind

Refer https://kind.sigs.k8s.io/docs/user/quick-start/#creating-a-cluster

> Create a yaml file with the name kind-example-config.yaml

```
# three node (two workers) cluster config
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
```
> Run the command as below

Note: you may need to clean docker before proceeding to create a cluster

`docker ps -a ` should return nothing.

run `docker system prune` afterwards.

if there is anythin inside `cd ~/.kube` then delete it.


```
kind create cluster --config kind-example-config.yaml
```


> Sample Output

```
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.25.3) 🖼
 ✓ Preparing nodes 📦 📦 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
 ✓ Joining worker nodes 🚜
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a nice day! 👋
```

> Run `docker ps` you will see below output (3 containers are created and running). You will see control-plane running with a port.

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                       NAMES
e81d8c200680   kindest/node:v1.25.3   "/usr/local/bin/entr…"   26 minutes ago   Up 25 minutes                               kind-worker
e239f6dea47b   kindest/node:v1.25.3   "/usr/local/bin/entr…"   26 minutes ago   Up 25 minutes   127.0.0.1:37535->6443/tcp   kind-control-plane
492597f05043   kindest/node:v1.25.3   "/usr/local/bin/entr…"   26 minutes ago   Up 25 minutes                               kind-worker2
```

> Run `docker network ls`. you will see a bridge for kind

```
NETWORK ID     NAME      DRIVER    SCOPE
384ee97ab44f   bridge    bridge    local
53775eb65e3a   host      host      local
d23ad7a0d91e   kind      bridge    local
9542858eb4f0   none      null      local
```

> To check the master/control-plane configuration, such as ip address and port

```
cat ~/.kube/config
```

> run the below command now and you will get server version information without error(previously before the cluster configuration this command would have given error)

```
kubectl version --output=json
```

# Get Nodes

```
kubectl get nodes
```

Sample Output : 

```
NAME                 STATUS   ROLES           AGE   VERSION
kind-control-plane   Ready    control-plane   51m   v1.25.3
kind-worker          Ready    <none>          51m   v1.25.3
kind-worker2         Ready    <none>          51m   v1.25.3

```
# Get inside the individual node

```
docker ps
```

Sample Output : 

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED             STATUS             PORTS                       NAMES
e81d8c200680   kindest/node:v1.25.3   "/usr/local/bin/entr…"   About an hour ago   Up About an hour                               kind-worker
e239f6dea47b   kindest/node:v1.25.3   "/usr/local/bin/entr…"   About an hour ago   Up About an hour   127.0.0.1:37535->6443/tcp   kind-control-plane
492597f05043   kindest/node:v1.25.3   "/usr/local/bin/entr…"   About an hour ago   Up About an hour                               kind-worker2
```

> get inside the control-plane/master to check important files

```
docker exec -it e239f6dea47b bash
```

Sample Output :

```
root@kind-control-plane:/#
```

> Important yaml files inside the control plane

```
cd /etc/kubernetes/manifests/
ls -l
```

Sample Output :

```
total 16
-rw------- 1 root root 2382 Feb 13 08:34 etcd.yaml
-rw------- 1 root root 3873 Feb 13 08:34 kube-apiserver.yaml
-rw------- 1 root root 3405 Feb 13 08:34 kube-controller-manager.yaml
-rw------- 1 root root 1440 Feb 13 08:34 kube-scheduler.yaml

```

> Check the processess running for kube inside master/control-plane

```
ps -ef|grep -n -T -E 'kube|etcd'
```

# Delete the cluster

> exit from the master/control-plane or node/worker if you are already in it.

> delete the cluster

```
kind delete cluster --name kind
```

Note: you can get the cluster name from `kind get clusters`

# Create Pod

- Pod is a type of workload. Its a collection of containers

> Reference

refer Pod in https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/

> create a new file `01-simple-pod.yaml`

```
apiVersion: v1
kind: Pod
metadata: 
  name: kk-pod
spec:
  containers:
  - name: nginx-kk
    image: nginx
```

> Check if pods are running

If cluster is not running run it. To Verify if its running 'kubectl get nodes`. To run it `kind create cluster --config ~/Desktop/shared/kind-learn/Lesson1/kind-example-config.yaml`

Run the command `kubectl get pod` to check or `watch -t -x kubectl get pod` to monitor if there are any pods available.

> create a pod

`kubectl create -f 01-simple-pod.yaml`

> check if pod is running

`kubectl get pod`

> delete a pod

`kubectl delete -f 01-simple-pod.yaml`



# Describe a Pod

 `kubectl describe pod`
 
 

