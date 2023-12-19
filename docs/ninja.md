# Ninja

Note on Ninja

* ninja does not support shell aliases
* ninja does not support wildcards
* ninja uses `$` for both line continuatino and variable expansion

## Command args

The best way to find out args for ninja is to use `man`

### Change directory

Use `-C somedir` to change directory to `somedir`` before running `ninja`.

```
$ ninja -C out tutorial
```

### Clean ninja build output

ie. make clean

```
$ ninja -t clean
```

if using an `out` directory:

```
$ ninja -C out -t clean
```