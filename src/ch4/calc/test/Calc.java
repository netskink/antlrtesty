

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

public class Calc {
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

        //
        // Above here its boilerplate
        //

        // Lexer
        LabeledExprLexer lexer = new LabeledExprLexer(input);

        // Token Stream - this is the same
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Parser 
        LabeledExprParser parser = new LabeledExprParser(tokens);

        // Start prarsing - this is the same
        ParseTree tree = parser.prog(); // parse; start at prog

        // This is new
        EvalVisitor eval = new EvalVisitor();
        eval.visit(tree);


        // This is no longer used.
        // Print the resulting tree
        //System.out.println(tree.toStringTree(parser));  // print tree as text
    }
}

