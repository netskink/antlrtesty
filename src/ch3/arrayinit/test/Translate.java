import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Translate {
    public static void main(String[] args) throws Exception {

        // ANTLR 
        // Creates a CharStream that reads from standard input
        ANTLRInputStream input = new ANTLRInputStream(System.in);

        // Lexer
        // Creates a lexer that feeds off of input CharStream
        ArrayInitLexer lexer = new ArrayInitLexer(input);

        // Token Stream
        // Creates a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Parser
        // Creates a parser that feeds off the tokens buffer
        ArrayInitParser parser = new ArrayInitParser(tokens);

        // Start prarsing
        // begin parsing at init rule, hence init()
        ParseTree tree = parser.init(); // parse; start at init

        // Print the resulting tree
        // print lisp style tree
        //System.out.println(tree.toStringTree(parser));  // print tree as text

        // Create a generic parse tree walker that can trigger callbacks.
        // a walker uses the parser listener to issue callbacks when
        // various phrases are recognized.
        ParseTreeWalker walker = new ParseTreeWalker();
        // Walk the tree created during the parse, trigger callbacks
        walker.walk(new ShortToUnicodeString(), tree);
        System.out.println(); // print a \n after translation
    }
}



