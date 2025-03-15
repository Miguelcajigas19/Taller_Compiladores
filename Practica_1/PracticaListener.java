// Generated from Practica.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PracticaParser}.
 */
public interface PracticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PracticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(PracticaParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PracticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(PracticaParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PracticaParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void enterSentencia(PracticaParser.SentenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PracticaParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void exitSentencia(PracticaParser.SentenciaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link PracticaParser#ifElseStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(PracticaParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfElse}
	 * labeled alternative in {@link PracticaParser#ifElseStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(PracticaParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CondicionSimple}
	 * labeled alternative in {@link PracticaParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicionSimple(PracticaParser.CondicionSimpleContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CondicionSimple}
	 * labeled alternative in {@link PracticaParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicionSimple(PracticaParser.CondicionSimpleContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Assign}
	 * labeled alternative in {@link PracticaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAssign(PracticaParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Assign}
	 * labeled alternative in {@link PracticaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAssign(PracticaParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterVariable(PracticaParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitVariable(PracticaParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(PracticaParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(PracticaParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(PracticaParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(PracticaParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterParens(PracticaParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitParens(PracticaParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Int}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterInt(PracticaParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Int}
	 * labeled alternative in {@link PracticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitInt(PracticaParser.IntContext ctx);
}