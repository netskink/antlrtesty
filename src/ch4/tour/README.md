# Notes on how to use


## tour

![img](./imgs/uml.png)

* [lucid uml url](https://www.youtube.com/watch?v=UI6lqHOVHic)
* [all antrl classes](https://www.antlr.org/api/Java/allclasses.html)
* abstract classes are show either in Italics or `<<abstract class>>`
* public attribute or method shown with `+`
* private shown with `-`
* protected with `#`
* connections with open arrow head shown inheritance
* connections which use are shown with a word describing the relationship. eg. "eats"
* association where a group can have a collection of classes is shown with open diamond on group end.  It denotes an aggregation.  This applies when the part can exist outside the whole.  
* Composition is when the parts can not exist without the whole.  The example is a visitor center with a bathroom and a lobby.  If the visitor center is destroyed the lobby and the bathroom are destroyed as well.  In this case the composition is denoted by a filled in diamond at the visitor center end.
* Multiplicity - If only one lobby is possible, put a 1 at the lobby end of the association line.  If more than one bathroom can exist put a `1..*` at the end of the bathroom composition line.
    - 0..1 zero to one (optional)
    - n specific number
    - 0..* zero to many
    - 1..* one to many
    - m..n specific range
* attributes
    - shown in top of class
    - visiblity marker then name : type
* methods
    - shown in bottom of class
    - visibility marker then function name: return type






### Build 

#### build using book

```
$ antlr4 Expr.g4
```

#### build using ninja

```
$ ninja
or
$ ninja -t clean
```


### Test

* `grun` is an alias for java vm cli to run the jar file.
* `t.expr` is the sample script we are parsing

```
$ grun Expr prog -gui t.expr
or
$ ninja
```

This example uses the test rig to test the parser first.  Afterwards,
it uses a custom java program ExprJoyRide.java to exercise the grammar.

