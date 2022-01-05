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

    a. Check 'Set hostname', enter desired hostname for your pi

    b. Check 'Enable SSH', enter desired password for accessing your pi

    c. Check 'Configure wifi', enter SSID and Password, select country, save

    d. Select Write

### Pi setup Method 2: Terminal

1. Download image and rename to 'raspioslite.img' (or aything short) https://www.raspberrypi.com/software/operating-systems/

2. View list of drives and note directory of SD card (Example: '/dev/disk4')

        foo@bar ~ % diskutil list

3. Format SD Card to FAT32 and unmount

        foo@bar ~ %diskutil eraseDisk FAT32 NONAME /dev/disk4
        foo@bar ~ % diskutil unmountDisk /dev/disk4

4. Write OS image to SD card (after entering password, wait a while)

        foo@bar ~ % sudo dd bs=1m if=Downloads/raspioslite.img of=/dev/disk4'

    This results in SD card renamed to 'boot'

    - if 'not permitted', need to enable terminal disk utility privlidges

        System Preferences > Security & Privacy > Full Disk Access > Unlock > select Terminal, then restart terminal


5. Create ssh file

        foo@bar ~ % touch /Volumes/boot/ssh

6. Create file to trigger avahi-daemon (allows usb tethering for ssh)

        foo@bar ~ % touch /Volumes/boot/avahi

7. Edit ```config.txt``` to enable dwc2

        foo@bar ~ % cd /Volumes/boot
        foo@bar boot % echo dtoverlay=dwc2 >> config.txt

8. Edit ```cmdline.txt```

        foo@bar boot % open -a "TextEdit" cmdline.txt'

    - insert 'modules-load=dwc2,g_ether' after "rootwait" (make sure to leave only one space after rootwait and one space after the inserted text)
    - save the file

9. Create network info file

        foo@bar ~ % touch /Volumes/boot/wpa_supplicant.conf
        foo@bar ~ % open -a "TextEdit" /Volumes/boot/wpa_supplicant.conf

10. Copy info to wpa_supplicant.conf (adjust country code, ssid, psk)

        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1
        country=<Country Code>

        network={
            ssid="<SSID>"
            psk="<PASSWORD>"
            scan_ssid=1
        }

    Save and close file. 

11. Eject SD card
    foo@bar ~ % diskutil eject /dev/disk4

12. Boot raspberry pi
    a. Input SD card to raspberry pi
    b. Plug in usb micro cable to usb port on raspberry pi (not power)
    c. Plug in usb cable to computer
    d. Allow Raspberry pi to boot up (~90 seconds)

13. Establish SSH connection

        default username: pi
        default hostname: raspberrypi
        default password: raspberry

        foo@bar ~ % ssh-keygen -R raspberrypi.local (not sure this is required)

        foo@bar ~ % ssh <username>@<hostname>.local

    Example

        foo@bar ~ % ssh pi@raspberrypi.local

    If "WARNING: POSSIBLE DNS SPOOFING DETECTED!"

        foo@bar ~ % rm -f /User/<username>/.ssh/known_hosts

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

    a. Disable avahi (this failed?)

        pi@raspberrypi:~ $ systemctl disable avahi-daemon (permission denied?)

    b.  Keep raspberry pi from going to sleep

        pi@raspberrypi:~ % sudo /sbin/iw wlan0 set power_save off
        pi@raspberrypi:~ % iwconfig (confirm 'Power Management:off')

        pi@raspberrypi:~ % sudo nano /etc/rc.local

    copy info to just above "exit0" in rc.local

        pi@raspberrypi:~ $ sudo /sbin/iw wlan0 set power_save off

    save file and exit (control+x, y, return)

    c. Reboot

        pi@raspberrypi:~ $ sudo reboot now

### Install Pi-hole

1. Establish ssh (root not necessary, root ssh worked on one, but not another)

        foo@bar ~ % ssh root@raspberrypi.local

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

        pi@raspberrypi:~ $ shutdown now

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

    a. http://192.168.86.10/admin/

    b. Select Login and enter password

    c. Under Settings > DHCP

    - Select 'DHCP server enabled'

    - Under "Range of IP addresses to handout", select a suitable range (.10 - .251)

    - Save changes

    d. Restart Google router Wifi > Setting cog > restart network

    e. To login with web interface password: http://pi.hole/admin

4. Add lists to block 

    a. Lists to block can be found here: https://firebog.net

    b. Login to web interface with web interface

    c. Group Management > Adlist

    d. Copy and paste as many urls into "Address" 

    e. Update gravity list to implement changes (link under "Addresses")
