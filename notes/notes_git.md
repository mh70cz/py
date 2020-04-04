### create repo

```
mkdir mypy
cd mypy
echo "# mypy" >> README.md
git init
git add README.md
git commit -m "first commit"
git config --global user.email "mh70@mh70.cz"
git config --global user.name "mh70cz" # mh70 atlassian mh70cz github
git commit -m "first commit"
git remote add origin https://github.com/mh70cz/mypy.git
```

### date of modification of unstaged files

```
git status -s | while read mode file; do echo $mode $file $(stat -c %y $file); done
```