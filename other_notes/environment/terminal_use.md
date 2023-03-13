# Terminal Use

## Root access
1. For root access  ```% sudo -i```
2. To leave root  ```% root```

## Navigation
- lists folders in current directory  ```% ls``` 
- lists all folders in directory as a list  ```% ls -l```
- lists all hidden folders and files as well ```% ls -a```
- do both above ```% ls -la```
- change to specific directory ```% cd Downloads```
- navigate to roo directory ```% cd ~```
- go back up one level ```% cd ..```
- clear all output ```clear```

## Commands

### Files and directories
- create a file ```% touch file.txt```
- open file in default ```% open file.txt```
- open in sublime text ```% subl file.txt```
- delete a file ```% rm file.txt```
- delete a directory ```% rm -r /path/to/delete```
- move directory or file and rename ```% mv old/path/old_name.py new/path/new_name.py```
- output file ```cat <file>```

## Random Tidbits

### Vim text editor
- to make edits: enter insert mode with ```i```
- return to command mode with: "esc"
- to abandon changes and exit (Quit and Abandon) ```:qa! + enter ```
- to save changes (Write and Quit) ```:wq! + enter```

### Keyboard interrupt
- Used to interrupt python script  "command" + "c"
- Works by raising an exception in the next line of code
        - Does not work if script is stuck on one line and does not proceed. 

### Stuck terminal
- Closing terminal not a good idea if editing a file. Will save partially edited file and cause problems. 
- Useful if script is stuck. 
- Restarting computer should fix most issues from closed terminal. 