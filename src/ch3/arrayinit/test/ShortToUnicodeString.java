import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;


/** This code extends listner so that we can do custom
 * operations when particular phrases are encountered
 * hence it extends ArrayInit - our grammar - base listener.
 */
public class ShortToUnicodeString extends ArrayInitBaseListener {
    /** Translate { to " 
    */
    @Override
    public void enterInit(ArrayInitParser.InitContext ctx) {
        System.out.print('"');
    }
    /** Translate } to " 
    */
    @Override
    public void exitInit(ArrayInitParser.InitContext ctx) {
        System.out.print('"');
    }
    /** Translate integers to 4-digit hexadecimal strings
     * prefixed with ||u
     */
    @Override
    public void enterValue(ArrayInitParser.ValueContext ctx) {
        // assumes no neted array initialization
        int value = Integer.valueOf(ctx.INT().getText());
        System.out.printf("\\u%04x",value);
    }
}



