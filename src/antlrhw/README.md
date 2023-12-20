

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



# Sample code to do what I need with ninja

Now, all I need to do is get the configure.py script to build the equivalent of this

```

#
# Variables
#
outdir = out

CLASSPATH = .:/workspaces/antlrtesty/jars/antlr-4.13.1-complete.jar:$outdir:$outdir/hello

# ninja does not respect shell aliases
antlr4 = java -jar /workspaces/antlrtesty/jars/antlr-4.13.1-complete.jar -o $outdir

# grun
grun = java org.antlr.v4.runtime.misc.TestRig



# rule to transform *.g4 files into *java, *.interp and *.tokens files
rule antlr_r
  command = $antlr4 $in

# Build statement
# Note the use of dollar sign to escape new lines and variables.
build $
$outdir/hello/Hello.interp $
$outdir/hello/HelloLexer.interp $
$outdir/hello/Hello.tokens $
$outdir/hello/HelloLexer.tokens $
$outdir/hello/HelloBaseListener.java $
$outdir/hello/HelloLexer.java $
$outdir/hello/HelloListener.java $
$outdir/hello/HelloParser.java $
$outdir/hello $
: antlr_r hello/Hello.g4


# rule to compile java code
rule jc
  command = javac -d $outdir --class-path $CLASSPATH $in
  description = javac $outdir

# depends upon nothing
build $outdir/HelloLexer.class: jc $outdir/hello/HelloLexer.java

# depends upon HelloListener
build $outdir/HelloBaseListener.class: jc $outdir/hello/HelloBaseListener.java

# depends upon HelloParser
build $outdir/HelloListener.class: jc $outdir/hello/HelloListener.java

# depends upon HelloListener
build $outdir/HelloParser$$RContext.class $outdir/HelloParser.class: jc $outdir/hello/HelloParser.java






#
# Testing
#

rule testit
  command = cd $outdir; echo hello john | $grun Hello r -tokens 
  description = Testing the tokenizer

build $outdir do_testit: testit $outdir/HelloParser$$RContext.class
```

