
# notes on chapter 4

These are the exercises from ch 4.

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

# usage

Replace ch4/tour with whatever you wish: tour, tour2, ...

```
$ cd bin
$ . ./setenv.sh
$ cd ..
$ cd src/ch4/tour
$ ninja
```