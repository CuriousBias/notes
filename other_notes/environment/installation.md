# Installation

## Simple Method
Single version of python without package manager

1. Install python from https://www.python.org
2. Find which python was installed) `% ls -l /usr/local/bin/python*`
3. Remap python3 to python `% sudo ln -s -f /usr/local/bin/python3.8 /usr/local/bin/python`
4. Check PATH `% python --version`
5. Update pip `% pip install --upgrade pip`
6. Install packages as necessary
```terminal
pip install numpy
pip install scipy
pip install matplotlib
pip install jupytherlab
```

## Leet Method
Uses package manager Homebrew https://brew.sh
- browse brew site for info about what is available to install
- Can also look up which version is latest in homebrew formulae

1. Install Xcode from App store https://developer.apple.com/xcode/
2. Add command line tools `% Xcode-select --install`
3. Install homebrew https://brew.sh/#install
    `% /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
4. Add Homebrew to your PATH. Seems like brew gets added to path automatically now.
    ` % echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/kurt/.zprofile`
    ` % eval $(/opt/homebrew/bin/brew shellenv)`
5. Test brew install
` % brew help 
    % brew analytics off
    % brew doctor
    % brew cleanup
`
6. Install desired version of python. `% brew install python@3.10`
7. Add symlinks for python 
    - Seems to be done automatically now. 
    - This adds to PATH through ~/.zshrc file (sourced when starting terminal) 
    - Double check that directory for libexec is correct (this one has the symlinks)!
    - on M1 MacOS
    ` % echo 'export PATH="/opt/homebrew/opt/python@3.10/libexec/bin:$PATH"' >> ~/.zshrc`
    - on Intel MacOS
        - python & pip @ /usr/local/bin/python3
        - symlinks @ /usr/local/opt/python@3.9.libexec/bin

7. Close Terminal and reopen to check if successful
        `% python --version`
        `% pip --version`
8. Upgrade git `% brew upgrade git`
    - This will install a new version of git connected to homebrew and add symlinks to make it default. 

9. Install IDE `% brew install --cask visual-studio-code`

## Dependency location
1. Global
    - Go to pip.md

2. Virtual environment (multiple options)
    - better option if you are managing multiple projects.
    - different projects may require different versions of the same dependency. 
    a. venv
        - defualt
        - install dependencies with pip via requirements.txt
    b. pipenv
        - installed seperately `% python -m pip install pipenv`
        - dependencies managed in Pipfile
        - go to virtual_environments.md
    c. virtualenv
        - another option
