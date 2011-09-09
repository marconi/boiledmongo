How to use:

1. cd <project_dir>
2. perl -e "s/boiledmongo/<project_name>/g;" -pi $(find . -type f)
   NOTE: Don't include the "`" and replace <project_name> with your actual project's name.
   Also note that this will break the files under .git so make sure to remove
   it first, run #2 and initialize a new repo if you're planning to.
3. rename your apps folder name: mv boiledmongo <project_name>
4. python setup.py develop
