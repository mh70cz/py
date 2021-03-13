## create repo

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

## date of modification of unstaged files

```
git status -s | while read mode file; do echo $mode $file $(stat -c %y $file); done
```

## Kopie starsi verze souboru pod jinym jmenem

    git show commit_id:path/to/file > path/to/file

problem s relative paths ve windows (funguje s ./path) - viz nize



zobrazeni historie

    git log  <file_name>


C:\Users\m.houska\Documents\_CIS\Toyota\CZ\reports\VariantyNabidek>git log
commit 90b363f7f3b79ed7422739be034569005afec067 (HEAD -> master)
Author: mh70cz <mh70@mh70.cz>
Date:   Mon Apr 27 14:40:16 2020 +0200

first
```
C:\Users\m.houska\Documents\_CIS\Toyota\CZ\reports\VariantyNabidek>git show 90b363f7f3b79ed7422739be034569005afec067:./VariantyNabidek.report > ./VariantyNabidek_original.report
```

## Remote "local" bare repo

http://www.thehorrors.org.uk/snippets/git-local-filesystem-remotes/


vytvoreni remote "local" bare repo bare repo:
cd c:\Users\m.houska\OneDrive\CIS\git_bare

    git init --bare ci.git

V lokalnim repu

    git remote add origin /c/Users/m.houska/OneDrive/CIS/git_bare/ci.git
    git git push origin master

Remove remote, show remote 

    $ git remote rm destination  # nesmaze "vzdalene" repo, jen odpoji
    $ git remote -v

##  Pridani jen modifikovanych souboru
(ignoruje untracked)  
git add -u 