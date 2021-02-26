IMPORTANT

1) The following line needs to be added to crontab, with the command sudo crontab -e

@reboot sh /home/pi/pishutdown/pishutdown.sh >/home/pi/pishutdown/logs/cronlog 2>&1


2) The following lines must be added to /boot/config.txt

gpio=5=op,dh
gpio=6=ip

