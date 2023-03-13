# Terminal

zsh default (short for Z shell)

## Python in terminal

### Run python files from terminal

run the test.py file located in Documents  ```% python ./Documents/test.py```

Or enter python interactive shell  ```% python```

And then run test.py

```python
exec(open("./Documents/test.py").read())
```

## PATH

### Modify default terminal paths: ***NOT*** recommended

1. Locate current default paths list  ```% sudo nano /etc/paths```
2. Enter password
```text
        /usr/local/bin
        /usr/bin
        /bin
        /usr/sbin
        /sbin
```
3. paste any path you want added to default terminal here

4. Quit out and save changes: ```^ + X, Y```

### Symbolic links

#### Add to PATH
Add location for terminal to check if application exists
To see all python links  ```% ls -la /usr/local/bin | grep python```

1. .profile (??)
2. .zprofile (sourced on login)
3. .zshrc (sourced when opening terminal)

##### Add to .zprofile
1. Open .zprofile  ```% open ~ /.zprofile```
2. Add: eval "$(/opt/homebrew/bin/brew shellenv)"
3. cmd + save, exit

##### Add to .zprofile
1. Open .zprofile  ```% open ~ /.zprofile```
2. Add: export PATH="/opt/homebrew/opt/python/libexec/bin:$PATH"
3. cmd + save, exit

##### To restart terminal
1. Re source files ```% source ~/.zshrc```



#### full absolute path

```python
import os

dir = os.path.dirname(__file__)  # directory of current .py file
dbc = os.path.join(dir, 'file.txt')
```