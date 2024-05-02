# Notes on examples

There are two types of patterns used in this book

* Parse-Tree Listeners
    - Antlr provides ParseTreeWalker
    - ParseTreeListener 
    - A ParseTreeListener subclass specific to each grammar
    - ParseTreeWalker calls the the enter/exit methods for rule
* Parse-Tree Visitors
    - similar but you control the walk?
    - uses option -visitor on antlr command line
    - ParseTree tree = ...; // tree is result of parsing
    - MyVisitor v = new MyVisitor();
    - v.visit(tree)
    - It calls the visitSomeTopLevelNode() 
    - then that routine would call the visitLowerNodes() for each of the children
    - so on and so forth.


## chapter 3

Ths chapter has one grammar but various uses of the grammar.  The grammar is ArrayInit
and pertains to recognizing `{1,{2,3}, 4}` constructs.

It shows how to:

* use grun to test it
* use with Test.java to test similar to grun and print the parse tree
* use with ShortToUnicodeString.java and Translate.java
    - ShortToUnicodeString extends ArrayInitBaseVisitor
    - demos
        - enterInit
        - exitInit
        - enterValue
    - Translate.java uses ParseTreeWalker()
        - walks with ShortToUnicodeString()


## Chapter 4

* tour - section 4.1 Matching an Arithmetic Expression Language
    - up to page 38
    - Uses grun to test
    - Uses ExprJoyRide.java
        - demos
        - calls the parser
        - tree.toStringTree(parser)
* tour2 - section 4.1 Matching an Arithmetic Expression Language
    - starting on page 38 under heading Importing Grammars
    - This code takes the previous example and splits into two files for the parser and lexer.
    - Remember:
        - lexer identifies numbers and identifiers. 
            - breaks up input string/stream into tokens
        - parser checks syntax
            - compares token sequences to particular patterns
    - same as tour but separates the grammar and lexer
* calc - section 4.2 building a calculator using a Visitor
    * builds grammar with
        - -no-listener
        - -visitor
    * use with EvalVisitor.java to test similar to grun
        - extends LabeledExprBaseVisitor
        - demos
            - visitAssign
                - visits expr
            - visitPrintExpr
                - visits expr
            - visitInt
            - visitId
            - visitMulDiv
                - visit expr (left and right)
            - visitAddSub
                - visit expr (left and right)
            - visitParens
                - visit expr 
    * use with Calc.java to 
        - creates a eval = new EvalVisitor()
        - simply does eval.(tree)



* interface - section 4.3 building a translator with a Listener


