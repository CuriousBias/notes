# Git

## Structure and definitions
- Working directory < Staging area < Local Repo (HEAD) < Remote Repo (master) 

### Best practices
- Think of adding code in commits. 
    - Bundle all changes to related code into one commit. Do not modify different functionality across many commits. 
- Working across multiple branches. Share code by cherry picking. 

### General commands
- To check status ```% git status```
- To see current branch ```% git branch```

## Levels
1. Modified: files with changes are not yet stored in local repo
2. Staged: files with changes are marked to be committed to local repo
3. Committed: changes are stored in local repo
4. Pushed: changes are store on remote repo

### Modify
- Just make usual edits to your local directory.
- Add files ```% touch file_name.txt```
- Remove files ``` % rm file_name.txt```
- Remove directories ```% rm -r <specific/directory>```
- Changes to existing files: make edits and **save** them!

### Stage
- To add file from local directory to staging area ```% git add <specific/file/path>```
- To un-stage a specific file ```% git restore <specific/file/path>```
    - Un-stage everything ```% git restore .```

### Commit
#### Create a commit
- To move files from staging area to local repo ```% git commit```
    - Commit all changes with message inline```% git commit -a -m "commit message"```
    - -a This will commit everything (no need for git add first)
    - -m Adds message for commit so no need to open text editor

#### Remove a commit **Need to verify**
- Remove last commit (not pushed)
    - Moves 1 commit from committed to staged status ```% git reset --soft ~HEAD1```
    - Moves 1 commit from committed to modified status ```% git reset --hard ~HEAD1```
    - Remove all local commits and reset to version on remote ```% git reset --hard origin/main```

### Push
- To add files committed files from local repo to remote repo ```% git push```
- Remove specific commit (pushed) ```% git revert <commit_hash>```
    - Find commit hash in git history  ```% git log```

### Pull
- To get files from remote repo to local repo ```% git fetch```
- To get files from local repo to working directory ```% git merge```
- To get from from remote repo to working directory (git fetch and git merge at once) ```% git pull```
- To abort merge conflicts ```% git reset --hard HEAD```

## Branches

### Create new feature branch from repo
```
    % git checkout master
    % git pull origin master
    % git checkout -b <feature/branch>
    % git add -a -m "commit some change"
    % git push -set-upstream origin <feature/branch>
```

### Go to a different branch
#### Two options
1. Old command ```% git checkout <branch>```
2. New command ```% git switch <branch>```

### See difference between two branches
- ```% git log <branch> ^<master>```
- escape from long printout with ":" followed by "q"

### Rebase
Reorders commits to be in order at current head of master
1. Rebase onto another branch (usually master)
- This will keep all commits intact
    1. Checkout master ```% git checkout master```
    2. Updated to latest version of master ```% git pull origin master```
    3. Switch to feature branch ```% git switch <feature_branch>```
    4. Initiate rebase ```% git rebase master```
            - go through rebase steps
    5. Save any changes (shouldn't there be no changes?)
    6. Don't forget to force **Push** changes ```% git push -f```
2. Simple interactive rebase to squash commits (reduce number)
    1. Same first 3 steps to checkout, pull origin and switch to feature
    2. Initiate rebase ```% git rebase -i HEAD~5``` (5 for five commits)
        Can also just do squash and rebase in one step with ```% git rebase -i master```
    3. replace "pick" with "s" for squash at beginning of each commit. 
        - But leave the first commit as "pick" or change to "r" to edit message
    4. Follow along in text edit (Vim)
    5. "esc" + ":wq" to write and quit Vim editor. 
    6. Don't forget to force **Push** changes ```% git push -f```
3. Complex interactive rebase to resolve merge conflicts (due to two people working on same file)
    1. Navigate to repository
    2. Checkout master ```% git checkout master```
    3. Updated to latest version of master ```% git pull origin master```
    4. Switch to feature branch ```% git switch <feature_branch>```
    5. Do simple interactive rebase to squash all commits of feature branch into one commit. 
    6. Initiate rebase ```% git rebase master```
    6. Go through files to resolve each conflict individually. 
        1. Find merge conflics
            ```
            <<<<<<
            edits
            ======
            other edits
            >>>>>>
            ```
        2. Go through and remove all markers and unwanted code. Save each file
           - This will look like deleting all text between <<<<<< and ====== or ===== and >>>>>> . One or other, not both!
        3. Make a new commit to save changes. ```% git commit -a -m "resolve merge conflicts```
        4. Don't forget to force **Push** changes ```% git push -f```

### Sharing between branches
- To checkout a single file from a different branch (bad) ```% git checkout <feature/branch> --<specific/file/path>```
- To grab a specific commit (good) ```% git cherrypick <commit_hash>```

### Delete branch from repo
#### Local
- List local branches ```% git branch```
- Delete local branch ```% git branch -d <branch>```
#### Remote
- List remote branches ```% git branch -a```
- Delete one ```% git push origin --delete <branch>```

### Create repository
1. Navigate to folder for repository ```% cd ~ /<dir>```
2. Open README.md file and add any info you want ```% touch README.md```
3. Initialize repo ```% git init```
4. Add any local files ```% git add files.py```
5. Add all local files ```% git add .```

## Pull Requests

### Prior to merging Pull request
1. Rebase to get all commits in order
2. Squash all commits into single commit
3. Check that everything still works
4. Force push changes
3. Start Pull Request

## Merge


## Errors
1. "error: cannot lock ref". Two commands to fix for slightly different situations.
    1. ```% git gc --prune=now```
    2. ```git remote prune origin```
2. Branch diverged after rebase on a different machine. ``` % git fetch && git reset --hard```


