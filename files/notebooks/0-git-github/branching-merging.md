## Branching and Merging
- In Git, a branch is a new/separate version of the main repository.
- Branches allow you to work on different parts of a project without impacting the main branch.
- When the work is complete, a branch can be merged with the main project. 
- We can even switch between branches and work on different projects without them interfering with each other.

> [git branch](https://git-scm.com/docs/git-branch)
### Listing branches ✅
- `git branch`: list all local branches in the current repository
- `git branch -l/--list`: _____
- `git branch --show-current`: print the name of the current branch. In detached HEAD state, nothing is printed.
- `git branch -a/--all`: list both remote-tracking and local branches
- `git branch -av`: shows all branches (both local and remote) {along with their latest commits}
- `git branch -r/--remotes`: list remote branches
- `git branch -rv`: _____
### Creating a new branch ✅
- `git branch <branch_name>`: create/make a new Git branch with <branch_name>
### Switching to another branch ✅
- `git switch <branch_name>`: switch (to) branch
- `git checkout <branch_name>`: switch (to) another branch
- `git checkout -b <branch_name>`: create and switch (to) the branch directly; Switch to a new branch after creating
### Renaming a branch ✅
- `git branch -m/--move <new_branch_name>`: rename a branch; use this if you want to rename current branch [done]
- `git branch -m/--move <old_branch_name> <new_branch_name>`: use this if you want to rename other/current branch [done]
### Deleting a branch ✅
- A branch cannot be deleted while being there in the same branch (that you're going to delete).
- `git branch -d <branch_name>` delete a local branch (only if mereged) [done]
- `git branch -D <branch_name>` force delete a local branch (even if unmereged) [done]

> [git merge](#)
### Merging a branch
- git merge: *combine changes from another branch*
- It’s preferred to change/switch to master branch before any branch needs to be merged with it.
- `git merge <branch_name>`: merge branch into current; merge changes from another branch; merge the <specified branch> with the master branch.
- `git merge --abort`: 