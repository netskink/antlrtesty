

[this guy writes his own gn](https://bernsteinbear.com/blog/ninja-is-enough/)


Get the ninja_syntax.py script

```

$ curl -O https://raw.githubusercontent.com/ninja-build/ninja/master/misc/ninja_syntax.py
```

Use like so:

```
$ python gen.py > build.ninja
$ out=out ninja
```

To clean

```
$ ninja -t clean
```


