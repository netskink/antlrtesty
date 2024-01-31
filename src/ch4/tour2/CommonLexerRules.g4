lexer grammar CommonLexerRules;  // Note: "lexer grammar"


// Notice the newline has an optional carriage return
// followed by a new-line.
ID :          [a-zA-Z]+ ;        // match identifiers
INT :         [0-9]+ ;           // match integers
NEWLINE:      '\r'? '\n';        // return newlines to parser (is end-statement signal)
WS:           [ \t]+   -> skip ; // toss out whitespace



