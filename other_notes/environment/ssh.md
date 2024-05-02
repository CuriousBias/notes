# SSH
- Secure SHell
- Cryptographic protocol to securely share data.
- Also used in file transfer tools.
- One of few protocols freely allowed through firewalls!

## SSH Protocol
- Secures connection betwen client and server.
- All authentication, commands, output, and file transfers are encrypted.

### Connection flow
1. Client --> Server: Client initiates the connection by contacting the server.
2. Client <-> Server: **Server authentication** Proof of possession by host (process uses both parties host keys).
2. Client <-> Server: : Negotiate protocol, parameters, algorithm, generate one-time session keys, etc.
3. Client --> Server: **Clien authentication**: Proof of possession by client.

#### Proof of possession (by host)
1. Client sends challenge value to server.
2. Server responds with public key (host_key) and signature of challenge value.
3. Client computes signature to see if they match. This proves server has private key (host_key) to match its public key. 
4. If client has public key stored, then it knows it talked to this host previously.

#### Client authentication
- Client needs to prove they have right to access account.
    1. Proof can be password to account.
    2. Similar proof of possession to check against public key (user_key) stored in "authorized_keys" of server. 

### Processes

#### sshd
- SSH server process
- Usually located at ```/usr/sbin/sshd```
- Starts when system boots
- Listens for incoming connections and handles authentications, encryption, connections, file transfers, and tunneling.

#### ssh
- Used to establish a connection
- Checks both client config files. 1st checks ```.ssh/config```, 2nd checks ```etc/ssh/ssh_config```. Uses 1st value found.
- Uses port 22

#### ssh-agent
- Holds private keys in memory and can use them to authenticate logins

### Implimentations
1. OpenSSH: Server for Unix, Linux
2. PuTTY: Client for windows and linux
3. Many others: 

## SSH keys
- Access credentials for authenticating users
- Similar to username and passwords, but more useful for automated processes and single-sign-on systems. 
- Are cyrptographic keys, but are managed more as authentication credentials. 

### User keys
- Used for authenticating users
1. Authorized keys
    - Is a public key
    - Used to verify digial signature
    - Can be easily derived from private key
2. Identity keys
    - Is a private key
    - Used to sign data

### Host keys
- Similar public/private key combination as User keys
- Used for host authenticating computers.
- Prevent man-in-the-middle attacks.
- Remembered after first login to a host - known host keys stored in ```<user>/.ssh/known_hosts```
- Stored long term means can be compromised. Overall connection is not compromised because session keys kept secret!

### Session keys
- Used to encrypt bulk of data in a connection.
- Negotiated when connection is established.
- Usually consist of encryption algorithm and message authentication code algorithm


## Files
- Unix style on MacOS using OpenSSH
- Each line with # is interpreted as a comment.

### /user/.ssh

#### .ssh/config
- First configuration file for client side

#### .ssh/authorized_keys
- Allows sshd process to authenticate users accessing this system.
- List of public keys which can be used for logging into this system.
- This directory is normal location. However, at companies, this file is usually moved to root-owned locations to prevent self-provisioning by normal users.

#### .ssh/id_*
- Private keys; either id_rsa, id_ecdsa, id_dsa, or id_

#### .ssh/id_*.pub
- Public keys; similar to private keys above. 

#### .ssh/id_*-cert.pub
- 

#### .ssh/known_hosts
- Allows client to authenticate server
- List of known hosts which client can connect to

### /etc/ssh/
- Directory contains this machine's host key pairs. 
- Also contains files below:

#### /etc/ssh/ssh_config
- Second configuration file for client side

#### /etc/ssh/sshd_config
- Configuration file for server side sshd process
- Specifies locations of host_keys and authorized_keys
- Many other settings here

```
PubkeyAuthentication yes  # Allows public key authentication
```

## Setup Features

### Keys

- generates public and private key pair ```ssh-keygen```

### Passwordless login
Settings
1. Allow PubKey authentication on server side
    - In server side /etc/ssh/sshd_config file
    ```
    PubkeyAuthentication yes  # Allows public key authentication
    ```
2. Allow PubKey authenticatin on client side
    - In clinet side /ect/ssh/config or /.ssh/config
    ```
    PubkeyAuthentication yes  # Allows public key authentication
    ``` 

### Root login
Settings
1. Allow root login on server side
    - In server side /etc/ssh/sshd_config file
    ```
    PermitRootLogin yes
    ```

Steps
1. Copy public key from client to server ```ssh-copy-id -i ~.ssh/id_rsa.pub user@host``` 
2. Test install: ```ssh -i ~.ssh/id_rsa.pub user@host```
- Interpret private key to generate public key: ```ssh-keygen -y -e -f .ssh/<private_key>```

### Use

ssh -v <host>
- Verbose, provides more information

### Remove known hosts
1. Delete file (a bit crude): ```rm -f ~/.ssh/known_hosts```
2. Remove individual host keys: ```ssh-keygen -R <host>```

### Root login
- Seperate privilaged access.
- May need to run sudo anyways after login to execute commands


SSH PubkeyAuthentication MacOS -> Windows
Configure for password-less access
authorized_keys or administrator_authorized_keys
create new files: 
C:\ProgramData\ssh> New-Item administrators_authorized_keys
PS C:\Users\user\ssh> New-Item authorized_keys.