grammar DOT;

// 
STRICT       : [Ss] [Tt] [Rr] [Ii] [Cc] [Tt] ;
GRAPH        : [Gg] [Rr] [Aa] [Pp] [Hh] ;
DIGRAPH      : [Dd] [Ii] [Gg] [Rr] [Aa] [Pp] [Hh] ;
NODE         : [Nn] [Oo] [Dd] [Ee] ;
EDGE         : [Ed] [Dd] [Gg] [Ee] ;
SUBGRAPH     : [Ss] [Uu] [Bb] [Gg] [Aa] [Pp] [Hh] ;

ID           : LETTER (LETTER|DIGIT)* ;
fragment
LETTER       : [a-zA-Z\u0080-\u00FF_] ;

NUMBER       : '-'? ('.' DIGIT+ | DIGIT+ ('.' DIGIT*)? ) ;
fragment
DIGIT        : [0-9] ;

STRING       : '"' ('\\"'|.)*? '"' ;

HTML_STRING  : '<' (TAG|~[<>])* '>' ;
fragment
TAG          : '<' .*? '>' ;

PREPROC      : '#' .*? '\n' -> skip ;





