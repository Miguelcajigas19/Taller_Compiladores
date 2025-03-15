# Generated from Practica3.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Practica3Parser import Practica3Parser
else:
    from Practica3Parser import Practica3Parser

# This class defines a complete listener for a parse tree produced by Practica3Parser.
class Practica3Listener(ParseTreeListener):

    # Enter a parse tree produced by Practica3Parser#query.
    def enterQuery(self, ctx:Practica3Parser.QueryContext):
        pass

    # Exit a parse tree produced by Practica3Parser#query.
    def exitQuery(self, ctx:Practica3Parser.QueryContext):
        pass


    # Enter a parse tree produced by Practica3Parser#column_list.
    def enterColumn_list(self, ctx:Practica3Parser.Column_listContext):
        pass

    # Exit a parse tree produced by Practica3Parser#column_list.
    def exitColumn_list(self, ctx:Practica3Parser.Column_listContext):
        pass


    # Enter a parse tree produced by Practica3Parser#column.
    def enterColumn(self, ctx:Practica3Parser.ColumnContext):
        pass

    # Exit a parse tree produced by Practica3Parser#column.
    def exitColumn(self, ctx:Practica3Parser.ColumnContext):
        pass


    # Enter a parse tree produced by Practica3Parser#table.
    def enterTable(self, ctx:Practica3Parser.TableContext):
        pass

    # Exit a parse tree produced by Practica3Parser#table.
    def exitTable(self, ctx:Practica3Parser.TableContext):
        pass


    # Enter a parse tree produced by Practica3Parser#condition.
    def enterCondition(self, ctx:Practica3Parser.ConditionContext):
        pass

    # Exit a parse tree produced by Practica3Parser#condition.
    def exitCondition(self, ctx:Practica3Parser.ConditionContext):
        pass


    # Enter a parse tree produced by Practica3Parser#operator.
    def enterOperator(self, ctx:Practica3Parser.OperatorContext):
        pass

    # Exit a parse tree produced by Practica3Parser#operator.
    def exitOperator(self, ctx:Practica3Parser.OperatorContext):
        pass


    # Enter a parse tree produced by Practica3Parser#value.
    def enterValue(self, ctx:Practica3Parser.ValueContext):
        pass

    # Exit a parse tree produced by Practica3Parser#value.
    def exitValue(self, ctx:Practica3Parser.ValueContext):
        pass



del Practica3Parser