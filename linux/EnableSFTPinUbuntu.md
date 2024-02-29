
# Update and Upgrade
```
sudo apt update
sudo apt upgrade
```
# Install SSH as its a dependency of SFTP. After installation enable and start the ssh 
```
sudo apt install ssh
sudo systemctl enable ssh
sudo systemctl start ssh
```
# Check the status of ssh
```
sudo systemctl status ssh
```
# Create a sftp group
```
sudo addgroup sftp
```
# Add a user to the above sftp group
```
sudo usermod -a -G sftp kk 
```
# Verify sftp group
```
sudo grep sftp /etc/group
```
# Create a SFTP directory and set the ownership to root user & etc
```
sudo mkdir -p /var/sftp/Files1
sudo chown root:root /var/sftp
sudo chmod 755 /var/sftp
sudo chown kk:sftp /var/sftp/Files1
```
# Open /etc/ssh/sshd_config file and add the below script to the end of the file
`sudo vi /etc/ssh/sshd_config`

```
Match group sftp
ChrootDirectory /var/sftp
X11Forwarding no
AllowTcpForwarding no
ForceCommand internal-sftp
```
# Restart the ssh service
` sudo systemctl restart ssh `

# Connect to the SFTP from your windows command prompt
```
sftp -P 2022 kk@192.168.1.3
```
