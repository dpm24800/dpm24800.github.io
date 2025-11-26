# Git and GitHub
## Indroduction
## **What is Git?**  
- Git is a distributed version control system.
- It helps manage code changes efficiently and collaborate with others on software projects.
- Git helps you keep track of code changes.
- Git is used to collaborate on code.
- Git and GitHub are different things.

## Why Git?
Over 70% of developers use Git!
- Developers can work together from anywhere in the world.
- Developers can see the full history of the project.
- Developers can revert to earlier versions of a project.

## Features of Git :-
- When a file is changed, added or deleted, it is considered modified
- You select the modified files you want to Stage
- The Staged files are Committed, which prompts Git to store a permanent snapshot of the files
- Git allows you to see the full history of every commit.
- You can revert back to any previous commit.
- Git does not store a separate copy of every file in every commit, but keeps track of changes made in each commit!

## Installation
- Windows/Mac/Linux - Download Git
- Verify Installation: `git --version`

- [Glossary](C:/Program%20Files/Git/mingw64/share/doc/git-doc/gitglossary.html)

## Basic Concepts
- Repository (Repo): Directory tracked by Git
- Commit: A snapshot of your code
- Branch: Independent line of development
- Clone: Copy of a repository from remote to local

## Best practices
- Write meaningful commit messages.
- Commit often.
- Keep branches small and focused.
- Regularly sync branches with main.




# General Git Features



## Stashing Changes
### git stash:
- save uncommitted changes temporarily 
- `git stash`: stash changes; saving changes to stash
- `git stash list`: list all stashes  
- `git stash apply`: apply the latest stash
- `git stash apply [stash_number]`: apply the latest stash
- `git stash pop`: apply stash
- `git stash drop`: drop the latest stash; delete from stash

## Tagging
- `git tag`: list all tags
- `git tag <tag_name>`: create a new tag
- `git tag <tag> <commit_ID>`: create tag (eg. `git tag 1.0.0 1b2e1d63ff`)
- `git push origin <tag_name>`: push tag to remote






# Cleaning Repository
- `git clean -f`: remove untracked files [done]
- `git clean -fd`: remove untracked directories too [done]

## Advanced
### git rebase
- reapply commits on top of another base
- `git rebase <branch_name>`: rebase branch
### git cherry-pick
- apply specific commit from another branch

## Git Help
- If you are having trouble remembering commands or options for commands, you can use Git help.
- `git help -a/--all`: list available subcommands and some concept guides.
- `git <command> -help`: See all the available options for the specific command
- `git help -g`: list available subcommands and some concept guides.
- `git help git`: overview of the system [done]
- `git help <command>`: read about a specific subcommand or concept (on webpage)
- `git help <concept>`: read about a specific subcommand or concept (on webpage)

If you find yourself stuck in the list view, `SHIFT + G` to jump the end of the list, then `q` to exit the view.

https://www.facebook.com/photo?fbid=122147070482888020&set=pcb.1850700518862323


- https://www.facebook.com/share/p/19XTSBqm2J/
- https://www.facebook.com/share/p/17fZUCeydD/
- https://www.facebook.com/share/p/19rQNQMB1y/
- https://www.facebook.com/share/p/19iAdEBGgK/