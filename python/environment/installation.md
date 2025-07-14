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
1. Install homebrew
2. Install desired version of python. `% brew install python@3.10`
3. Add symlinks for python 
    - Seems to be done automatically now. 
    - This adds to PATH through ~/.zshrc file (sourced when starting terminal) 
    - Double check that directory for libexec is correct (this one has the symlinks)!
    - on M1 MacOS
    ` % echo 'export PATH="/opt/homebrew/opt/python@3.10/libexec/bin:$PATH"' >> ~/.zshrc`
    - on Intel MacOS
        - python & pip @ /usr/local/bin/python3
        - symlinks @ /usr/local/opt/python@3.9.libexec/bin

4. Close Terminal and reopen to check if successful
        `% python --version`
        `% pip --version`
5. Upgrade git `% brew upgrade git`
    - This will install a new version of git connected to homebrew and add symlinks to make it default. 

6. Install IDE `% brew install --cask visual-studio-code`

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
