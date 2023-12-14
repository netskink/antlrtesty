import ninja_syntax
import os
import sys


writer = ninja_syntax.Writer(sys.stdout)
writer.variable("cc", os.getenv("CC", "clang"))
writer.rule("cc", "$cc $cflags -c -o $out $in")
writer.rule("ld", "$cc -o $out $in $ldflags")
writer.build("main", "ld", ["main.o", "lib.o"])
writer.build("main.o", "cc", "main.c")
writer.build("lib.o", "cc", "lib.c", implicit=["lib.h"])


