# Git
Some notes for working with git

## Structure and definitions
- Git structure: Repo is repository
- Working directory < Staging area < Local Repo (Head) < Remote Repo (Master) 
- staged: files with changes are marked to be committed to local repo
- modified: files with changes are not yet stored in local repo
- committed: changes are stored in local repo

## Git commands
- To check status ```% git status```

### Stage
- To add file from local directory to staging area ```% git add <specific/file/path>```
- To un-stage a specific file ```% git restore <specific/file/path>```
    - Un-stage everything ```% git restore .```

### Commit
- To move files from staging area to local repo ```% git commit```
    - Commit all changes with message inline```% git commit -a -m "commit message"```
    - -a This will commit everything (no need for git add first)
    - -m Adds message for commit so no need to open text editor

### Push
- To add files committed files from local repo to remote repo ```% git push```

### Pull
- To get files from remote repo to local repo ```% git fetch```
- To get files from local repo to working directory ```% git merge```
- To get from from remote repo to working directory (git fetch and git merge at once) ```% git pull```

### Delete
- Delete files ```% git rm <specific/file/path>```
- Delete directories ```% git rm -r <specific/directory>```        

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
2. Interactive rebase
- This has many options. One is to squash commits (reduce number)
    1. Same first 3 steps to checkout, pull origin and switch to feature
    2. Initiate rebase ```% git rebase -i HEAD~5``` (5 for five commits)
        Can also just do squash and rebase in one step with ```% git rebase -i master```
    3. replace "pick" with "s" for squash at beginning of each commit. 
        - But leave the first commit as "pick" or change to "r" to edit message
    4. Follow along in text edit (Vim)
    5. "esc" + ":wq" to write and quit Vim editor. 
    6. Don't forget to force **Push** changes ```% git push -f```

## Branches

### Go to a different branch
#### Two options
1. Old command ```% git checkout <branch>```
2. New command ```% git switch <branch>```

### See difference between two branches
- ```% git log <branch> ^<master>```
- escape from long printout with ":" followed by "q"

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

### Create new feature branch from repo
```
    % git checkout master
    % git pull origin master
    % git checkout -b <feature/branch>
```

## Pull Requests

### Prior to merging Pull request
1. Rebase to get all commits in order
2. Squash all commits into single commit
3. Check that everything still works
4. Force push changes
3. Start Pull Request

## Troubleshooting
Issues ran into so far

### Undo commits  **Need to verify**

- Remove last commit (not pushed)
    - Moves 1 commit from committed to staged ```% git reset --soft ~HEAD1```
    - Moves 1 commit from committed to un-staged ```% git reset --hard ~HEAD2```

- Remove specific commit (pushed) ```% git revert <commit_hash>```
    - Find commit hash in git history

## Errors
- "error: cannot lock ref" ```% git gc --prune=now```

## Best practices
- Think of adding code in commits. 
    - Bundle all changes to related code into one commit. Do not modify different functionality across many commits. 
- Working across multiple branches. Share code by cherry picking. 
