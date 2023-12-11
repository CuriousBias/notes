# Pip
- python package install via PPI (python package index)
- Included with installation of python (each python version will get its own pip)
- Check current version `% pip --version`

## Simple
this intalls via default pip. Can be pip2 or pip3
`% pip install <package>`

Browse published packages: https://pypi.org

## Explicit
Example below assumes python install via homebrew

`% /opt/homebrew/opt/python/libexec/bin/python -m pip install jupyter notebook`

This installs jupyter notebook via pip version associate with python installed at that directory

### From requirements.txt
`% python -m pip install -r Documents/github/Notes/environment/requirements.txt`

## Maintenance
1. Update pip `% python -m pip install --upgrade pip`
2. Update setup tools and wheel `% python -m pip install --upgrade setuptools wheel`
3. Or just use homebrew `% brew update`
    - This will keep everything upto date

## Random

### Uninstall
Uinstall all pip packages
`% pip freeze | xargs pip uninstall -y`
`% pip cache purge`
