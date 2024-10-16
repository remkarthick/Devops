# Virtual Box - Access Denied to Shared Folder - Error Opening directory'/media/sf_SHARED':Permission denied

# 1 . User must be added to a specific group named "vboxsf"

```
kk@kk-lubuntu-vbox:/media$ ls -lrt
drwxrwx---  1 root vboxsf    0 Oct 16 22:31 sf_SHARED
```

```
sudo usermod -aG vboxsf <user_name>
```
