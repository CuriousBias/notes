# PiHole

## Setup guide for headless install using using ```Terminal```

### Required equipment
 - Raspberry Pi Zero W or Pi Zero 2 W
 - Power supply
 - Micro SDHC card (minimum 8 GB, class 10 recommended)

 ### 1. Install Raspberry Pi OS Lite

1. Download image and rename to 'raspioslite.img' (or aything short)

    https://www.raspberrypi.com/software/operating-systems/

2. View list of drives and note directory of SD card Ex: '/dev/disk4'

        foo@bar ~ % diskutil list

3. Format SD Card to FAT32 and unmount

        foo@bar ~ %diskutil eraseDisk FAT32 NONAME /dev/disk4
        foo@bar ~ % diskutil unmountDisk /dev/disk4

4. Write OS image to SD card (after entering password, wait a while)

        foo@bar ~ % sudo dd bs=1m if=Downloads/raspioslite.img of=/dev/disk4'

    This results in SD card renamed to 'boot'

    - if 'not permitted', need to enable terminal disk utility privlidges

        System Preferences > Security & Privacy > Full Disk Access > Unlock > select Terminal, then restart terminal

### Enable ssh and wifi connect files

1. Create ssh file

        foo@bar ~ % touch /Volumes/boot/ssh

2. Create file to trigger avahi-daemon (allows usb tethering for ssh)

        foo@bar ~ % touch /Volumes/boot/avahi

3. Edit ```config.txt``` to enable dwc2

        foo@bar ~ % cd /Volumes/boot
        foo@bar boot % echo dtoverlay=dwc2 >> config.txt

4. Edit ```cmdline.txt```

        foo@bar boot % open -a "TextEdit" cmdline.txt'

    - insert 'modules-load=dwc2,g_ether' after "rootwait" (make sure to leave only one space after rootwait and one space after the inserted text)
    - save the file

5. Create network info file

    foo@bar ~ % touch /Volumes/boot/wpa_supplicant.conf
    foo@bar ~ % open -a "TextEdit" /Volumes/boot/wpa_supplicant.conf

6. Copy info to wpa_supplicant.conf (adjust country code, ssid, psk)

        country=US
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1

        network={
            ssid="NETWORK-NAME"
            psk="NETWORK-PASSWORD"
        }

7. Eject SD card
    foo@bar ~ % diskutil eject /dev/disk4

### Boot up 

3. Boot raspberry pi
    a. Input SD card to raspberry pi
    b. Plug in usb micro cable to usb port on raspberry pi (not power)
    c. Plug in usb cable to computer
    d. Allow Raspberry pi to boot up (~90 seconds)
    e. Check connection
        Settings > Network > ?

4. Login over USB
    'ssh-keygen -R raspberrypi.local'
    'ssh pi@raspberrypi.local'

    default hostname: pi
    default password: raspberry

    - Should see SSH enabled...
        pi@raspberrypi:~ $ 

5. Change hostname and password
    a. Enter pi configuration: 'sudo raspi-config'
    b. Select '1 System Options'
    c. Select 'S3 Password'
    d. Input new password: peterpan89
    e. Select 'S4 Hostname'
    f. Input new hostname: mypi-hole
    g. Expand file system
        Select 'Advanced options'
        Select 'Expand file system'
    f. Select 'Finish' at bottom
    g. Select 'Yes' when asked to reboot

6. Update raspberry pi
    a. Reestablish ssh connection
        'ssh pi@mypi.local'
    b. Update and upgrade (these take a while)
        'sudo apt-get update -y'
        'sudo apt-get upgrade -y'
        'sudo apt-get dist-upgrade -y'
    c. Disable avahi
        'systemctl disable avahi-daemon' (this failed?)

10. Keep raspberry pi from going to sleep
    a. 'iwconfig' (to see power management setting)
    b. 'sudo /sbin/iw wlan0 set power_save off' (turns off power management)
    c. Make sure it runs everytime on reboot
        'sudo nano /etc/rc.local'
        - input 'sudo /sbin/iw wlan0 set power_save off' above exit0 line (scroll down)
        - save file and exit: ^X, Y, Enter

11. Assign raspberry pi a static IP address
    - Google home app: Wifi > Setting cog > Advanced Networking > DHCP IP Resrevations > Add > pick number and save
    - 192.168.86.69

12. Install pi-hole
    a. ssh pi@mypi-hole.local
    b. curl -sSL https://install.pi-hole.net | bash
    c. Follow prompts:
        Input static IPv4 when prompted
        Confirm gateway 192.168.86.1
        Confirm settings are correct
        Admin install interface: yes
        Install web server: yes
        Log queries: yes
        Privacy mode: Show everything
        
    d. Settings: ...
    e. Save web interface password: rVncCBM0
    f. Check setup at web interface
        - http://192.168.86.69/admin/



13. Configure router
    a. Google home app: Wifi > Setting cog > Advanced Networking > LAN Settings > DHCP Pool
        - Set both Start and End to : 192.168.86.69

    b. Go back to pi-hole web interface dashboard
    c. Under Settings > DHCP
        - Select "DHCP server enabled"
        - Under "Range of IP addresses to handout", select a suitable range (.70 - .251)
        - Save changes
    d. Restart Google router Wifi > Setting cog > restart network
    e. http://pi.hole/admin
