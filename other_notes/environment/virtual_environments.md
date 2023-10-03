# Virtual environments
Used to manage dependencies on multiple projects

continue...
https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref

continue ...
https://realpython.com/python-virtual-environments-a-primer/


## venv
- Most basic python virtual environments
- Added with python install by default

#### venv commands
1. Create virtual environment  `% python -m venv test_env`
2. Activate the environment `% source test_env/bin/activate`
3. Install whichever packages you want `% pip install <package>`
4. Install packages from environment `% python -m install -r <dir>/requirements.txt`
5. Run code `% python ./Documents/test.py`
6. Exit environment ` % deactivate`


## Virtualenv
- Build ontop of venv
- Adds more functionality

### Basic commands
- install: `pip install virtualenv`
- create a new virtual environment: `virtualenv venv`
- This will create new environment with python version on path in your current directory.
- Places copy of python and virtual environment in current_dir/venv
- to step into and use: `source venv/bin/activate`
- install packages inside: `pip install numpy`
- Install from requirements file: `pip install -r requirements.txt`
- exit environment: `deactivate`
- Save currently install packages in environment: `pip freeze > requirements.txt`
- delete environment: `sudo rm -rf venv

### Workflow
1. enter: `source venv/bin/activate` or `venv\Scripts\activate` (for windows)
2. install: `pip install -r requirements.txt`
3. leave: `deactivate`
