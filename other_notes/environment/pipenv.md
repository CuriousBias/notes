## pipenv
- Lets you set dependencies and lock them
- Uses pip and virtualenv under the hood.
- ***No need to use `pip` commands when using `pipenv`***

### Files

#### Pipfile
- Meant to replace `requirements.txt`
- Inlcudes section for regular packages and another for dev packages.
- Uses TOML syntax
- Use any version: `numpy = "*"`
- Use specific version: `numpy = "1.14.1"

#### Pipfile.lock
- Shold not edit manually.
- Edit via `% pipevn lock`

### Installation
- Install pipenv `% python -m pip install pipenv`

### Usage

#### Environment Control
- Create ***Pipenv*** and ***Pipenv.lock*** files: `% pipenv install`
- Activate existing environment or create(if does not exit) `% pipenv shell`
- Exit environment: `% exit`
- Delete environemnt: `% pipenv --rm`
- Locate environment `% pipenv --venv`

#### Dependencies
- Install package (will also add to pipfile): `% pipenv install numpy`
- Install package and add to dev flag of pipfile (if only needed for development): `%p pipenv install pylint --dev`
- Install all regular packages in pipfile: `% pipenv install`
- Install all regular packages + dev packages: `% pipenv install --dev`
- Install many: `% pipenv install -r <dir>/requirements.txt`
- Uninstall dependency: `pipenv uninstall numpy`
- Update all packages `% pipenv uninstall -all`
- Lock dependencies (usually done before pushing code): `% pipevn lock -r`

#### Extras
- Check security `% pipenv check`
- List packages and their dependencies `% pipenev graph`

### Workflow
1. Put minium requirements in setup.py under "install requires" instead of directly with `pipenv install `
2. Use `pipenv install '-e.` to install packages as editable. 
3. Use `pipenv lock` to make reproducible environment.


