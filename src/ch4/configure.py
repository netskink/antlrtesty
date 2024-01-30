#!/usr/bin/env python3


import os
import sys
import ninja_syntax

# Open a file writer using stdout
# writer = ninja_syntax.Writer(sys.stdout)
# open a file writer using build.ninja
a_file = open('build.ninja', 'w')
writer = ninja_syntax.Writer(a_file)

# create some env variables
writer.comment("#")
writer.comment("# Variables")
writer.comment("#")
writer.comment("Dir for building")
writer.variable("outdir", os.getenv("OUTDIR", "out"))
writer.comment("Dir for grammar")
writer.variable("srcdir", "starter")
writer.comment("Classpath setting")
writer.variable("CLASSPATH", ".:/Users/davis/progs/github/antlrtesty/jars/antlr-4.13.1-complete.jar:$outdir:$outdir/$srcdir")
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
outputs = ["$outdir/$srcdir/ArrayInit.tokens",
"$outdir/$srcdir/ArrayInitLexer.tokens",
"$outdir/$srcdir/ArrayInit.interp",
"$outdir/$srcdir/ArrayInitLexer.interp",
"$outdir/$srcdir/ArrayInitBaseListener.java",
"$outdir/$srcdir/ArrayInitLexer.java",
"$outdir/$srcdir/ArrayInitListener.java",
"$outdir/$srcdir/ArrayInitParser.java",
"$outdir/$srcdir"]
writer.build(outputs, "antlr_r", "$srcdir/ArrayInit.g4")
writer.newline()

# # create a rule for javac compiler command line
writer.comment("RULE: for javac compiler command line")
writer.rule("jc_r", "javac -d $outdir --class-path $CLASSPATH $in", description="javac $outdir")
writer.newline()



# depends upon nothing
writer.comment("BUILD: depends upon nothing.")
writer.comment("BUILD: makes class:")
writer.comment("  * ArrayInitLexer")
writer.build("$outdir/ArrayInitLexer.class", "jc_r", "$outdir/$srcdir/ArrayInitLexer.java")
writer.newline()

# depends upon nothing
writer.comment("BUILD: depends upon nothing.")
writer.comment("BUILD: makes class:")
writer.comment("  * ArrayInitLexer")
writer.build(["$outdir/ArrayInitParser$$InitContext.class","$outdir/ArrayInitParser$$ValueContext.class","$outdir/ArrayInitBaseListener.class"], "jc_r", "$outdir/$srcdir/ArrayInitBaseListener.java")
writer.newline()

# depends upon nothing
writer.comment("BUILD: depends upon nothing.")
writer.comment("BUILD: makes class:")
writer.comment("  * ArrayInitLexer")
writer.comment("  * ArrayInitParser")
writer.comment("  * ArrayInitParser$InitContext")
writer.comment("  * ArrayInitParser$ValueContext")
writer.build("$outdir/ArrayInitListener.class", "jc_r", "$outdir/$srcdir/ArrayInitListener.java")
writer.newline()

# depends upon nothing
writer.comment("BUILD: depends upon nothing.")
writer.comment("BUILD: makes class:")
writer.comment("  * ArrayInitLexer")
writer.comment("  * ArrayInitParser")
writer.comment("  * ArrayInitParser$InitContext")
writer.comment("  * ArrayInitParser$ValueContext")
writer.build("$outdir/ArrayInitParser.class", "jc_r", "$outdir/$srcdir/ArrayInitParser.java")
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
writer.rule("testit_r", "cd $outdir; echo {1, 2, 3} | $grun ArrayInit init -tokens", description="Testing the tokenizer")
writer.newline()

# Test with grun
writer.comment("BUILD: depends upon nothing")
writer.build(["$outdir", "do_testit"], "testit_r", "$outdir/ArrayInitParser$$InitContext.class")
writer.newline()


# #
# # add these two lines to make it regen files?
# #

# # This line creates a command that pipes output
# # to a file.
# writer.rule("regen_ninja", f"{sys.executable} $in > $out")
# # This lines says the file for output is build.ninja
# # It is triggered when this file (gen.py) changes.
# writer.build("build.ninja", "regen_ninja", __file__)



