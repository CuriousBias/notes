# Networking

ping -c 20 www.google.com

## Network Config

### IP Address
- Address of device
- Common: 192.168.1.100

### SubNet mask
- Determines # of hosts on network
- Common: 255.255.255.0 (allows 254 hosts)
- Common: 255.255.0.0 (allows 65,534 hosts)

### Gateway
- Usually ends in .1 or .254 in the subnet
- Must be within the same subnet as your other devices
- Most common for home/small office: 192.168.1.1 or 192.168.0.1

#### CIDR (Classless Inter-Domain Routing)
