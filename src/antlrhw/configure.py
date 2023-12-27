#!/usr/bin/env python3


import os
import sys
import ninja_syntax

# Open a file writer using stdout
#writer = ninja_syntax.Writer(sys.stdout)
# open a file writer using build.ninja
a_file = open('build.ninja', 'w')
writer = ninja_syntax.Writer(a_file)

# create some env variables
writer.comment("#")
writer.comment("# Variables")
writer.comment("#")
writer.comment("Dir for building")
writer.variable("outdir", os.getenv("OUTDIR", "out"))
writer.comment("Classpath setting")
writer.variable("CLASSPATH", ".:/Users/davis/progs/github/antlrtesty/jars/antlr-4.13.1-complete.jar:$outdir:$outdir/hello")
writer.comment("antlr tool")
writer.variable("antlr4", os.getenv("ANTLR4", "java -jar /Users/davis/progs/github/antlrtesty/jars/antlr-4.13.1-complete.jar -o $outdir"))
writer.comment("grun test rig")
writer.variable("grun", os.getenv("GRUN", "java org.antlr.v4.runtime.misc.TestRig"))
writer.newline()

# create a rule for antlr command line
writer.comment("RULE: for antlr command line")
writer.rule("antlr_r", "$antlr4 $in")
writer.newline()

# create a build statement declaring relationship
# between input and output files.
writer.comment("BUILD: transform *.g4 files into:")
writer.comment(" - *.java")
writer.comment(" - *.interp")
writer.comment(" - *.tokens")
outputs = ["$outdir/hello/Hello.interp", 
           "$outdir/hello/HelloLexer.interp", 
           "$outdir/hello/Hello.tokens",
           "$outdir/hello/HelloLexer.tokens",
           "$outdir/hello/HelloBaseListener.java",
           "$outdir/hello/HelloLexer.java",
           "$outdir/hello/HelloListener.java",
           "$outdir/hello/HelloParser.java",
           "$outdir/hello"]
writer.build(outputs, "antlr_r", "hello/Hello.g4")
writer.newline()

# create a rule for javac compiler command line
writer.comment("RULE: for javac compiler command line")
writer.rule("jc_r", "javac -d $outdir --class-path $CLASSPATH $in", description="javac $outdir")
writer.newline()



# depends upon nothing?
writer.comment("BUILD: depends upon nothing")
writer.build("$outdir/HelloLexer.class", "jc_r", "$outdir/hello/HelloLexer.java")
writer.newline()

# depends upon HelloBaseListener
writer.comment("BUILD: depends upon HelloBaseListener")
writer.build("$outdir/HelloBaseListener.class", "jc_r", "$outdir/hello/HelloBaseListener.java")
writer.newline()

# depends upon HelloParser
writer.comment("BUILD: depends upon HelloListener")
writer.build("$outdir/HelloListener.class", "jc_r", "$outdir/hello/HelloListener.java")
writer.newline()

# depends upon HelloListener
writer.comment("BUILD: depends upon HelloParser")
writer.build(["$outdir/HelloParser$$RContext.class", "$outdir/HelloParser.class"], "jc_r", "$outdir/hello/HelloParser.java")
writer.newline()


#
# Testing
#
writer.comment("#")
writer.comment("# Testing")
writer.comment("#")
writer.newline()

# create a rule for grun command line
writer.comment("RULE: for grun command line")
writer.rule("testit_r", "cd $outdir; echo hello john | $grun Hello r -tokens", description="Testing the tokenizer")
writer.newline()

# Test with grun
writer.comment("BUILD: depends upon nothing")
writer.build(["$outdir", "do_testit"], "testit_r", "$outdir/HelloParser$$RContext.class")
writer.newline()


#
# add these two lines to make it regen files?
#

# This line creates a command that pipes output
# to a file.
writer.rule("regen_ninja", f"{sys.executable} $in > $out")
# This lines says the file for output is build.ninja
# It is triggered when this file (gen.py) changes.
writer.build("build.ninja", "regen_ninja", __file__)



