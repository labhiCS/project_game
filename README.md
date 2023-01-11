# Python-Course-For-Beginner
Repo for teaching python to a beginner (my Cousin)

#### Style:
* PEP8 guidlines suggest 78 characters per line

#### Git commands 
`$ git add  filename.py`

`$ git commit -m message`

`$ git push -u origin main`

* if you see any error while pushing the code to git use :

`$ git pull`

* Display all available branch

`$ git branch`

* Create a new branch name 

`$ git branch name ` =====> name = name of the branch you want to create 

For example:
`$ git branch week2`

* Switching branch 

`$ git checkout name` ===> again here name = the branch you want to checkout

* Deleting the branch 

`$ git branch -d nameOfTheBranch `
 
 **Make sure to change your current branch to another one , if it's the one you're deleting 
 then it will give you error**

 * If you're not able to delete the branch even after following above step you might want to use force delete using -D instead of -d like :

 `$ git branch -D nameOfTheBranch`
 
 * pull from specific branch remote repo 

 `$ git pull <remote_repo> <branch>`

 * clone from specific branch 
 
 `$ git clone -b <branch> <remote-repo>`

 For example:
 
 `$ git clone -b week4 github_repo-link`

#### Common terminal commands 
`$ cd ..` => go back a folder 

`$ cd 'folder'` => go inside a folder 

`$ ls ` ===> list directories 

#### Anaconda  activate

`$ source ~/anaconda3/bin/activate root`

`$ jupyter-notebook`