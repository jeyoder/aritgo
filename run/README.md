

===== SSH Key Access =====
1. Edit hosts file and append snapdragon's ip
```
sudo vim /etc/hosts
$SNAPDRAGON_IP        snapdragon
```

2. Generate an RSA key pair
```
 ssh-keygen -t rsa
```

3. Copy the public key
```
ssh-copy-id root@$SNAPDRAGON_IP 
```

4. Make sure you can ssh to root on snapdragon. Must edit the /etc/ssh/sshd_config file: change PermitRootLogin to yes
5. Make sure root has password: sudo passwd root
5. Make sure ssh with host key algorithm: https://answers.ros.org/question/244060/roslaunch-ssh-known_host-errors-cannot-launch-remote-nodes/
