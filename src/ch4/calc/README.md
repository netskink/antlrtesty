# Notes on how to use

This is an improvement in that it breaks up the grammar into

* parser
* lexer grammer
    - contains the bits to identify the lowest level tokens


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
