# Create directory
mkdir compose
cd compose/

# docker compose command
```
docker compose
```
# Download docker-compose.yml file for vprofile project
```
wget https://raw.githubusercontent.com/remkarthick/Devops/main/docker-compose/docker-compose.yml
ls
vim docker-compose.yml
```
# Bring up all the containers
```
docker compose up -d
```
- -d is to run in background

# Check the containers in docker compose
```
docker compose ps
```

# Verify/Validate(get ip iddress - then open browser and enter http://VMIP:80)
```
ip addr show
```
- also http://10.0.2.15/, where cred is admin_vp/admin_vp

# Stops containers and removes containers, networks, volumes, and images created by up.
```
docker compose down
```
- external network and volumes are not removed
# Stops running containers without removing them
```
docker compose stop
```
- They can be started again with "docker compose start"
