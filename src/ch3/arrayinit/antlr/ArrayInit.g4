
/** Grammars always start with a grammar header.  This grammar
is called ArrayInit and it must match the filename ArrayInit.g4 */
grammar ArrayInit;              // Define a grammar called ArrayInit

/*
 * Parser Rules
 */

/** parser rules start with lowercase letters */
/** A rule called init that matches comma-separated values between {...} */
init  : '{' value (',' value)* '}' ; // must match at least one value

/** A value can be either a nested array/struct or a simpmle integer (INT) */
value : init
      | INT
      ;


/*
 * Lexer Rules
 */

/** lexer rules consist of all uppercase letters */
INT  :  [0-9]+  ;            // Define token INT as one or more digits
WS   :  [ \t\r\n]+ -> skip;  // Define whitespace rule, toss it out




