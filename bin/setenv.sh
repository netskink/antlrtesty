

#
# github codespace
#
#ROOTDIR="/workspaces/antlrtesty/"


#
# macos terminal
#
ROOTDIR="${HOME}/progs/github/antlrtesty/"

#export CLASSPATH=".:/usr/local/lib/antlr-4.13-1.jar:$CLASSPATH"
# github codespace
#export CLASSPATH=".:/workspaces/antlrtesty/jars/antlr-4.13.1-complete.jar:$CLASSPATH"
# macos terminal
export CLASSPATH=".:${ROOTDIR}/jars/antlr-4.13.1-complete.jar:$CLASSPATH"




# github codespace
#alias antlr4='java -jar /workspaces/antlrtesty/jars/antlr-4.13.1-complete.jar'
# macos terminal
alias antlr4="java -jar ${ROOTDIR}/jars/antlr-4.13.1-complete.jar"

alias grun="java org.antlr.v4.runtime.misc.TestRig"


# GN
# github codespace
#export PATH="/workspaces/antlrtesty/gn/out:$PATH"
# macos terminal
export PATH="${ROOTDIR}/gn/out:$PATH"
