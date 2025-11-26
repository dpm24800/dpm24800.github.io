## 0. Git Configuration: for the first time
- `git config --global user.name "user_name"`: set global user_name; set the user_name that will be associated with your commits [done]
- `git config --global user.email "email"`: set global email; set the email that will be associated with your commits [done]
- `git config --global core.editor [editor]`: set the default text editor for commit messages (eg. `vi`, `code`)
- 
- `git config --global alias.st "status"`: create a short for a Git command (eg. `alias.glog "log --graph --oneline"`)
- `git config --global --edit`: open the global config file in a text editor for manual editing
- `git config --list`: xxx [done]

## 1. Git Initialization
- Unless Git initialization, it doesn't know/track the changes made in files and directories.
- Once Git is initialized, now it knows that it should watch the folder you initiated it on. 
- Git creates a hidden folder to keep track of changes.
- `git init`: initialize a new Git repository [done]

## 2. Staging files
- Staged files are files that are ready to be committed to the repository you are working on. 
- When you first add files to an empty repository, they are all untracked. 
- To get Git to track them, you need to stage them, or add them to the staging environment.
---
- `git add .`: stage all changes [done]
- `git add *`: add all changes to INDEX [done]
- `git add -A`: staging all files in a folder [done]
- `git add --all`: staging all files in a folder [done]
- `git add <file_name>`: stage a changes for commit; stage specific file; add changes to INDEX; add changes to staging [done]

- `git add -p <file_name>`: 
- `git rm --cached <file_name>`: remove/delete file, keep file cached
- `git rm -f <file_name>`: force removal/deletion of the file 
- `git rm <file_name>`: remove/delete file

## 3. Committing change: adding files to Git repo:
- Adding commits keep track of our progress and changes as we work. 
- Git considers each commit change-point or "save-point". 
  - It is a point in the project you can go back to if you find a bug, or want to make a change. 
- When we commit, we should always include a message.
---
- `git commit -m "commit_message"`: commit (changes) with message; save changes to local repository
### Git Commit without Stage
- Sometimes, when you make small changes, using the staging environment seems like a waste of time. 
- It is possible to commit changes directly, skipping the staging environment.
- `git commit -am "commit_message"`: add (tracked) & commit; commit without stage [done]
- `git commit -a -m "commit_message"`: same as above
### Changing commit messge
- `git commit --amend -m "new_commit_message"`: Rename the latest commit message which hasn't pushed yet:

## 4. Getting history of Local Changes/Status of files and log
- `git status`: view repository status; show changes status; check status; show current changes and staged files [done]
- `git status --short`: file status in a more compact way

- `git log`: view commit history for repos[done]
- `git log --oneline`: view short commit history; compact log [done]

- `git log -p <file_name>`: ?? git history
- `git blame <file>`: ?? git history

## Viewing differences
### git diff
- show differences between commits or branches
- `git diff`: show changes between working directory and index
- `git diff HEAD`: show changes between working directory and last commit
- `git diff <source_branch> <target_branch>`: view changes between two branches (eg `git diff feature_x feature_y`)

## Undoing/restoring Changes
### git revert:
- create new commit to undo a change
- `git revert <commit_hash>`: revert commit; Revert changes in a commit
- `git revert <commit>`: Undo changes from specified commit by creating a new commit; revert commit
### git reset
- unstage or undo commits
- `git reset <file>`: remove file from staging index but leave unchanged locally; unstage file
- `git reset <commit>`: resets to mommit ??
- `git reset --hard HEAD`: Discard changes; eg. `git reset --hard HEAD~3`
- `git reset --hard`: reset to HEAD

### git checkout
- `git checkout HEAD <file_name>`:
- `git checkout -- <file_name>`: replace working copy with latest from HEAD
- `git checkout <file_name>`: discard changes
- `git clean -n`: shows which files would be removed from working directory. Use `-f` option to execute clean.