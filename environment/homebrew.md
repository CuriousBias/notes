# Homebrew

Package manager for MacOS

https://brew.sh

See link for latest install instructions
See installation.ipynb for installation process

## Common commands
- List all commands  ```% brew commands```

#### Help
- See verion  ```% brew --version```
- Get some help  ```% brew help```
- Get info about a specific command  ```% brew help <command>```
- See any problems  ```% brew doctor```

#### Updating
- Update homebrew  ```% brew update```
- Show any possible updates  ```% brew outdated```
- Update all outdated  ```% brew upgrade```
- Update only a specific  ```% brew upgrade <formula>```

#### Applications
- See possible formula  ```% brew search <name>```
    ex: brew search python
- Install an application  ```% brew install <formula>```
    ex: ```% brew install git```
- See info of an application ```% brew info <formula>```
- Open homepage ```% brew home <formula>```

#### Installing GUI applications (Cask)
- See installed applications  ```% brew list --cask```
- Install a program ```% brew install --cask <application>```
    ex: ```% brew install --cask visual-studio-code```
- See info about applications ```% brew info visual-studio-code```

#### Versions
- Keep a specific formalae from being updated  ```% brew pin <formula>```
- Reverse above  ```% brew unpin <formula>```
- Switch to different version ```% brew switch <formula version>```

#### Repositories (but which repos are these?)
- List current repositories  ```% brew tap```
- Tap a formula repository from github for tap  ```% brew tap <user/repo>```
- Tap a formula repository from a specific URL  ```% brew tap <user/repo/><URL>```
- Remove a tap  ```% brew untap <user/repo>```

