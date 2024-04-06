grammar LabeledExpr;  // Rename again

import CommonLexerRules;  // includes all rules from CommonLexerRules.g4

// 
// NOTE:
// The # symbols are labeled alternatives, they use the LabeledExpr.gr
// file.
//


/** The start rule; begin parsing here. */
// NOTE: the `# text` in third column has a special
// meaning to Antlr.  These called `labeled alternatives`.
// Labels appear on the right edge of alternatives and start
// with the # symbol.  They provide separate visitor methods
// for each rule. 
prog:         stat+ ;

stat:         expr NEWLINE                 # printExpr
    |         ID '=' expr NEWLINE          # assign
    |         NEWLINE                      # blank
    ;

expr:         expr op=('*'|'/') expr       # MulDiv
    |         expr op=('+'|'-') expr       # AddSub
    |         INT                          # int
    |         ID                           # id
    |         '(' expr ')'                 # parens
    ;


// This part defines token names for the operator literals
// this allows us to use java constants in the visitor

MUL:     '*' ;
DIV:     '/' ;
ADD:     '+' ;
SUB:     '-' ;




