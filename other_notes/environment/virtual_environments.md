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

## pipenv
- Lets you set dependencies and lock them
- Uses pip and virtualenv under the hood.
- ***No need to use `pip` commands when using `pipenv`***

### Files

#### Pipfile
- meant to replace `requirements.txt`

#### Pipfile.lock
- 

### Installation
- Install pipenv `% python -m pip install pipenv`

### Usage

#### Environment Control
- Create ***Pipenv*** and ***Pipenv.lock*** files: `% pipenv install`
- Activate existing environment or create(if does not exit) `% pipenv shell`
- Exit environment: `% exit`
- Delete environemnt: `% pipenv --rm`
- Locate environment `% pipenv -venv`

#### Dependencies
- Install dependencies (will also add to pipfile): `% pipenv install numpy`
- Install dependencies and add to dev flag of pipfile: `%p pipenv install pylint -dev`
- Install many: `% pipenv install -r <dir>/requirements.txt`
- Uninstall dependency: `pipenv uninstall numpy`
- Update all packages `% pipenv uninstall -all`
- Lock dependencies (usually done before pushing code): `% pipevn lock -r`
- 

#### Extras
- Check security `% pipenv check`
- List packages and their dependencies `% pipenev graph`

