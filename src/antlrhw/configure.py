
import os
import sys
import ninja_syntax


writer = ninja_syntax.Writer(sys.stdout)

# create some env variables
writer.variable("jc", os.getenv("JC", "javac"))
writer.variable("outdir", os.getenv("OUTDIR", "out"))

# create a rule for java compiler command line
writer.rule("jc", "$jc -d $outdir $in")

# create a build statement declaring relationship
# between input and output files.
writer.build("$outdir/Tutorial.class", "jc", "tutorial/Tutorial.java")

#
# This will make a test to run 
#
# Create a rule for running java
writer.rule("testit", "cd $outdir; echo 'yo'; java Tutorial")
# create a build statement declaring an action
writer.build("do_testit", "testit", "$outdir/Tutorial.class")            



#
# add these two lines to make it regen files?
#

# This line creates a command that pipes output
# to a file.
#writer.rule("regen_ninja", f"{sys.executable} $in > $out")
# This lines says the file for output is build.ninja
# It is triggered when this file (gen.py) changes.
#writer.build("build.ninja", "regen_ninja", __file__)


