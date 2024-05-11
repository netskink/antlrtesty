
import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.tree.*;

import java.io.FileInputStream;
import java.io.InputStream;


public class InsertSerialID {

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
        JavaLexer lexer = new JavaLexer(input);

        // Token Stream - this is the same
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Parser 
        JavaParser parser = new JavaParser(tokens);

        // Start prarsing - this is the same
        ParseTree tree = parser.compilationUnit(); // parse; start at compilationUnit


        ParseTreeWalker walker = new ParseTreeWalker();  // create standard walker
        // This uses the new listener and it uses the tokens rather than the parser
        InsertSerialIDListener extractor = new InsertSerialIDListener(tokens);
        walker.walk(extractor, tree);

        // This is new for InsertSerialID
        System.out.println(extractor.rewriter.getText());


    }

    
}
