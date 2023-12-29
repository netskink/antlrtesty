# Notes on the antlr ch3

Builds a parser and lexer that recognizes a grammer that looks like:

```
{1, 2, 3}
{1, {2, 3}, 4}
```

* A lexer breaks up the input stream into tokens.
* A parser checks syntax.

## manual steps to test

### Set environment

Setup antlr alias's and python virtual environment

```
$ source /workspaces/antlrtesty/bin/setenv.sh
$ source /workspaces/antlrtesty/src/env/bin/activate
```

### Examine the antlr grammar

```
$ cd src/antlrhw/starter
$ cat ArrayInit.g4
```

```
grammar ArrayInit;              // Define a grammar called ArrayInit

/** A rule called init that matches comma-separated values between {...} */
init  : '{' value (',' value)* '}' ; // must match at least one value

/** A value can be either a nested array/struct or a simpmle integer (INT) */
value : init
      | INT
      ;

/** parser rules start with lowercase letters */
/** lexer rules consist of all uppercase letters */
INT  :  [0-9]+  ;            // Define token INT as one or more digits
WS   :  [ \t\r\n]+ -> skip;  // Define whitespace rule, toss it out
```


### Run antlr on the grammar definition 

```
$ antlr4 ArrayInit.g4
```

This makes:

* tokens
    - ArrayInit.tokens
    - ArrayInitLexer.tokens
* interp
    - ArrayInit.interp
    - ArrayInitLexer.interp
* java
    - ArrayInitBaseListener.java
    - ArrayInitLexer.java
    - ArrayInitListener.java
    - ArrayInitParser.java



### Compile the generated java code

```
$ javac *.java
```

### Run the test rig on the grammar

The test rig takes a grammar name, a starting rule name (consider it similar to main() ) and various options.  In this
case options to print the various tokens created during recognition.


```
$ grun Hello r -tokens
```

Use `ctrl-d` to exit.  Afterwards, the `recognizer` exercised by the test rig
prints the list of recognized tokens.

```
hello john
[@0,0:4='hello',<'hello'>,1:0]
[@1,6:9='john',<ID>,1:6]
[@2,11:10='<EOF>',<EOF>,2:0]
```


The list has an entry for each `token` with the following info:

* @0 means token 0
* 0:4 means the token goes from position 0 to position 5
* ='hello' means token text
* <'hello> means token 
* 1:0 means line 1, character 0

Notes regarding counts

* ids start counting at zero
* positions start counting at zero
* lines start counting at one


## Building with configure and ninja

### Set environment

Setup antlr alias's and python virtual environment

```
$ source /workspaces/antlrtesty/bin/setenv.sh
$ source /workspaces/antlrtesty/src/env/bin/activate
$ cd src/antlrhw
```



