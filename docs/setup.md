
# Java install on macOS

## specific version

This installs a specific version on macOS

```
$ brew install --cask semeru-jdk-open@17
```

## select specific version

```
$ export JAVA_HOME=`/usr/libexec/java_home -v 17`
$ java --version
openjdk 17.0.11 2024-04-16
IBM Semeru Runtime Open Edition 17.0.11.0 (build 17.0.11+9)
Eclipse OpenJ9 VM 17.0.11.0 (build openj9-0.44.0, JRE 17 Mac OS X aarch64-64-Bit 20240416_599 (JIT enabled, AOT enabled)
OpenJ9   - b0699311c7
OMR      - 254af5a04
JCL      - 5d7d758b682 based on jdk-17.0.11+9)
$ export JAVA_HOME=`/usr/libexec/java_home -v 19`
$ java --version
openjdk 19.0.2 2023-01-17
OpenJDK Runtime Environment (build 19.0.2+7-44)
OpenJDK 64-Bit Server VM (build 19.0.2+7-44, mixed mode, sharing)
```

# Maven install on macOS

```
$ brew install mvn
```




# Fresh Install of Antlr

By default, I did not need to install java.  However, if you need
to install a particular java version use the process above
to install and switch java versions.

1. get the jar
    * `mkdir jars`
    * `cd jars`
    * `curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar`
2. source the bin/setenv.sh script
3. verify antlr4 and grun runs
4. Install a python venv
    * `cd src`
    * `mkdir env`
    * `python3 -m venv env`
    * `source env/bin/activate`
5. Install ninja
    * github codespace
        * `sudo apt-get update`
        * `sudo apt-get upgrade`
        * `sudo apt-get install ninja`
    * macos
        * `brew update`
        * `brew upgrade`
        * `brew install ninja`
5. Get gn and disable git
    * `git clone https://gn.googlesource.com/gn`
6. Test gn install
    * `cd gn`
    * `python build/gen.py`
    * `ninja -C out`
        * it will build code using compiler
    * disable git so the repo does not have a submodule
    * `rm -rf .git`


# Resuming work

1. source the setup script
    * `cd antlrtesty`
    * `source bin/setenv.sh`
2. activate the environment
    * `cd antlrtesty`
    * `source src/env/bin/activate`
3. Using the antlrhw examples, make the following build.ninja file
    * `cd src/antlrhw`
    * `cp build.ninja.works build.ninja`
    * `ninja`
        * builds the sample code
    * `ninja -t clean`
        * cleans the build results
4. Test using the `configure.py` script
    * `./configure.py`
    * `ninja`
    * `ninja -t clean`
