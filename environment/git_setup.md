# Git setup
Git should be installed by homebrew
But if you need to install manually: https://git-scm.com/download/
Current passphrase: "partha"

## SSH vs HTTPS

### SSH
- Store private key on local machine to login
- Considered more secure

#### SSH key setup
1. Check version ```% git --version```
2. Set up username and email (good idea, not sure why I have gotten away without it)
```
    % git config --global user.name "Kurt"
    % git config --global user.email "kurt.partha@gmail.com"
```
3. Check ```% git config --global --list```
4. Set up SSH key
    1. Check for ssh key ```% ls -al ~/.ssh```
    2. if not (~./ssh doesn't exist) -> generate new key (in terminal) ```% ssh-keygen -t rsa -b 4096 -C "kurt.partha@gmail.com"```
    3. press enter to select default file location
    4. enter passphrase "partha"
    5. Check config ```% open ~/.ssh/config```
    6. if not (The file /Users/you/.ssh/config does not exist) 
        ```% touch ~/.ssh/config``` # create the file
        ```% ssh-add -K ~/.ssh/id_rsa``` # add key to agent

5. copy ssh key to github account (Copies the contents of the id_rsa.pub file to your clipboard) ```% pbcopy < ~/.ssh/id_rsa.pub```

6. Login to github > settings > SSH and GPG Keys > New/Add SSH key > paste key > "add" > confirm git hub password

7. Test your key ```% ssh -T git@github.com # Attempts to ssh to GitHub```

#### Clone via SSH

To clone repo (get link from github Code > SSH > Copy) ```% git clone <ssh_repo_link>```

### HTTPS 
- (Personal Access Token or just Token)
- Unique to git
- Has advantage of having limited scope. 

#### Token setup
- Generate **Personal Access Tokens** on github.com and then use as password to push changes to master
- Tokens generated Github.com > Settings > Developer Settings > Personal Access Tokens > Generate New Token > Input info: Then use token as password
