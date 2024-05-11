
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
* actions - section 4.4 (first half) making things happen during parse
    - uses a tsv file as input to parse
* actions2 - section 4.4 (second half)
    - uses a file containing a sequence 
* xmllexer - section 4.5 (first third)
    - Island Grammars: dealing with Different Formats in the Same File
    - Island Grammars are like a mini language inside a larger language
        - @author tags inside Java Comment lines.
        - Antlr has a lexical mode capability where it can switch modes
          based upon a special sentinel character sequence.
        - XML has a similar capability.  When XML sees a `<`, it
          switches to `inside` mode and switches back to `default` mode
          when it sees `>` or `/>`.
    - This example is lexer grammar and not the normal grammar.  
        - When built it does not make a xxxGrammar.java or xxxLexer.java

    

# URLS

* [ninja manual](https://ninja-build.org/manual.html#_comparison_to_make)
* [ninja guide](https://spectra.mathpix.com/article/2024.01.00364/a-complete-guide-to-the-ninja-build-system)

# usage

Replace ch4/tour with whatever you wish: tour, tour2, ...

```
$ cd bin
$ . ./setenv.sh
$ cd ..
$ cd src/ch4/tour
$ ninja
```

## list available targets

```
$ ninja -t targets
```

## run a particular target

```
$ ninja do_test3
```

## clean all targets

```
$ ninja -t clean
```
