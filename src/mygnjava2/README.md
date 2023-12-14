

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


jc = javac
outdir = out
rule jc
  command = $jc -d $outdir $in
build $outdir/Tutorial.class: jc tutorial/Tutorial.java
rule testit
  command = cd $outdir; echo 'yo'; java Tutorial
build wtf: testit $outdir/Tutorial.class


#rule regen_ninja
#  command = /workspaces/antlrtesty/src/env/bin/python $in > $out
#build build.ninja: regen_ninja /workspaces/antlrtesty/src/mygnjava2/gen.py
