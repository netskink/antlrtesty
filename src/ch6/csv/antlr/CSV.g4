grammar CSV;

// a file has a header row which is just a row
// but because its a rename it can be hooked when
// identified.
file    : hdr row+                          ;
hdr     : row                               ;

// rows have fields separated by commas and end 
// with a newline and on windows an optional
// of carriage return and new line.
row     : field (',' field)* '\r'? '\n'     ;

// fields can be either text, strings or blanks.
field   : TEXT
        | STRING
        |
        ;

// Text is anything other than a comma, carriage return
// new line or a double-quote
TEXT    : ~[,\n\r"]+                        ;

// Strings use quote-quote to make an escaped quote
STRING  : '"' ('""'|~'"')* '"'              ;

