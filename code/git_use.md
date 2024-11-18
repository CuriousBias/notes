# Git

### Concepts
- HEAD: currently checked out commit.

## Structure and definitions
- Working directory < Staging area < Local Repo (HEAD) < Remote Repo (main) 

### Best practices
- Think of adding code in commits. 
    - Bundle all changes to related code into one commit. Do not modify different functionality across many commits. 
- Working across multiple branches. Share code by cherry picking. 

### General commands
- To check status `git status`
- To see current branch `git branch`

## Levels
1. Modified: files with changes are not yet stored in local repo
2. Staged: files with changes are marked to be committed to local repo
3. Committed: changes are stored in local repo
4. Pushed: changes are store on remote repo

### Modify
- Just make usual edits to your local directory.
- Create files `touch add file_name.txt`
- Remove files `rm file_name.txt`
- Remove directories `rm -r <specific/directory>`

### Stage
- Add file from local directory to staging area `git add <specific/file/path>`
- Un-stage a specific file `git restore <specific/file/path>`
    - Un-stage everything `git restore .`

### Commit
#### Create a commit
- To move files from staging area to local repo `git commit`
    - Commit all changes with message inline`git commit -a -m "commit message"`
    - -a This will commit everything (no need for git add first)
    - -m Adds message for commit so no need to open text editor

#### Remove a commit (local)
- Remove last commit (not pushed)
    - Move commit from commited to staged status `git reset HEAD~`
    - Need to verify:
        - Moves commit from committed to staged status: `git reset --soft HEAD~1`
        - Moves 1 commit from committed to modified status: `git reset --hard HEAD~1`
    - Remove all local commits and reset to version on remote: `git reset --hard origin/main`

### Push
Arguments (commit or branch): `git push origin source:destination` 
If destination does not exist. It will be created on remote.

#### Push to remote
- To add files committed files from local repo to remote repo: `git push`
- To push with arguments (push feature branch to remote): `git push origin feature`
    
#### Undo pushed commit (not actually removing commit, but creating new commit undoing changes).
- Remove pushed commit: `git revert HEAD`
- Remove specific commit (pushed): `git revert <commit_hash>`
    - Find commit hash in git history  `git log`

### Fetch
Download history from remote, but does not actually update local.
- Download history of remote repo: `git fetch`
- Actually update local repo: `git merge`
Arguments (commit or branch): `git fetch origin source:destination`
If destination does not exist, it will be created locally.

### Pull
Combination of fetch and merge.
Arguments (commit or branch): `git pull origin source:destination`
- Update and merge changes at once: `git pull`

#### Diverged remote
- Pull changes and rebase local: `git pull --rebase`

## Branches

### Create new feature branch from repo
Creates feature branch to avoid working on main
    ```
    git checkout main
    git pull origin main
    git checkout -b <feature>
    git add -a -m "commit some change"
    git push origin --set-upstream <feature>
    ```

### Merge feature branch onto main

```terminal
git switch <feature/branch>
git pull 
git switch main
git pull
git merge --no-ff --no-commit branch
# if conflicts
git status

# if no conflicts
git commit -m "merge branch"
git push
```

### Go to a different branch
#### Two options
1. Old command `git checkout <branch>`
2. New command `git switch <branch>`

### See difference between two branches
- `git diff <branch1> <branch2>`
- escape from long printout with ":" followed by "q"

### Merge vs Rebase
- Both methods to update one branch to match another.

#### Merge
Pro: No change in history.
Con: Reorganization is messy.
1. Merge another branch onto HEAD: `git merge branch1`

#### Rebase
Pro: Results in clean history.
Con: Reorders commits which alters history.

1. Move branch2 commits below branch1 (order of arguments same as order or commits): `git rebase branch1 branch2`
2. Rebase onto another branch (usually main)
- This will keep all commits intact
    1. Checkout main `git checkout main`
    2. Updated to latest version of main `git pull origin main`
    3. Switch to feature branch `git switch <feature_branch>`
    4. Initiate rebase `git rebase main`
            - go through rebase steps
    5. Save any changes (shouldn't there be no changes?)
    6. Don't forget to force **Push** changes `git push -f`
3. Simple interactive rebase to squash commits (reduce number)
    1. Same first 3 steps to checkout, pull origin and switch to feature
    2. Initiate rebase `git rebase -i HEAD~5` (5 for five commits)
        Can also just do squash and rebase in one step with `git rebase -i main`
    3. replace "pick" with "s" for squash at beginning of each commit. 
        - But leave the first commit as "pick" or change to "r" to edit message
    4. Follow along in text edit (Vim)
    5. "esc" + ":wq" to write and quit Vim editor. 
    6. Don't forget to force **Push** changes `git push -f`
4. Complex interactive rebase to resolve merge conflicts (due to two people working on same file)
    1. Navigate to repository
    2. Checkout main `git checkout main`
    3. Updated to latest version of main `git pull origin main`
    4. Switch to feature branch `git switch <feature_branch>`
    5. Do simple interactive rebase to squash all commits of feature branch into one commit. 
    6. Initiate rebase `git rebase main`
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
        3. Make a new commit to save changes. `git commit -a -m "resolve merge conflicts`
        4. Don't forget to force **Push** changes `git push -f`

Undo rebase
1. See log: `git reflog`
2. Undo rebase: `git reset —hard HEAD~{5}` # to reset to reflog point {5}

### Sharing between branches
- To checkout a single file from a different branch (bad) `git checkout <feature/branch> --<specific/file/path>`
- To grab a specific commit (good) `git cherrypick <commit_hash>`

### Delete branch from repo
#### Local
- List local branches `git branch`
- Delete local branch `git branch -d <branch>`
#### Remote
- List remote branches `git branch -a`
- Delete one `git push origin --delete <branch>`

### Create repository
1. Navigate to folder for repository `cd ~ /<dir>`
2. Open README.md file and add any info you want `touch README.md`
3. Initialize repo `git init`
4. Add any local files `git add files.py`
5. Add all local files `git add .`

## Pull Requests

### Prior to merging Pull request
1. Rebase to get all commits in order
2. Squash all commits into single commit
3. Check that everything still works
4. Force push changes
3. Start Pull Request

## Renaming 
### Branch
1. Rename local  `git branch -m <old> <new>`
2. Push to new remote branch  `git push -u origin <new>`
3. Delete old remote  `git push origin --delete <old>`
4. If deleting protected or default branch, will need to remove protections on remote host.

## Tags
- Associate a commit with a searchable tag.
- See tags `git fetch —tags` and `git tag -l`
- Create tag: `git tag <tag>` ex: `git tag v1.0`
- Create annotated tag: `git tag -a v1.0 "initial release"`
- Delete a local tag:
- Delete a tag on remote: `git push origin --delete  <tagname>`

## Errors
1. "error: cannot lock ref". Two commands to fix for slightly different situations.
    1. `git gc --prune=now`
    2. `git remote prune origin`
2. Branch diverged after rebase on a different machine. ` git fetch && git reset --hard`

## Traversing History
Moving between commits. 
1. Moving upwards one commit: `git checkout HEAD^`
2. Moving upwards 5 commits: `git checkout HEAD~5`
