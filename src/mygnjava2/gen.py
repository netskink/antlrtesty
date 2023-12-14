
import os
import sys
import ninja_syntax


writer = ninja_syntax.Writer(sys.stdout)

# create some env variables
writer.variable("jc", os.getenv("JC", "javac"))
writer.variable("out", os.getenv("OUT", "out"))

# create a rule for java compiler command line
writer.rule("jc", "$jc -d $out $in")

# create a build statement declaring relationship
# between input and output files.
writer.build("$out", "jc", "tutorial/Tutorial.java")

#
# add these two lines to make it regen files?
#

# This line creates a command that pipes output
# to a file.
writer.rule("regen_ninja", f"{sys.executable} $in > $out")
# This lines says the file for output is build.ninja
# It is triggered when this file (gen.py) changes.
writer.build("build.ninja", "regen_ninja", __file__)


