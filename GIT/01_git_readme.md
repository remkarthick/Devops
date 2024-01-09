# I) Working in Local Repository

# Create a local git repository

- go to any directory /create a new directory and get in that directory and type the below command

  ```
  git init
  ```
  > this will create a .git directory
  > this folder/directory will become a local git repo
  > ex. Initialized empty Git repository in /home/kk/Desktop/gitrepos/test1/.git/
  > Default branch will be master
## Create 10 folders in the directory
ex.
```
kk@kk-computer:~/Desktop/gitrepos/test1$ mkdir planet{1..10}
```
## Create 10 files in the directory
ex.
```
kk@kk-computer:~/Desktop/gitrepos/test1$ touch star{1..5}.txt
```
# Get Status of reposiory

```
git status
```
> Sample Output
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        star1.txt
        star2.txt
        star3.txt
        star4.txt
        star5.txt

nothing added to commit but untracked files present (use "git add" to track)
```
# To bring files to Staging area

```
git add .
```

# Check if files are in staging/tracking area(run after git add .)
```
git status
```

> Sample Output
```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   star1.txt
        new file:   star2.txt
        new file:   star3.txt
        new file:   star4.txt
        new file:   star5.txt

```
# Configure email and user name in git config (otherwise there will be problem in commit)

```
git config --global user.email "remkarthick@gmail.com"
git config --global user.name "K REM"
```
## To get what you have configured

```
git config --global -l
```
or
```
git config --global --get user.name
```
# Commit to local repository
```
git commit -m "kk's first commit"
```
- only the files that are staged(git add) will be committed to local repo
-------------------------------
# II ) Working with remote repository

# a) Local to remote

# b) Remote to local

> git clone `URL`

