import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

public class ExprJoyRide {
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

        // ANTLR input stream
        ANTLRInputStream input = new ANTLRInputStream(is);

        // Lexer
        LibExprLexer lexer = new LibExprLexer(input);

        // Token Stream
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Parser
        LibExprParser parser = new LibExprParser(tokens);

        // Start prarsing
        ParseTree tree = parser.prog(); // parse; start at prog

        // Print the resulting tree
        System.out.println(tree.toStringTree(parser));  // print tree as text
    }
}



