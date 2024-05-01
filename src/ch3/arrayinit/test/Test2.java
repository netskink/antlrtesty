import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

public class Test2 {
    public static void main(String[] args) throws Exception {
        String inputFile = null;
        if (args.length > 0) {
            inputFile = args[0];
        }

        // Geneeric input stream
        InputStream is = System.in;
        if (inputFile != null) {
            is  = new FileInputStream(inputFile);
        }

        // ANTLR 
        // Creates a CharStream that reads from standard input
        ANTLRInputStream input = new ANTLRInputStream(is);
        // in the actual code sample instead of the first two lines
        // it uses System.in rather than is

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
        System.out.println(tree.toStringTree(parser));  // print tree as text
    }
}



