# While trying to install vscode in Ubuntu you get the below error

```
it is held by process (unattended-upgr)
```

## Stop the automatic updater:

```
sudo dpkg-reconfigure -plow unattended-upgrades
```

Select the option not to download automatically, this can be turned on after all steps are done

You will receive the below output

```
Replacing config file /etc/apt/apt.conf.d/20auto-upgrades with new version
```

## Reboot the systen

```
reboot
```

## Ensure taht the packages in unclean state are installed correctly

```
sudo dpkg --configure -a
```

## Update your system

```
sudo apt update && sudo apt -f install && sudo apt full-upgrade
```

## Final Step : Start the automatic updater again
```
sudo dpkg-reconfigure -plow unattended-upgrades
```
