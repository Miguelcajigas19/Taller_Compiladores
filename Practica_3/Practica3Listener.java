// Generated from Practica3.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link Practica3Parser}.
 */
public interface Practica3Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#query}.
	 * @param ctx the parse tree
	 */
	void enterQuery(Practica3Parser.QueryContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#query}.
	 * @param ctx the parse tree
	 */
	void exitQuery(Practica3Parser.QueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#column_list}.
	 * @param ctx the parse tree
	 */
	void enterColumn_list(Practica3Parser.Column_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#column_list}.
	 * @param ctx the parse tree
	 */
	void exitColumn_list(Practica3Parser.Column_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#column}.
	 * @param ctx the parse tree
	 */
	void enterColumn(Practica3Parser.ColumnContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#column}.
	 * @param ctx the parse tree
	 */
	void exitColumn(Practica3Parser.ColumnContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#table}.
	 * @param ctx the parse tree
	 */
	void enterTable(Practica3Parser.TableContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#table}.
	 * @param ctx the parse tree
	 */
	void exitTable(Practica3Parser.TableContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(Practica3Parser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(Practica3Parser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(Practica3Parser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(Practica3Parser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica3Parser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(Practica3Parser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica3Parser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(Practica3Parser.ValueContext ctx);
}