import ninja_syntax
import os
import sys


writer = ninja_syntax.Writer(sys.stdout)
writer.variable("cc", os.getenv("CC", "javac"))
writer.variable("out", os.getenv("OUT", "out"))
writer.rule("cc", "$cc -d $out $in")
writer.build("$out", "cc", "tutorial/Tutorial.java")

#
# add these two lines to make it regen files?
#

# This line creates a command that pipes output
# to a file.
writer.rule("regen_ninja", f"{sys.executable} $in > $out")
# This lines says the file for output is build.ninja
# It is triggered when this file (gen.py) changes.
writer.build("build.ninja", "regen_ninja", __file__)


