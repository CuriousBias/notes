# PiHole

## Setup guide for headless install

### Required equipment
- Raspberry Pi Zero W or Pi Zero 2 W
- Micro-USB power supply
- Micro SDHC card (minimum 8 GB, class 10 recommended)
- Micro SDHC card -> computer cable
- Micro-USB -> computer cable
- Google wifi

### Pi setup Method 1: Raspberry Pi Imager

1. Download 'Raspberry Pi Imager' https://www.raspberrypi.com/software/

2. Select Raspberry Pi OS Lite

3. Select SD card

4. Enter hidden menu (command+shift+x)

    a. Check 'Set hostname', enter desired hostname

    b. Check 'Enable SSH' with password authentication, enter desired username and password

    c. Check 'Configure wireless LAN', enter SSID and Password, select country, save

    d. Select Write

### Pi setup Method 2: Terminal (Not working anymore)

1. Download image and rename to 'raspioslite.img' (or aything short) https://www.raspberrypi.com/software/operating-systems/

2. View list of drives and note directory of SD card (Example: '/dev/disk4')

        user@host ~ % diskutil list

3. Format SD Card to FAT32 and unmount

        user@host ~ %diskutil eraseDisk FAT32 NONAME /dev/disk4
        user@host ~ % diskutil unmountDisk /dev/disk4

4. Write OS image to SD card (after entering password, wait a while)

        user@host ~ % sudo dd bs=1m if=Downloads/raspioslite.img of=/dev/disk4'

    This results in SD card renamed to 'boot'

    - if 'not permitted', need to enable terminal disk utility privlidges

        System Preferences > Security & Privacy > Full Disk Access > Unlock > select Terminal, then restart terminal


5. Create ssh file

        user@host ~ % touch /Volumes/boot/ssh

6. Create file to trigger avahi-daemon (allows usb tethering for ssh)

        user@host ~ % touch /Volumes/boot/avahi

7. Edit ```config.txt``` to enable dwc2

        user@host ~ % cd /Volumes/boot
        user@host boot % echo dtoverlay=dwc2 >> config.txt

8. Edit ```cmdline.txt```

        user@host boot % open -a "TextEdit" cmdline.txt'

    - insert 'modules-load=dwc2,g_ether' after "rootwait" (make sure to leave only one space after rootwait and one space after the inserted text)
    - save the file

9. Create network info file

        user@host ~ % touch /Volumes/boot/wpa_supplicant.conf
        user@host ~ % open -a "TextEdit" /Volumes/boot/wpa_supplicant.conf

10. Copy info to wpa_supplicant.conf (adjust country code, ssid, psk)

        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1
        country=<us>

        network={
            ssid="<SSID>"
            psk="<PASSWORD>"
            scan_ssid=1
        }

    Save and close file. 

11. Eject SD card
    user@host ~ % diskutil eject /dev/disk4

12. Boot raspberry pi
    a. Input SD card to raspberry pi
    b. Plug in usb micro cable to usb port on raspberry pi (not power)
    c. Plug in usb cable to computer
    d. Allow Raspberry pi to boot up (~90 seconds)

13. Establish SSH connection

        default username: pi
        default hostname: raspberrypi
        default password: raspberry

        user@host ~ % ssh-keygen -R raspberrypi.local (not sure this is required)

        user@host ~ % ssh <username>@<hostname>.local

    Example

        user@host ~ % ssh pi@raspberrypi.local

    If "WARNING: POSSIBLE DNS SPOOFING DETECTED!"

        user@host ~ % rm -f /User/<username>/.ssh/known_hosts

    Should see SSH enabled...
        pi@raspberrypi:~ $ 

14. Change hostname and password

    a. Enter pi configuration

        pi@raspberrypi:~ $ sudo raspi-config

    b. Change password: System Options>S3 Password

    e. Change hostname: System Options>S4 Hostname

    g. Expand file system: Advanced options>Expand filesystem

    f. Reboot: Finish>Yes

