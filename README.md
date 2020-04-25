GIT - in the terminal 

1. check if git is intalled : git --version
2. check in config if user.email and user.name are set : git config --list
3. press q to get out
4. cd into the directory we want to track with git
5. start tracking the directory with : git init
6. Adding all files to the stagging area : git add -A
7. Commit files with message : git commit -m "Initial commit ATO"

Notes on GIT:

- to get help on a git <verb>: git help <verb> (e.g. git help config)
- see untracked files : git status
- ignore a file : touch .gitignore
  This will create a new file in the current directoty and you can insert the file you want to ignore in that .gitignore file
 - Git structure : Working directory > Stagging Area > .git directory (Repository)


Notes on the Terminal:
- ls command lists attributes of files and directories in the current directory. ls options are :
  - -a: lists all files (incl. hidden)
  - -l: produces a long listing
  - options can be concatenated (e.g. ls -la)
