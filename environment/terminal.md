# Terminal

zsh default (short for Z shell)

### Navigating

- lists folders in current directory  ```% ls``` 
- lists all folders in directory as a list  ```% ls -l```
- lists all hidden folders and files as well ```% ls -a```
- do both above ```% ls -la```
- change to specific directory ```% cd Downloads```
- navigate to roo directory ```% cd ~```
- go back up one level ```% cd ..```
- to open files  ```% open <file>```

#### Vim text editor

- to make edits: enter insert mode with ```i```
- return to command mode with: "esc"
- to abandon changes and exit (Quit and Abandon) ```:qa! + enter ```
- to save changes (Write and Quit) ```:wq! + enter```

#### Root access
1. For root access  ```% sudo -i```
2. To leave root  ```% root# exit```

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

To see all python links  ```% ls -la /usr/local/bin | grep python```

1. .zprofile (sourced on login)
2. .zshrc (sourced when opening terminal)

##### Add to .zprofile
1. Open .zprofile  ```% open ~ /.zprofile```
2. Add: eval "$(/opt/homebrew/bin/brew shellenv)"
3. cmd + save, exit

##### Add to .zprofile
1. Open .zprofile  ```% open ~ /.zprofile```
2. Add: export PATH="/opt/homebrew/opt/python/libexec/bin:$PATH"
3. cmd + save, exit

## Python in terminal

#### run python files from terminal

run the test.py file located in Documents  ```% python ./Documents/test.py```

Or enter python interactive shell  ```% python```

And then run test.py

```python
exec(open("./Documents/test.py").read())
```

#### full absolute path

```python
import os

dir = os.path.dirname(__file__)  # directory of current .py file
dbc = os.path.join(dir, 'file.txt')
```