### Pi configuration

1. Update raspberry pi
    a. Reestablish ssh connection

    b. Update and upgrade (these take a while)

        pi@raspberrypi:~ $ sudo apt-get update -y
        pi@raspberrypi:~ $ sudo apt-get upgrade -y
        pi@raspberrypi:~ $ sudo apt-get dist-upgrade -y

2. Other necessary pi settings

    a.  Keep raspberry pi from going to sleep

        pi@raspberrypi:~ % sudo /sbin/iw wlan0 set power_save off
        pi@raspberrypi:~ % iwconfig (confirm 'Power Management:off')

        pi@raspberrypi:~ % sudo nano /etc/rc.local

    copy info to just above "exit0" in rc.local (this ensures power_save is set to off on startup!)

        sudo /sbin/iw wlan0 set power_save off

    save file and exit (control+x, y, return)

    b. Reboot

        pi@raspberrypi:~ $ sudo reboot now

### Install Pi-hole

1. Establish ssh (root not necessary, root ssh worked on one, but not another)

        user@host ~ % ssh root@raspberrypi.local

2. Check wlan0 connection

        pi@raspberrypi:~ $ ifconfig wlan0

    Should see IP address listed inet. Also can just check devices connected to router. 

2. Install Pi-hole

    a. Install via curl

        pi@raspberrypi:~ $ curl -sSL https://install.pi-hole.net | sudo bash

    b. Network add block: Ok

    c. Pihole is free, but... : Ok

    d. Pihole is a SERVER, so its needs static IP... : Yes

    e. Select set manual values... : Input desired IP: 192.168.86.10 (example)

    f. Entered desired IPv4 address: 192.168.86.10/24 (matching above example)

    g. Enter your desired IPv4 default gateway: 192.168.86.1 (example)

    h. Are these settings correct... : confirm they are accurate

    i. Select upstream DNS provider: cloudflare

    j. Pi-hole relies on third party lists...: select StevenBlack or whatever is default

    k. Web admin interface: (*) On

    l. Web server: (*) On

    m. Log Queries: (*) On

    n. Privacy mode for FTL: (*) 0 Show Everything

    o. ****SAVE WEB INTERFACE PASSWORD**** (displayed after install)

    p. Shutdown raspberry pi

        pi@raspberrypi:~ $ sudo shutdown now

    q. Disconnect from computer and plug into power supply.


### Google router config

1. Launch Google home app

2. Assign raspberry pi a static IP address

    Wifi > Setting cog > Advanced Networking > DHCP IP Resrevations > Add > pick number and save

    Example: 192.168.86.10 (match IPv4 set during Pi-hole install)

2. Configure router

    Wifi > Setting cog > Advanced Networking > LAN Settings > DHCP Pool

    Set both Start and End to : 192.168.86.10 (match IPv4 set above)

3. Configure Pi-hole web interface

    a. http://pi.hole/admin or http://192.168.1.10/admin/ (address depends on IP!)

    b. Select Login and enter password

    c. Under Settings > DHCP

    - Select 'DHCP server enabled'

    - Under "Range of IP addresses to handout", select a suitable range (.10 - .251)

    - Save changes

    d. Restart Google router Wifi > Setting cog > restart network


### Access Web Interface

1. http://pi.hole/admin or http://192.168.1.10/admin/ (address depends on IP!)

    b. Select Login and enter password

2. Add lists to block 

    a. Lists to block can be found here: https://firebog.net

    b. Login to web interface with web interface

    c. Group Management > Adlist

    d. Copy and paste as many urls into "Address" 

    e. Update gravity list to implement changes. Sidebar > Tools > Upgrate Gravity > Upgrade

### Establish SSH connection (to update)

1. ssh: `% ssh <username>@<hostname>.local`

    a. ex: `ssh pi@ranchpi.local` or `ssh root@ranchpi.local`

    b. This login needs to be confirmed. Either using incorrect password or incorrect username or hostname.