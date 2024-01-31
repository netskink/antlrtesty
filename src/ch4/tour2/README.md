# Notes on how to use

This is an improvement in that it breaks up the grammar into

* parser
* lexer grammer
    - contains the bits to identify the lowest level tokens


## tour

### Build

```
$ antlr4 Expr.g4
```

### Test

* `grun` is an alias for java vm cli to run the jar file.
* `t.expr` is the sample script we are parsing

```
$ grun Expr prog -gui t.expr
```


### Custom test program

This code shows how to construct all the necessary components to parse
the sample script similar to using grun

```
$ 
```
