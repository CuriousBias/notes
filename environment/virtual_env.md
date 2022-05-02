# Virtual environments
Used to manage dependencies on multiple projects
https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref

## venv
added with python install by default

#### venv commands
1. Create virtual environment  ```% python -m venv test_env```
2. Activate the environment ```% source test_env/bin/activate```
3. Install whichever packages you want ```% pip install <package>```
4. Install packages from environment ```% python -m install -r <dir>/requirements.txt```
5. Run code ```% python ./Documents/test.py```
6. Exit environment ``` % deactivate```

## pipenv
- More involved
- Lets you set dependencies and lock them
- Setup Pipfile and run it. 

1. Install pipenv ```% python -m pip install pipenv```
2. First time run ```% pipenv install```
        This will create ***Pipenv*** and ***Pipenv.lock***
        ***Pipenv***
3. Activate already created environment ```% pipenv shell```
4. Install dependencies ```% pipenv install <package>```
5. Install many ```% pipenv install -r <dir>/requirements.txt```
6. Check security ```% pipenv check```
7. Check dependencies ```% pipenev graph```
8. Setup script
        a. Add script to run to Pipfile by opening Pipfile and manually editing? 
        b. Save changes
9. Lock dependencies ```% pipevn lock -r```
10. Execute ```% pipenev run server```
