
# Fresh Install

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