
import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.Token;

import java.io.FileInputStream;
import java.io.InputStream;
import java.io.*;  // for System.out.print[f|ln]()?


public class Col {

    public static void main(String[] args) throws Exception {

// This is for reading a file?        
//        String inputFile = null;
//        if (args.length > 0) {
//            inputFile = args[0];
//        }
//
//        // Geneeric input stream
//        InputStream is = System.in;
//        if (inputFile != null) {
//            is  = new FileInputStream(inputFile);
//        }
//
//        // ANTLR input stream
//        ANTLRInputStream input = new ANTLRInputStream(is);

// This is for reading stdin?
        // ANTLR input stream
        ANTLRInputStream input = new ANTLRInputStream(System.in);

        //
        // Above here its boilerplate
        //

        // Lexer
        RowsLexer lexer = new RowsLexer(input);

        // Token Stream - this is the same
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        int col = Integer.valueOf(args[0]);  // this is new
        System.out.printf("col: %d%n", col);

        // Parser 
        // This is new, we pas the col to the parser
        RowsParser parser = new RowsParser(tokens, col); // pass column number!

        // This is new.
        parser.setBuildParseTree(false); // Don't waste time building a tree
        parser.file();  // parse


    }

    
}
