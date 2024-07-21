# Homebrew

Package manager for MacOS

https://brew.sh

See link for latest install instructions
See installation.ipynb for installation process

## Common commands
- List all commands  `brew commands`

#### Help
- See verion  `brew --version`
- Get some help  `brew help`
- Get info about a specific command  `brew help <command>`
- See any problems  `brew doctor`

#### Updating
- Update homebrew  `brew update`
- Show any possible updates  `brew outdated`
- Update all outdated  `brew upgrade`
- Update only a specific  `brew upgrade <formula>`

#### Formula (Packages)
- See possible formula  `brew search <name>` ex: `brew search python`
- Install  `brew install <formula>` ex: `brew install git`
- Uninstall  `brew uninstall <formula>`
- See info `brew info <formula>`
- Open homepage `brew home <formula>`

#### Casks (GUI applications)
- See installed applications  `brew list --cask`
- Install a program `brew install --cask <application>`
    ex: `brew install --cask visual-studio-code`
- See info about applications `brew info visual-studio-code`

#### Versions
- Keep a specific formalae from being updated  `brew pin <formula>`
- Reverse above  `brew unpin <formula>`
- Switch to different version `brew switch <formula version>`

#### Repositories
- List current repositories  `brew tap`
- Tap a formula repository from github for tap  `brew tap <user/repo>`
- Tap a formula repository from a specific URL  `brew tap <user/repo/><URL>`
- Remove a tap  `brew untap <user/repo>`

## Locations
Locations vary among hardware

#### MacOS with M1 Silicon
1. Applications are installed to `cd /opt/homebrew/Cellar`
2. Cask applications are installed to `cd /opt/homebrew/Caskroom`

#### MacOS with Intel
1. Applications are installed to `cd /usr/local/Cellar`
2. Cask applications are installed to `cd /usr/local/Caskroom`

## Symlinks
Symlinks seem to be added automatically now. 

## Repositories
- Repos you want homebrew to track (install and update)

TODO: Installing vs cloning a repository