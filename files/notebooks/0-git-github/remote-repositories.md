## Remote Repositories (GitHub, GitLab)
### git remote: *manage remote repository connections*
- `git remote`: list remote repos
- `git remote -v`: list all remote repositories; show remote URLs
- `git remote add origin https://github.com/<user>/<repo>.git`: create a new remote repository ??
- `git remote add origin <server>`: connect local repository to remote repository
- `git remote add <name> <url>`: add a new remote repository
- `git remote add https://github.com/<git>.git`: create a git??
- `git remote remove <name>`: remove a remote repository  
### git clone: *manage remote Git repo*
- `git clone <repository_URL>`: clone a remote repository from URL
- `git clone https://github.com/<user>/<repo>.git`: clone a remote repository  
### git push: *upload commits to remote*
- `git push origin <branch_name>`: push branch/chanages to remote repository
- `git push -u origin master`: 
- `git push origin master`: push changes to remote repository
- `git push <remote> <branch>`: push changes to a remote
- `git push origin --delete <branch_name>`: delete branch from server
### git pull: *fetch and merge from remote*
- `git pull`: update local reopsitory with remote changes; fetch and merge changes
- `git pull origin <branch_name>`: pull updates/changes from remote
- `git pull <remote> <branch>`: pull changs from a remote
### git fetch: *download latest changes without merging*
- `git fetch`: fetch changes; fetch changes withou merging
- `git fetch <remote>`: fetches all branches from remote repository