# Generated from Practica3.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\5\3$\n\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\2\2\t\2")
        buf.write("\4\6\b\n\f\16\2\4\3\2\t\16\3\2\20\21\2-\2\20\3\2\2\2\4")
        buf.write("#\3\2\2\2\6%\3\2\2\2\b\'\3\2\2\2\n)\3\2\2\2\f-\3\2\2\2")
        buf.write("\16/\3\2\2\2\20\21\7\3\2\2\21\22\5\4\3\2\22\23\7\4\2\2")
        buf.write("\23\26\5\b\5\2\24\25\7\5\2\2\25\27\5\n\6\2\26\24\3\2\2")
        buf.write("\2\26\27\3\2\2\2\27\30\3\2\2\2\30\31\7\b\2\2\31\3\3\2")
        buf.write("\2\2\32$\7\6\2\2\33 \5\6\4\2\34\35\7\7\2\2\35\37\5\6\4")
        buf.write("\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!$")
        buf.write("\3\2\2\2\" \3\2\2\2#\32\3\2\2\2#\33\3\2\2\2$\5\3\2\2\2")
        buf.write("%&\7\17\2\2&\7\3\2\2\2\'(\7\17\2\2(\t\3\2\2\2)*\5\6\4")
        buf.write("\2*+\5\f\7\2+,\5\16\b\2,\13\3\2\2\2-.\t\2\2\2.\r\3\2\2")
        buf.write("\2/\60\t\3\2\2\60\17\3\2\2\2\5\26 #")
        return buf.getvalue()


class Practica3Parser ( Parser ):

    grammarFileName = "Practica3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'WHERE'", "'*'", 
                     "','", "';'", "'>'", "'<'", "'='", "'>='", "'<='", 
                     "'!='" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "STAR", "COMMA", 
                      "SEMI", "GT", "LT", "EQ", "GE", "LE", "NE", "IDENTIFIER", 
                      "NUMBER", "STRING", "WS" ]

    RULE_query = 0
    RULE_column_list = 1
    RULE_column = 2
    RULE_table = 3
    RULE_condition = 4
    RULE_operator = 5
    RULE_value = 6

    ruleNames =  [ "query", "column_list", "column", "table", "condition", 
                   "operator", "value" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    STAR=4
    COMMA=5
    SEMI=6
    GT=7
    LT=8
    EQ=9
    GE=10
    LE=11
    NE=12
    IDENTIFIER=13
    NUMBER=14
    STRING=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(Practica3Parser.SELECT, 0)

        def column_list(self):
            return self.getTypedRuleContext(Practica3Parser.Column_listContext,0)


        def FROM(self):
            return self.getToken(Practica3Parser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(Practica3Parser.TableContext,0)


        def SEMI(self):
            return self.getToken(Practica3Parser.SEMI, 0)

        def WHERE(self):
            return self.getToken(Practica3Parser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(Practica3Parser.ConditionContext,0)


        def getRuleIndex(self):
            return Practica3Parser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = Practica3Parser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(Practica3Parser.SELECT)
            self.state = 15
            self.column_list()
            self.state = 16
            self.match(Practica3Parser.FROM)
            self.state = 17
            self.table()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Practica3Parser.WHERE:
                self.state = 18
                self.match(Practica3Parser.WHERE)
                self.state = 19
                self.condition()


            self.state = 22
            self.match(Practica3Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(Practica3Parser.STAR, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Practica3Parser.ColumnContext)
            else:
                return self.getTypedRuleContext(Practica3Parser.ColumnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Practica3Parser.COMMA)
            else:
                return self.getToken(Practica3Parser.COMMA, i)

        def getRuleIndex(self):
            return Practica3Parser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = Practica3Parser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Practica3Parser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(Practica3Parser.STAR)
                pass
            elif token in [Practica3Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.column()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Practica3Parser.COMMA:
                    self.state = 26
                    self.match(Practica3Parser.COMMA)
                    self.state = 27
                    self.column()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Practica3Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Practica3Parser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = Practica3Parser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(Practica3Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Practica3Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Practica3Parser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = Practica3Parser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(Practica3Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(Practica3Parser.ColumnContext,0)


        def operator(self):
            return self.getTypedRuleContext(Practica3Parser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(Practica3Parser.ValueContext,0)


        def getRuleIndex(self):
            return Practica3Parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = Practica3Parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.column()
            self.state = 40
            self.operator()
            self.state = 41
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(Practica3Parser.GT, 0)

        def LT(self):
            return self.getToken(Practica3Parser.LT, 0)

        def EQ(self):
            return self.getToken(Practica3Parser.EQ, 0)

        def GE(self):
            return self.getToken(Practica3Parser.GE, 0)

        def LE(self):
            return self.getToken(Practica3Parser.LE, 0)

        def NE(self):
            return self.getToken(Practica3Parser.NE, 0)

        def getRuleIndex(self):
            return Practica3Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = Practica3Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Practica3Parser.GT) | (1 << Practica3Parser.LT) | (1 << Practica3Parser.EQ) | (1 << Practica3Parser.GE) | (1 << Practica3Parser.LE) | (1 << Practica3Parser.NE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Practica3Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(Practica3Parser.STRING, 0)

        def getRuleIndex(self):
            return Practica3Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = Practica3Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(_la==Practica3Parser.NUMBER or _la==Practica3Parser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





