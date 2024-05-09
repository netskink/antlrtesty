grammar Rows;

// This is new.  Its a constructor and the cols start counting
// at col=1.
// The members action injects code into the member area
// of the generated parser class.  
@parser::members { // add members to generated RowsParser
    int col;
    public RowsParser(TokenStream input, int col) { // custom constructor
        this(input);
        this.col = col;
    }
}

file: (row NL)+;

// This is new. It adds an action inside of a rule.
// Actions are code snippets surrounded by curly braces.
// The action within the fule row accesses $i, the local
// variable defined with the locals clause.  It also
// uses the $STUFF.text to get the text for the most
// recently matched STUFF token.
row
locals [int i=0]
    : (     STUFF
            {
            $i++;
            if ( $i == col ) System.out.println($STUFF.text);
            }
      )+
    ;


// The STUFF lexical rule matches anything that's not a tab
// or a newline which means we can have space characters in a column.
TAB     : '\t' -> skip  ;       // match but dont pass to the parser
//NL      : '\r'? '\n'    ;       // match and pass to the parser
//STUFF   : ~[\t\r\n]+    ;       // match any chars except tab, newline
NL      : '\n'    ;       // match and pass to the parser
STUFF   : ~[\t\n]+    ;       // match any chars except tab, newline

