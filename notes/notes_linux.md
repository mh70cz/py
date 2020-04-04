

***
mount -t "ntfs" -o ro /dev/sdb1 /media/mh70/big
https://github.com/xybu/onedrived-dev

***
### Find files modified after some date / time

https://stackoverflow.com/questions/8985989/is-there-any-way-to-find-out-changed-file-after-some-date-in-whole-project-code

```
$ find . -mmin -30        # -mmin n File's data was last modified n minutes ago.

find . -type f -mtime -7  # - mtime  n*24 hours ago , -type f -- regular files only

# modified after /tmp/foo
find /some/files -newer /tmp/foo
```