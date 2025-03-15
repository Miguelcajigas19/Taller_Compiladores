// Generated from Practica2.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link Practica2Parser}.
 */
public interface Practica2Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#query}.
	 * @param ctx the parse tree
	 */
	void enterQuery(Practica2Parser.QueryContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#query}.
	 * @param ctx the parse tree
	 */
	void exitQuery(Practica2Parser.QueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#column_list}.
	 * @param ctx the parse tree
	 */
	void enterColumn_list(Practica2Parser.Column_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#column_list}.
	 * @param ctx the parse tree
	 */
	void exitColumn_list(Practica2Parser.Column_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#column}.
	 * @param ctx the parse tree
	 */
	void enterColumn(Practica2Parser.ColumnContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#column}.
	 * @param ctx the parse tree
	 */
	void exitColumn(Practica2Parser.ColumnContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#table}.
	 * @param ctx the parse tree
	 */
	void enterTable(Practica2Parser.TableContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#table}.
	 * @param ctx the parse tree
	 */
	void exitTable(Practica2Parser.TableContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(Practica2Parser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(Practica2Parser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(Practica2Parser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(Practica2Parser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link Practica2Parser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(Practica2Parser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link Practica2Parser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(Practica2Parser.ValueContext ctx);
}