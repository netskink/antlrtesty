# Notes on examples

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
* tour2 - section 4.1 Matching an Arithmetic Expression Language
    - starting on page 38 under heading Importing Grammars
    - This code takes the previous example and splits into two files for the parser and lexer.
    - Remember:
        - lexer identifies numbers and identifiers. 
            - breaks up input string/stream into tokens
        - parser checks syntax
            - compares token sequences to particular patterns
* calc - section 4.2 building a calculator using a Visitor
* interface - section 4.3 building a translator with a Listener

# what is this?

* use grun to test it
* use with EvalVisitor.java to test similar to grun
    - extends LabeledExprBaseVisitor
    - demos
        - visitAssign
        - visitPrintExpr
        - visitInt
        - visitId
        - visitMulDiv
        - visitAddSub
        - visitParens
* use with Calc.java to 
