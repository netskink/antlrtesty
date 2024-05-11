# Notes on how to use

This example shows how to parse java source files to 
make an Interface definition which includes comments
in class and method definitions.

It uses grammar Java.g4 but only uses two definitions

* classDeclaration
    - line 37
* methodDeclaration
    - line 126


## tour

### Build

```
$ antlr4 -no-listener -visitor LabeledExpr.g4
```


### Custom program




```
$ javac Calc.java LabeledExpr*.java
$ java Calc t.expr
193
17
9
```
