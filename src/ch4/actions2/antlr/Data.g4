grammar Data;

file    : group+ ;

group   : INT sequence[$INT.int] ;



// This has a special boolean -valued action called
// semantic predicate: {$i<=$n}?
// That predicate evaluates to true until
// we surpass the number of integers requested by the sequence
// rule parameter n.
// False predicates make the associated alternative "disappear"
// from the grammar and, hence, from the generated parser.  In 
// this case, a false predicate makes the (...)* loop terminate
// and return from rule sequence.
sequence[int n]
locals [int i = 1;]
        : ( {$i<=$n}? INT {$i++;} )*    // match n integers
        ;

INT     : [0-9]+ ;                  // match integers
WS      : [ \t\n\r]+ -> skip ;      // toss out all whitespace

