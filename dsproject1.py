# my data science project

"""
This is another way to leave comments
Let's learn git commands
"""
# go to Data_Science directory
pwd
cd /Users/sanghyeop/PycharmProjects/Data_Science

# make sure I'm on the right branch
git checkout
git status

# add/edit a file I'm working on. Then,
git add .
git status
git commit -m "leave a commit note"
git commit -am "or use this to add & commit"

git log

#### 2.
"""
create a file: touch [filename]
check the status: git status
track and stage a single file: git add [filename]
track and stage all files: git add .
commit with a message: git commit -m "description of commit"
view the log: git log
push changes: git push [remotename] [branchname]
"""

# create a new file
git remote -v
touch new.md
ls

# open up the new file and edit. Then,
git add .
git status
git commit -m "edited"
git status
git log

# everything we've done so far has only affected the local machine.
# to get our  github repo up-to-date, we need to push our changes
git push origin master

#### Syncing my Github folk
# youtube.com/watch?v=-zvHQXnBO6c
git remote -v
git remote add upstream https://github.com/su1391/Gru_image.git
git fetch upstream
git merge upstream/master
git push origin master







