// Generated from d:\zfh\大三上\汇编与编译原理\编译大作业\CPPToLLVM\grammar\cpp2llvmParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class cpp2llvmParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IntegerLiteral=1, CharacterLiteral=2, FloatingLiteral=3, StringLiteral=4, 
		BooleanLiteral=5, PointerLiteral=6, Directive=7, Alignas=8, Alignof=9, 
		Asm=10, Auto=11, Bool=12, Break=13, Case=14, Catch=15, Char=16, Char16=17, 
		Char32=18, Class=19, Const=20, Constexpr=21, Const_cast=22, Continue=23, 
		Decltype=24, Default=25, Delete=26, Do=27, Double=28, Dynamic_cast=29, 
		Else=30, Enum=31, Explicit=32, Export=33, Extern=34, False_=35, Final=36, 
		Float=37, For=38, Friend=39, Goto=40, If=41, Inline=42, Int=43, Long=44, 
		Mutable=45, Namespace=46, New=47, Noexcept=48, Nullptr=49, Operator=50, 
		Override=51, Private=52, Protected=53, Public=54, Register=55, Reinterpret_cast=56, 
		Return=57, Short=58, Signed=59, Sizeof=60, Static=61, Static_assert=62, 
		Static_cast=63, Struct=64, Switch=65, Template=66, This=67, Thread_local=68, 
		Throw=69, True_=70, Try=71, Typedef=72, Typeid_=73, Typename_=74, Union=75, 
		Unsigned=76, Using=77, Virtual=78, Void=79, Volatile=80, Wchar=81, While=82, 
		LeftParen=83, RightParen=84, LeftBracket=85, RightBracket=86, LeftBrace=87, 
		RightBrace=88, Plus=89, Minus=90, Star=91, Div=92, Mod=93, Caret=94, And=95, 
		Or=96, Tilde=97, Not=98, Assign=99, Less=100, Greater=101, PlusAssign=102, 
		MinusAssign=103, StarAssign=104, DivAssign=105, ModAssign=106, XorAssign=107, 
		AndAssign=108, OrAssign=109, LeftShift=110, LeftShiftAssign=111, RightShift=112, 
		RightShiftAssign=113, Equal=114, NotEqual=115, LessEqual=116, GreaterEqual=117, 
		AndAnd=118, OrOr=119, PlusPlus=120, MinusMinus=121, Comma=122, ArrowStar=123, 
		Arrow=124, Question=125, Colon=126, Doublecolon=127, Semi=128, Dot=129, 
		DotStar=130, Ellipsis=131, Identifier=132, DecimalLiteral=133, OctalLiteral=134, 
		HexadecimalLiteral=135, BinaryLiteral=136, Integersuffix=137, Whitespace=138, 
		Newline=139, BlockComment=140, LineComment=141;
	public static final int
		RULE_literal = 0, RULE_translationUnit = 1, RULE_stringLiteral = 2, RULE_constExpression = 3, 
		RULE_leftExpression = 4, RULE_expression = 5, RULE_functionCall = 6, RULE_condition = 7, 
		RULE_statement = 8, RULE_expressionStatement = 9, RULE_compoundStatement = 10, 
		RULE_caseStatement = 11, RULE_selectionStatement = 12, RULE_iterationStatement = 13, 
		RULE_jumpStatement = 14, RULE_declaration = 15, RULE_variableDeclarator = 16, 
		RULE_variableDeclarationList = 17, RULE_variableDeclaration = 18, RULE_varDeclWithoutInit = 19, 
		RULE_varDeclWithConstInit = 20, RULE_varDeclWithNormalInit = 21, RULE_arrayDeclarator = 22, 
		RULE_normalArrayDeclaration = 23, RULE_arrayAssginExpressionList = 24, 
		RULE_stringDeclaration = 25, RULE_arrayName = 26, RULE_functionDeclarator = 27, 
		RULE_functionDeclaration = 28, RULE_functionDefinition = 29, RULE_functionHead = 30, 
		RULE_functionParameterList = 31, RULE_functionParameter = 32, RULE_typeModifier = 33, 
		RULE_pointerTypeModifier = 34, RULE_normalTypeModifier = 35, RULE_integerTypeModifier = 36, 
		RULE_realTypeModifier = 37, RULE_boolTypeModifier = 38, RULE_charTypeModifier = 39, 
		RULE_voidTypeModifier = 40;
	private static String[] makeRuleNames() {
		return new String[] {
			"literal", "translationUnit", "stringLiteral", "constExpression", "leftExpression", 
			"expression", "functionCall", "condition", "statement", "expressionStatement", 
			"compoundStatement", "caseStatement", "selectionStatement", "iterationStatement", 
			"jumpStatement", "declaration", "variableDeclarator", "variableDeclarationList", 
			"variableDeclaration", "varDeclWithoutInit", "varDeclWithConstInit", 
			"varDeclWithNormalInit", "arrayDeclarator", "normalArrayDeclaration", 
			"arrayAssginExpressionList", "stringDeclaration", "arrayName", "functionDeclarator", 
			"functionDeclaration", "functionDefinition", "functionHead", "functionParameterList", 
			"functionParameter", "typeModifier", "pointerTypeModifier", "normalTypeModifier", 
			"integerTypeModifier", "realTypeModifier", "boolTypeModifier", "charTypeModifier", 
			"voidTypeModifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'alignas'", "'alignof'", 
			"'asm'", "'auto'", "'bool'", "'break'", "'case'", "'catch'", "'char'", 
			"'char16_t'", "'char32_t'", "'class'", "'const'", "'constexpr'", "'const_cast'", 
			"'continue'", "'decltype'", "'default'", "'delete'", "'do'", "'double'", 
			"'dynamic_cast'", "'else'", "'enum'", "'explicit'", "'export'", "'extern'", 
			"'false'", "'final'", "'float'", "'for'", "'friend'", "'goto'", "'if'", 
			"'inline'", "'int'", "'long'", "'mutable'", "'namespace'", "'new'", "'noexcept'", 
			"'nullptr'", "'operator'", "'override'", "'private'", "'protected'", 
			"'public'", "'register'", "'reinterpret_cast'", "'return'", "'short'", 
			"'signed'", "'sizeof'", "'static'", "'static_assert'", "'static_cast'", 
			"'struct'", "'switch'", "'template'", "'this'", "'thread_local'", "'throw'", 
			"'true'", "'try'", "'typedef'", "'typeid'", "'typename'", "'union'", 
			"'unsigned'", "'using'", "'virtual'", "'void'", "'volatile'", "'wchar_t'", 
			"'while'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'+'", "'-'", "'*'", 
			"'/'", "'%'", "'^'", "'&'", "'|'", "'~'", null, "'='", "'<'", "'>'", 
			"'+='", "'-='", "'*='", "'/='", "'%='", "'^='", "'&='", "'|='", "'<<'", 
			"'<<='", "'>>'", "'>>='", "'=='", "'!='", "'<='", "'>='", null, null, 
			"'++'", "'--'", "','", "'->*'", "'->'", "'?'", "':'", "'::'", "';'", 
			"'.'", "'.*'", "'...'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IntegerLiteral", "CharacterLiteral", "FloatingLiteral", "StringLiteral", 
			"BooleanLiteral", "PointerLiteral", "Directive", "Alignas", "Alignof", 
			"Asm", "Auto", "Bool", "Break", "Case", "Catch", "Char", "Char16", "Char32", 
			"Class", "Const", "Constexpr", "Const_cast", "Continue", "Decltype", 
			"Default", "Delete", "Do", "Double", "Dynamic_cast", "Else", "Enum", 
			"Explicit", "Export", "Extern", "False_", "Final", "Float", "For", "Friend", 
			"Goto", "If", "Inline", "Int", "Long", "Mutable", "Namespace", "New", 
			"Noexcept", "Nullptr", "Operator", "Override", "Private", "Protected", 
			"Public", "Register", "Reinterpret_cast", "Return", "Short", "Signed", 
			"Sizeof", "Static", "Static_assert", "Static_cast", "Struct", "Switch", 
			"Template", "This", "Thread_local", "Throw", "True_", "Try", "Typedef", 
			"Typeid_", "Typename_", "Union", "Unsigned", "Using", "Virtual", "Void", 
			"Volatile", "Wchar", "While", "LeftParen", "RightParen", "LeftBracket", 
			"RightBracket", "LeftBrace", "RightBrace", "Plus", "Minus", "Star", "Div", 
			"Mod", "Caret", "And", "Or", "Tilde", "Not", "Assign", "Less", "Greater", 
			"PlusAssign", "MinusAssign", "StarAssign", "DivAssign", "ModAssign", 
			"XorAssign", "AndAssign", "OrAssign", "LeftShift", "LeftShiftAssign", 
			"RightShift", "RightShiftAssign", "Equal", "NotEqual", "LessEqual", "GreaterEqual", 
			"AndAnd", "OrOr", "PlusPlus", "MinusMinus", "Comma", "ArrowStar", "Arrow", 
			"Question", "Colon", "Doublecolon", "Semi", "Dot", "DotStar", "Ellipsis", 
			"Identifier", "DecimalLiteral", "OctalLiteral", "HexadecimalLiteral", 
			"BinaryLiteral", "Integersuffix", "Whitespace", "Newline", "BlockComment", 
			"LineComment"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "cpp2llvmParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public cpp2llvmParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode IntegerLiteral() { return getToken(cpp2llvmParser.IntegerLiteral, 0); }
		public TerminalNode CharacterLiteral() { return getToken(cpp2llvmParser.CharacterLiteral, 0); }
		public TerminalNode FloatingLiteral() { return getToken(cpp2llvmParser.FloatingLiteral, 0); }
		public TerminalNode StringLiteral() { return getToken(cpp2llvmParser.StringLiteral, 0); }
		public TerminalNode BooleanLiteral() { return getToken(cpp2llvmParser.BooleanLiteral, 0); }
		public TerminalNode PointerLiteral() { return getToken(cpp2llvmParser.PointerLiteral, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TranslationUnitContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(cpp2llvmParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public TranslationUnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_translationUnit; }
	}

	public final TranslationUnitContext translationUnit() throws RecognitionException {
		TranslationUnitContext _localctx = new TranslationUnitContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_translationUnit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Bool) | (1L << Char) | (1L << Double) | (1L << Float) | (1L << Int) | (1L << Long) | (1L << Short))) != 0) || _la==Void) {
				{
				{
				setState(84);
				declaration();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringLiteralContext extends ParserRuleContext {
		public TerminalNode StringLiteral() { return getToken(cpp2llvmParser.StringLiteral, 0); }
		public StringLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringLiteral; }
	}

	public final StringLiteralContext stringLiteral() throws RecognitionException {
		StringLiteralContext _localctx = new StringLiteralContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stringLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(StringLiteral);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstExpressionContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ConstExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constExpression; }
	}

	public final ConstExpressionContext constExpression() throws RecognitionException {
		ConstExpressionContext _localctx = new ConstExpressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_constExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			literal();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LeftExpressionContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode LeftBracket() { return getToken(cpp2llvmParser.LeftBracket, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RightBracket() { return getToken(cpp2llvmParser.RightBracket, 0); }
		public LeftExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leftExpression; }
	}

	public final LeftExpressionContext leftExpression() throws RecognitionException {
		LeftExpressionContext _localctx = new LeftExpressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_leftExpression);
		try {
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				match(Identifier);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(97);
				match(Identifier);
				{
				setState(98);
				match(LeftBracket);
				setState(99);
				expression(0);
				setState(100);
				match(RightBracket);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public TerminalNode Not() { return getToken(cpp2llvmParser.Not, 0); }
		public TerminalNode Minus() { return getToken(cpp2llvmParser.Minus, 0); }
		public TerminalNode And() { return getToken(cpp2llvmParser.And, 0); }
		public LeftExpressionContext leftExpression() {
			return getRuleContext(LeftExpressionContext.class,0);
		}
		public TerminalNode LeftBracket() { return getToken(cpp2llvmParser.LeftBracket, 0); }
		public TerminalNode RightBracket() { return getToken(cpp2llvmParser.RightBracket, 0); }
		public TerminalNode Assign() { return getToken(cpp2llvmParser.Assign, 0); }
		public TerminalNode PlusPlus() { return getToken(cpp2llvmParser.PlusPlus, 0); }
		public TerminalNode MinusMinus() { return getToken(cpp2llvmParser.MinusMinus, 0); }
		public TerminalNode Star() { return getToken(cpp2llvmParser.Star, 0); }
		public TerminalNode Div() { return getToken(cpp2llvmParser.Div, 0); }
		public TerminalNode Mod() { return getToken(cpp2llvmParser.Mod, 0); }
		public TerminalNode Plus() { return getToken(cpp2llvmParser.Plus, 0); }
		public TerminalNode Less() { return getToken(cpp2llvmParser.Less, 0); }
		public TerminalNode Greater() { return getToken(cpp2llvmParser.Greater, 0); }
		public TerminalNode LessEqual() { return getToken(cpp2llvmParser.LessEqual, 0); }
		public TerminalNode GreaterEqual() { return getToken(cpp2llvmParser.GreaterEqual, 0); }
		public TerminalNode Equal() { return getToken(cpp2llvmParser.Equal, 0); }
		public TerminalNode NotEqual() { return getToken(cpp2llvmParser.NotEqual, 0); }
		public TerminalNode Or() { return getToken(cpp2llvmParser.Or, 0); }
		public TerminalNode Caret() { return getToken(cpp2llvmParser.Caret, 0); }
		public TerminalNode OrOr() { return getToken(cpp2llvmParser.OrOr, 0); }
		public TerminalNode AndAnd() { return getToken(cpp2llvmParser.AndAnd, 0); }
		public TerminalNode LeftShift() { return getToken(cpp2llvmParser.LeftShift, 0); }
		public TerminalNode RightShift() { return getToken(cpp2llvmParser.RightShift, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(105);
				functionCall();
				}
				break;
			case 2:
				{
				setState(106);
				literal();
				}
				break;
			case 3:
				{
				setState(107);
				match(Identifier);
				}
				break;
			case 4:
				{
				setState(108);
				match(LeftParen);
				setState(109);
				expression(0);
				setState(110);
				match(RightParen);
				}
				break;
			case 5:
				{
				setState(112);
				match(Not);
				setState(113);
				expression(25);
				}
				break;
			case 6:
				{
				setState(114);
				match(Minus);
				setState(115);
				expression(24);
				}
				break;
			case 7:
				{
				setState(116);
				match(And);
				setState(117);
				leftExpression();
				}
				break;
			case 8:
				{
				setState(118);
				match(Identifier);
				setState(119);
				match(LeftBracket);
				setState(120);
				expression(0);
				setState(121);
				match(RightBracket);
				}
				break;
			case 9:
				{
				setState(123);
				leftExpression();
				setState(124);
				match(Assign);
				setState(125);
				expression(3);
				}
				break;
			case 10:
				{
				setState(127);
				leftExpression();
				setState(128);
				match(PlusPlus);
				}
				break;
			case 11:
				{
				setState(130);
				leftExpression();
				setState(131);
				match(MinusMinus);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(191);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(189);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(135);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(136);
						match(Star);
						setState(137);
						expression(23);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(138);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(139);
						match(Div);
						setState(140);
						expression(22);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(141);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(142);
						match(Mod);
						setState(143);
						expression(21);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(144);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(145);
						match(Plus);
						setState(146);
						expression(20);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(147);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(148);
						match(Minus);
						setState(149);
						expression(19);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(150);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(151);
						match(Less);
						setState(152);
						expression(18);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(153);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(154);
						match(Greater);
						setState(155);
						expression(17);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(156);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(157);
						match(LessEqual);
						setState(158);
						expression(16);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(159);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(160);
						match(GreaterEqual);
						setState(161);
						expression(15);
						}
						break;
					case 10:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(162);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(163);
						match(Equal);
						setState(164);
						expression(14);
						}
						break;
					case 11:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(165);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(166);
						match(NotEqual);
						setState(167);
						expression(13);
						}
						break;
					case 12:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(168);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(169);
						match(Or);
						setState(170);
						expression(12);
						}
						break;
					case 13:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(171);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(172);
						match(And);
						setState(173);
						expression(11);
						}
						break;
					case 14:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(174);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(175);
						match(Caret);
						setState(176);
						expression(10);
						}
						break;
					case 15:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(177);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(178);
						match(OrOr);
						setState(179);
						expression(9);
						}
						break;
					case 16:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(180);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(181);
						match(AndAnd);
						setState(182);
						expression(8);
						}
						break;
					case 17:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(183);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(184);
						match(LeftShift);
						setState(185);
						expression(7);
						}
						break;
					case 18:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(186);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(187);
						match(RightShift);
						setState(188);
						expression(6);
						}
						break;
					}
					} 
				}
				setState(193);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> Comma() { return getTokens(cpp2llvmParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(cpp2llvmParser.Comma, i);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(Identifier);
			setState(195);
			match(LeftParen);
			setState(204);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(196);
				expression(0);
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Comma) {
					{
					{
					setState(197);
					match(Comma);
					setState(198);
					expression(0);
					}
					}
					setState(203);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(206);
			match(RightParen);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public SelectionStatementContext selectionStatement() {
			return getRuleContext(SelectionStatementContext.class,0);
		}
		public IterationStatementContext iterationStatement() {
			return getRuleContext(IterationStatementContext.class,0);
		}
		public JumpStatementContext jumpStatement() {
			return getRuleContext(JumpStatementContext.class,0);
		}
		public VariableDeclaratorContext variableDeclarator() {
			return getRuleContext(VariableDeclaratorContext.class,0);
		}
		public ArrayDeclaratorContext arrayDeclarator() {
			return getRuleContext(ArrayDeclaratorContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statement);
		try {
			setState(217);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(210);
				expressionStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
				compoundStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(212);
				selectionStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(213);
				iterationStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(214);
				jumpStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(215);
				variableDeclarator();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(216);
				arrayDeclarator();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionStatementContext extends ParserRuleContext {
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionStatement; }
	}

	public final ExpressionStatementContext expressionStatement() throws RecognitionException {
		ExpressionStatementContext _localctx = new ExpressionStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expressionStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(219);
				expression(0);
				}
			}

			setState(222);
			match(Semi);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompoundStatementContext extends ParserRuleContext {
		public TerminalNode LeftBrace() { return getToken(cpp2llvmParser.LeftBrace, 0); }
		public TerminalNode RightBrace() { return getToken(cpp2llvmParser.RightBrace, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CompoundStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundStatement; }
	}

	public final CompoundStatementContext compoundStatement() throws RecognitionException {
		CompoundStatementContext _localctx = new CompoundStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_compoundStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(LeftBrace);
			setState(228);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral) | (1L << Bool) | (1L << Break) | (1L << Char) | (1L << Continue) | (1L << Do) | (1L << Double) | (1L << Float) | (1L << For) | (1L << Goto) | (1L << If) | (1L << Int) | (1L << Long) | (1L << Return) | (1L << Short))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (Switch - 65)) | (1L << (Void - 65)) | (1L << (While - 65)) | (1L << (LeftParen - 65)) | (1L << (LeftBrace - 65)) | (1L << (Minus - 65)) | (1L << (And - 65)) | (1L << (Not - 65)) | (1L << (Semi - 65)))) != 0) || _la==Identifier) {
				{
				{
				setState(225);
				statement();
				}
				}
				setState(230);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(231);
			match(RightBrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CaseStatementContext extends ParserRuleContext {
		public TerminalNode Case() { return getToken(cpp2llvmParser.Case, 0); }
		public ConstExpressionContext constExpression() {
			return getRuleContext(ConstExpressionContext.class,0);
		}
		public TerminalNode Colon() { return getToken(cpp2llvmParser.Colon, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public CaseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseStatement; }
	}

	public final CaseStatementContext caseStatement() throws RecognitionException {
		CaseStatementContext _localctx = new CaseStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_caseStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(Case);
			setState(234);
			constExpression();
			setState(235);
			match(Colon);
			setState(236);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectionStatementContext extends ParserRuleContext {
		public TerminalNode If() { return getToken(cpp2llvmParser.If, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode Else() { return getToken(cpp2llvmParser.Else, 0); }
		public TerminalNode Switch() { return getToken(cpp2llvmParser.Switch, 0); }
		public TerminalNode LeftBrace() { return getToken(cpp2llvmParser.LeftBrace, 0); }
		public TerminalNode RightBrace() { return getToken(cpp2llvmParser.RightBrace, 0); }
		public List<CaseStatementContext> caseStatement() {
			return getRuleContexts(CaseStatementContext.class);
		}
		public CaseStatementContext caseStatement(int i) {
			return getRuleContext(CaseStatementContext.class,i);
		}
		public SelectionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectionStatement; }
	}

	public final SelectionStatementContext selectionStatement() throws RecognitionException {
		SelectionStatementContext _localctx = new SelectionStatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_selectionStatement);
		int _la;
		try {
			setState(260);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case If:
				enterOuterAlt(_localctx, 1);
				{
				setState(238);
				match(If);
				setState(239);
				match(LeftParen);
				setState(240);
				condition();
				setState(241);
				match(RightParen);
				setState(242);
				statement();
				setState(245);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(243);
					match(Else);
					setState(244);
					statement();
					}
					break;
				}
				}
				break;
			case Switch:
				enterOuterAlt(_localctx, 2);
				{
				setState(247);
				match(Switch);
				setState(248);
				match(LeftParen);
				setState(249);
				condition();
				setState(250);
				match(RightParen);
				setState(251);
				match(LeftBrace);
				setState(255);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Case) {
					{
					{
					setState(252);
					caseStatement();
					}
					}
					setState(257);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(258);
				match(RightBrace);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IterationStatementContext extends ParserRuleContext {
		public TerminalNode While() { return getToken(cpp2llvmParser.While, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode Do() { return getToken(cpp2llvmParser.Do, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> Semi() { return getTokens(cpp2llvmParser.Semi); }
		public TerminalNode Semi(int i) {
			return getToken(cpp2llvmParser.Semi, i);
		}
		public TerminalNode For() { return getToken(cpp2llvmParser.For, 0); }
		public List<TerminalNode> Comma() { return getTokens(cpp2llvmParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(cpp2llvmParser.Comma, i);
		}
		public IterationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterationStatement; }
	}

	public final IterationStatementContext iterationStatement() throws RecognitionException {
		IterationStatementContext _localctx = new IterationStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_iterationStatement);
		int _la;
		try {
			setState(305);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case While:
				enterOuterAlt(_localctx, 1);
				{
				setState(262);
				match(While);
				setState(263);
				match(LeftParen);
				setState(264);
				condition();
				setState(265);
				match(RightParen);
				setState(266);
				statement();
				}
				break;
			case Do:
				enterOuterAlt(_localctx, 2);
				{
				setState(268);
				match(Do);
				setState(269);
				statement();
				setState(270);
				match(While);
				setState(271);
				match(LeftParen);
				setState(272);
				expression(0);
				setState(273);
				match(RightParen);
				setState(274);
				match(Semi);
				}
				break;
			case For:
				enterOuterAlt(_localctx, 3);
				{
				setState(276);
				match(For);
				setState(277);
				match(LeftParen);
				setState(286);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(278);
					expression(0);
					setState(283);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==Comma) {
						{
						{
						setState(279);
						match(Comma);
						setState(280);
						expression(0);
						}
						}
						setState(285);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(288);
				match(Semi);
				setState(290);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(289);
					expression(0);
					}
				}

				setState(292);
				match(Semi);
				setState(301);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(293);
					expression(0);
					setState(298);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==Comma) {
						{
						{
						setState(294);
						match(Comma);
						setState(295);
						expression(0);
						}
						}
						setState(300);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(303);
				match(RightParen);
				setState(304);
				statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class JumpStatementContext extends ParserRuleContext {
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public TerminalNode Break() { return getToken(cpp2llvmParser.Break, 0); }
		public TerminalNode Continue() { return getToken(cpp2llvmParser.Continue, 0); }
		public TerminalNode Return() { return getToken(cpp2llvmParser.Return, 0); }
		public TerminalNode Goto() { return getToken(cpp2llvmParser.Goto, 0); }
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public JumpStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jumpStatement; }
	}

	public final JumpStatementContext jumpStatement() throws RecognitionException {
		JumpStatementContext _localctx = new JumpStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_jumpStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Break:
				{
				setState(307);
				match(Break);
				}
				break;
			case Continue:
				{
				setState(308);
				match(Continue);
				}
				break;
			case Return:
				{
				setState(309);
				match(Return);
				setState(311);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(310);
					expression(0);
					}
				}

				}
				break;
			case Goto:
				{
				setState(313);
				match(Goto);
				setState(314);
				match(Identifier);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(317);
			match(Semi);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public VariableDeclaratorContext variableDeclarator() {
			return getRuleContext(VariableDeclaratorContext.class,0);
		}
		public ArrayDeclaratorContext arrayDeclarator() {
			return getRuleContext(ArrayDeclaratorContext.class,0);
		}
		public FunctionDeclaratorContext functionDeclarator() {
			return getRuleContext(FunctionDeclaratorContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_declaration);
		try {
			setState(322);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(319);
				variableDeclarator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(320);
				arrayDeclarator();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(321);
				functionDeclarator();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclaratorContext extends ParserRuleContext {
		public TypeModifierContext typeModifier() {
			return getRuleContext(TypeModifierContext.class,0);
		}
		public VariableDeclarationListContext variableDeclarationList() {
			return getRuleContext(VariableDeclarationListContext.class,0);
		}
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public VariableDeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclarator; }
	}

	public final VariableDeclaratorContext variableDeclarator() throws RecognitionException {
		VariableDeclaratorContext _localctx = new VariableDeclaratorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_variableDeclarator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			typeModifier();
			setState(325);
			variableDeclarationList();
			setState(326);
			match(Semi);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclarationListContext extends ParserRuleContext {
		public List<VariableDeclarationContext> variableDeclaration() {
			return getRuleContexts(VariableDeclarationContext.class);
		}
		public VariableDeclarationContext variableDeclaration(int i) {
			return getRuleContext(VariableDeclarationContext.class,i);
		}
		public List<TerminalNode> Comma() { return getTokens(cpp2llvmParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(cpp2llvmParser.Comma, i);
		}
		public VariableDeclarationListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclarationList; }
	}

	public final VariableDeclarationListContext variableDeclarationList() throws RecognitionException {
		VariableDeclarationListContext _localctx = new VariableDeclarationListContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_variableDeclarationList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			variableDeclaration();
			setState(333);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(329);
				match(Comma);
				setState(330);
				variableDeclaration();
				}
				}
				setState(335);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableDeclarationContext extends ParserRuleContext {
		public VarDeclWithoutInitContext varDeclWithoutInit() {
			return getRuleContext(VarDeclWithoutInitContext.class,0);
		}
		public VarDeclWithConstInitContext varDeclWithConstInit() {
			return getRuleContext(VarDeclWithConstInitContext.class,0);
		}
		public VarDeclWithNormalInitContext varDeclWithNormalInit() {
			return getRuleContext(VarDeclWithNormalInitContext.class,0);
		}
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_variableDeclaration);
		try {
			setState(339);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(336);
				varDeclWithoutInit();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(337);
				varDeclWithConstInit();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(338);
				varDeclWithNormalInit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDeclWithoutInitContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public VarDeclWithoutInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclWithoutInit; }
	}

	public final VarDeclWithoutInitContext varDeclWithoutInit() throws RecognitionException {
		VarDeclWithoutInitContext _localctx = new VarDeclWithoutInitContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_varDeclWithoutInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			match(Identifier);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDeclWithConstInitContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode Assign() { return getToken(cpp2llvmParser.Assign, 0); }
		public ConstExpressionContext constExpression() {
			return getRuleContext(ConstExpressionContext.class,0);
		}
		public VarDeclWithConstInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclWithConstInit; }
	}

	public final VarDeclWithConstInitContext varDeclWithConstInit() throws RecognitionException {
		VarDeclWithConstInitContext _localctx = new VarDeclWithConstInitContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_varDeclWithConstInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(343);
			match(Identifier);
			setState(344);
			match(Assign);
			setState(345);
			constExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDeclWithNormalInitContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode Assign() { return getToken(cpp2llvmParser.Assign, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public VarDeclWithNormalInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclWithNormalInit; }
	}

	public final VarDeclWithNormalInitContext varDeclWithNormalInit() throws RecognitionException {
		VarDeclWithNormalInitContext _localctx = new VarDeclWithNormalInitContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_varDeclWithNormalInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(347);
			match(Identifier);
			setState(348);
			match(Assign);
			setState(349);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayDeclaratorContext extends ParserRuleContext {
		public NormalArrayDeclarationContext normalArrayDeclaration() {
			return getRuleContext(NormalArrayDeclarationContext.class,0);
		}
		public StringDeclarationContext stringDeclaration() {
			return getRuleContext(StringDeclarationContext.class,0);
		}
		public ArrayDeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayDeclarator; }
	}

	public final ArrayDeclaratorContext arrayDeclarator() throws RecognitionException {
		ArrayDeclaratorContext _localctx = new ArrayDeclaratorContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_arrayDeclarator);
		try {
			setState(353);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(351);
				normalArrayDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(352);
				stringDeclaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NormalArrayDeclarationContext extends ParserRuleContext {
		public NormalTypeModifierContext normalTypeModifier() {
			return getRuleContext(NormalTypeModifierContext.class,0);
		}
		public ArrayNameContext arrayName() {
			return getRuleContext(ArrayNameContext.class,0);
		}
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public TerminalNode Assign() { return getToken(cpp2llvmParser.Assign, 0); }
		public TerminalNode LeftBrace() { return getToken(cpp2llvmParser.LeftBrace, 0); }
		public ArrayAssginExpressionListContext arrayAssginExpressionList() {
			return getRuleContext(ArrayAssginExpressionListContext.class,0);
		}
		public TerminalNode RightBrace() { return getToken(cpp2llvmParser.RightBrace, 0); }
		public NormalArrayDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_normalArrayDeclaration; }
	}

	public final NormalArrayDeclarationContext normalArrayDeclaration() throws RecognitionException {
		NormalArrayDeclarationContext _localctx = new NormalArrayDeclarationContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_normalArrayDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			normalTypeModifier();
			setState(356);
			arrayName();
			setState(362);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(357);
				match(Assign);
				setState(358);
				match(LeftBrace);
				setState(359);
				arrayAssginExpressionList();
				setState(360);
				match(RightBrace);
				}
			}

			setState(364);
			match(Semi);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayAssginExpressionListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> Comma() { return getTokens(cpp2llvmParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(cpp2llvmParser.Comma, i);
		}
		public ArrayAssginExpressionListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayAssginExpressionList; }
	}

	public final ArrayAssginExpressionListContext arrayAssginExpressionList() throws RecognitionException {
		ArrayAssginExpressionListContext _localctx = new ArrayAssginExpressionListContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_arrayAssginExpressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
			expression(0);
			setState(371);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(367);
				match(Comma);
				setState(368);
				expression(0);
				}
				}
				setState(373);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringDeclarationContext extends ParserRuleContext {
		public CharTypeModifierContext charTypeModifier() {
			return getRuleContext(CharTypeModifierContext.class,0);
		}
		public ArrayNameContext arrayName() {
			return getRuleContext(ArrayNameContext.class,0);
		}
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public TerminalNode Assign() { return getToken(cpp2llvmParser.Assign, 0); }
		public StringLiteralContext stringLiteral() {
			return getRuleContext(StringLiteralContext.class,0);
		}
		public StringDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringDeclaration; }
	}

	public final StringDeclarationContext stringDeclaration() throws RecognitionException {
		StringDeclarationContext _localctx = new StringDeclarationContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_stringDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			charTypeModifier();
			setState(375);
			arrayName();
			setState(378);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(376);
				match(Assign);
				setState(377);
				stringLiteral();
				}
			}

			setState(380);
			match(Semi);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayNameContext extends ParserRuleContext {
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode LeftBracket() { return getToken(cpp2llvmParser.LeftBracket, 0); }
		public TerminalNode IntegerLiteral() { return getToken(cpp2llvmParser.IntegerLiteral, 0); }
		public TerminalNode RightBracket() { return getToken(cpp2llvmParser.RightBracket, 0); }
		public ArrayNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayName; }
	}

	public final ArrayNameContext arrayName() throws RecognitionException {
		ArrayNameContext _localctx = new ArrayNameContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_arrayName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			match(Identifier);
			setState(383);
			match(LeftBracket);
			setState(384);
			match(IntegerLiteral);
			setState(385);
			match(RightBracket);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDeclaratorContext extends ParserRuleContext {
		public FunctionDeclarationContext functionDeclaration() {
			return getRuleContext(FunctionDeclarationContext.class,0);
		}
		public FunctionDefinitionContext functionDefinition() {
			return getRuleContext(FunctionDefinitionContext.class,0);
		}
		public FunctionDeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclarator; }
	}

	public final FunctionDeclaratorContext functionDeclarator() throws RecognitionException {
		FunctionDeclaratorContext _localctx = new FunctionDeclaratorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_functionDeclarator);
		try {
			setState(389);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(387);
				functionDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(388);
				functionDefinition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDeclarationContext extends ParserRuleContext {
		public FunctionHeadContext functionHead() {
			return getRuleContext(FunctionHeadContext.class,0);
		}
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public FunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDeclaration; }
	}

	public final FunctionDeclarationContext functionDeclaration() throws RecognitionException {
		FunctionDeclarationContext _localctx = new FunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_functionDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(391);
			functionHead();
			setState(392);
			match(Semi);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionDefinitionContext extends ParserRuleContext {
		public FunctionHeadContext functionHead() {
			return getRuleContext(FunctionHeadContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public FunctionDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefinition; }
	}

	public final FunctionDefinitionContext functionDefinition() throws RecognitionException {
		FunctionDefinitionContext _localctx = new FunctionDefinitionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_functionDefinition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			functionHead();
			setState(395);
			compoundStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionHeadContext extends ParserRuleContext {
		public TypeModifierContext typeModifier() {
			return getRuleContext(TypeModifierContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public FunctionParameterListContext functionParameterList() {
			return getRuleContext(FunctionParameterListContext.class,0);
		}
		public FunctionHeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionHead; }
	}

	public final FunctionHeadContext functionHead() throws RecognitionException {
		FunctionHeadContext _localctx = new FunctionHeadContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_functionHead);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			typeModifier();
			setState(398);
			match(Identifier);
			setState(399);
			match(LeftParen);
			setState(401);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Bool) | (1L << Char) | (1L << Double) | (1L << Float) | (1L << Int) | (1L << Long) | (1L << Short))) != 0) || _la==Void || _la==Ellipsis) {
				{
				setState(400);
				functionParameterList();
				}
			}

			setState(403);
			match(RightParen);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionParameterListContext extends ParserRuleContext {
		public List<FunctionParameterContext> functionParameter() {
			return getRuleContexts(FunctionParameterContext.class);
		}
		public FunctionParameterContext functionParameter(int i) {
			return getRuleContext(FunctionParameterContext.class,i);
		}
		public List<TerminalNode> Comma() { return getTokens(cpp2llvmParser.Comma); }
		public TerminalNode Comma(int i) {
			return getToken(cpp2llvmParser.Comma, i);
		}
		public FunctionParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionParameterList; }
	}

	public final FunctionParameterListContext functionParameterList() throws RecognitionException {
		FunctionParameterListContext _localctx = new FunctionParameterListContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_functionParameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
			functionParameter();
			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(406);
				match(Comma);
				setState(407);
				functionParameter();
				}
				}
				setState(412);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionParameterContext extends ParserRuleContext {
		public PointerTypeModifierContext pointerTypeModifier() {
			return getRuleContext(PointerTypeModifierContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public NormalTypeModifierContext normalTypeModifier() {
			return getRuleContext(NormalTypeModifierContext.class,0);
		}
		public TerminalNode Ellipsis() { return getToken(cpp2llvmParser.Ellipsis, 0); }
		public FunctionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionParameter; }
	}

	public final FunctionParameterContext functionParameter() throws RecognitionException {
		FunctionParameterContext _localctx = new FunctionParameterContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_functionParameter);
		try {
			setState(420);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(413);
				pointerTypeModifier();
				setState(414);
				match(Identifier);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(416);
				normalTypeModifier();
				setState(417);
				match(Identifier);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(419);
				match(Ellipsis);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeModifierContext extends ParserRuleContext {
		public PointerTypeModifierContext pointerTypeModifier() {
			return getRuleContext(PointerTypeModifierContext.class,0);
		}
		public NormalTypeModifierContext normalTypeModifier() {
			return getRuleContext(NormalTypeModifierContext.class,0);
		}
		public TypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeModifier; }
	}

	public final TypeModifierContext typeModifier() throws RecognitionException {
		TypeModifierContext _localctx = new TypeModifierContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_typeModifier);
		try {
			setState(424);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(422);
				pointerTypeModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(423);
				normalTypeModifier();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PointerTypeModifierContext extends ParserRuleContext {
		public NormalTypeModifierContext normalTypeModifier() {
			return getRuleContext(NormalTypeModifierContext.class,0);
		}
		public TerminalNode Star() { return getToken(cpp2llvmParser.Star, 0); }
		public PointerTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pointerTypeModifier; }
	}

	public final PointerTypeModifierContext pointerTypeModifier() throws RecognitionException {
		PointerTypeModifierContext _localctx = new PointerTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_pointerTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(426);
			normalTypeModifier();
			setState(427);
			match(Star);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NormalTypeModifierContext extends ParserRuleContext {
		public IntegerTypeModifierContext integerTypeModifier() {
			return getRuleContext(IntegerTypeModifierContext.class,0);
		}
		public RealTypeModifierContext realTypeModifier() {
			return getRuleContext(RealTypeModifierContext.class,0);
		}
		public BoolTypeModifierContext boolTypeModifier() {
			return getRuleContext(BoolTypeModifierContext.class,0);
		}
		public CharTypeModifierContext charTypeModifier() {
			return getRuleContext(CharTypeModifierContext.class,0);
		}
		public VoidTypeModifierContext voidTypeModifier() {
			return getRuleContext(VoidTypeModifierContext.class,0);
		}
		public NormalTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_normalTypeModifier; }
	}

	public final NormalTypeModifierContext normalTypeModifier() throws RecognitionException {
		NormalTypeModifierContext _localctx = new NormalTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_normalTypeModifier);
		try {
			setState(434);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(429);
				integerTypeModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(430);
				realTypeModifier();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(431);
				boolTypeModifier();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(432);
				charTypeModifier();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(433);
				voidTypeModifier();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntegerTypeModifierContext extends ParserRuleContext {
		public TerminalNode Int() { return getToken(cpp2llvmParser.Int, 0); }
		public List<TerminalNode> Long() { return getTokens(cpp2llvmParser.Long); }
		public TerminalNode Long(int i) {
			return getToken(cpp2llvmParser.Long, i);
		}
		public TerminalNode Short() { return getToken(cpp2llvmParser.Short, 0); }
		public IntegerTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integerTypeModifier; }
	}

	public final IntegerTypeModifierContext integerTypeModifier() throws RecognitionException {
		IntegerTypeModifierContext _localctx = new IntegerTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_integerTypeModifier);
		try {
			setState(441);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(436);
				match(Int);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(437);
				match(Long);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(438);
				match(Short);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(439);
				match(Long);
				setState(440);
				match(Long);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RealTypeModifierContext extends ParserRuleContext {
		public TerminalNode Float() { return getToken(cpp2llvmParser.Float, 0); }
		public TerminalNode Double() { return getToken(cpp2llvmParser.Double, 0); }
		public TerminalNode Long() { return getToken(cpp2llvmParser.Long, 0); }
		public RealTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_realTypeModifier; }
	}

	public final RealTypeModifierContext realTypeModifier() throws RecognitionException {
		RealTypeModifierContext _localctx = new RealTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_realTypeModifier);
		try {
			setState(447);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Float:
				enterOuterAlt(_localctx, 1);
				{
				setState(443);
				match(Float);
				}
				break;
			case Double:
				enterOuterAlt(_localctx, 2);
				{
				setState(444);
				match(Double);
				}
				break;
			case Long:
				enterOuterAlt(_localctx, 3);
				{
				setState(445);
				match(Long);
				setState(446);
				match(Double);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BoolTypeModifierContext extends ParserRuleContext {
		public TerminalNode Bool() { return getToken(cpp2llvmParser.Bool, 0); }
		public BoolTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolTypeModifier; }
	}

	public final BoolTypeModifierContext boolTypeModifier() throws RecognitionException {
		BoolTypeModifierContext _localctx = new BoolTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_boolTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(449);
			match(Bool);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CharTypeModifierContext extends ParserRuleContext {
		public TerminalNode Char() { return getToken(cpp2llvmParser.Char, 0); }
		public CharTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_charTypeModifier; }
	}

	public final CharTypeModifierContext charTypeModifier() throws RecognitionException {
		CharTypeModifierContext _localctx = new CharTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_charTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(451);
			match(Char);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VoidTypeModifierContext extends ParserRuleContext {
		public TerminalNode Void() { return getToken(cpp2llvmParser.Void, 0); }
		public VoidTypeModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_voidTypeModifier; }
	}

	public final VoidTypeModifierContext voidTypeModifier() throws RecognitionException {
		VoidTypeModifierContext _localctx = new VoidTypeModifierContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_voidTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(453);
			match(Void);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 5:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 22);
		case 1:
			return precpred(_ctx, 21);
		case 2:
			return precpred(_ctx, 20);
		case 3:
			return precpred(_ctx, 19);
		case 4:
			return precpred(_ctx, 18);
		case 5:
			return precpred(_ctx, 17);
		case 6:
			return precpred(_ctx, 16);
		case 7:
			return precpred(_ctx, 15);
		case 8:
			return precpred(_ctx, 14);
		case 9:
			return precpred(_ctx, 13);
		case 10:
			return precpred(_ctx, 12);
		case 11:
			return precpred(_ctx, 11);
		case 12:
			return precpred(_ctx, 10);
		case 13:
			return precpred(_ctx, 9);
		case 14:
			return precpred(_ctx, 8);
		case 15:
			return precpred(_ctx, 7);
		case 16:
			return precpred(_ctx, 6);
		case 17:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u008f\u01ca\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2"+
		"\3\3\7\3X\n\3\f\3\16\3[\13\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\5\6i\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0088"+
		"\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\7\7\u00c0\n\7\f\7\16\7\u00c3\13\7\3\b\3\b\3\b\3\b\3\b\7\b\u00ca"+
		"\n\b\f\b\16\b\u00cd\13\b\5\b\u00cf\n\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\5\n\u00dc\n\n\3\13\5\13\u00df\n\13\3\13\3\13\3\f\3\f\7\f"+
		"\u00e5\n\f\f\f\16\f\u00e8\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\5\16\u00f8\n\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\7\16\u0100\n\16\f\16\16\16\u0103\13\16\3\16\3\16\5\16\u0107\n\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\7\17\u011c\n\17\f\17\16\17\u011f\13\17\5\17\u0121"+
		"\n\17\3\17\3\17\5\17\u0125\n\17\3\17\3\17\3\17\3\17\7\17\u012b\n\17\f"+
		"\17\16\17\u012e\13\17\5\17\u0130\n\17\3\17\3\17\5\17\u0134\n\17\3\20\3"+
		"\20\3\20\3\20\5\20\u013a\n\20\3\20\3\20\5\20\u013e\n\20\3\20\3\20\3\21"+
		"\3\21\3\21\5\21\u0145\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u014e"+
		"\n\23\f\23\16\23\u0151\13\23\3\24\3\24\3\24\5\24\u0156\n\24\3\25\3\25"+
		"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\5\30\u0164\n\30\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u016d\n\31\3\31\3\31\3\32\3\32\3\32"+
		"\7\32\u0174\n\32\f\32\16\32\u0177\13\32\3\33\3\33\3\33\3\33\5\33\u017d"+
		"\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u0188\n\35\3\36"+
		"\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0194\n \3 \3 \3!\3!\3!\7!\u019b"+
		"\n!\f!\16!\u019e\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01a7\n\"\3#\3#\5"+
		"#\u01ab\n#\3$\3$\3$\3%\3%\3%\3%\3%\5%\u01b5\n%\3&\3&\3&\3&\3&\5&\u01bc"+
		"\n&\3\'\3\'\3\'\3\'\5\'\u01c2\n\'\3(\3(\3)\3)\3*\3*\3*\2\3\f+\2\4\6\b"+
		"\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\3"+
		"\3\2\3\b\2\u01ee\2T\3\2\2\2\4Y\3\2\2\2\6^\3\2\2\2\b`\3\2\2\2\nh\3\2\2"+
		"\2\f\u0087\3\2\2\2\16\u00c4\3\2\2\2\20\u00d2\3\2\2\2\22\u00db\3\2\2\2"+
		"\24\u00de\3\2\2\2\26\u00e2\3\2\2\2\30\u00eb\3\2\2\2\32\u0106\3\2\2\2\34"+
		"\u0133\3\2\2\2\36\u013d\3\2\2\2 \u0144\3\2\2\2\"\u0146\3\2\2\2$\u014a"+
		"\3\2\2\2&\u0155\3\2\2\2(\u0157\3\2\2\2*\u0159\3\2\2\2,\u015d\3\2\2\2."+
		"\u0163\3\2\2\2\60\u0165\3\2\2\2\62\u0170\3\2\2\2\64\u0178\3\2\2\2\66\u0180"+
		"\3\2\2\28\u0187\3\2\2\2:\u0189\3\2\2\2<\u018c\3\2\2\2>\u018f\3\2\2\2@"+
		"\u0197\3\2\2\2B\u01a6\3\2\2\2D\u01aa\3\2\2\2F\u01ac\3\2\2\2H\u01b4\3\2"+
		"\2\2J\u01bb\3\2\2\2L\u01c1\3\2\2\2N\u01c3\3\2\2\2P\u01c5\3\2\2\2R\u01c7"+
		"\3\2\2\2TU\t\2\2\2U\3\3\2\2\2VX\5 \21\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2"+
		"YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\2\2\3]\5\3\2\2\2^_\7\6\2\2_\7\3\2"+
		"\2\2`a\5\2\2\2a\t\3\2\2\2bi\7\u0086\2\2cd\7\u0086\2\2de\7W\2\2ef\5\f\7"+
		"\2fg\7X\2\2gi\3\2\2\2hb\3\2\2\2hc\3\2\2\2i\13\3\2\2\2jk\b\7\1\2k\u0088"+
		"\5\16\b\2l\u0088\5\2\2\2m\u0088\7\u0086\2\2no\7U\2\2op\5\f\7\2pq\7V\2"+
		"\2q\u0088\3\2\2\2rs\7d\2\2s\u0088\5\f\7\33tu\7\\\2\2u\u0088\5\f\7\32v"+
		"w\7a\2\2w\u0088\5\n\6\2xy\7\u0086\2\2yz\7W\2\2z{\5\f\7\2{|\7X\2\2|\u0088"+
		"\3\2\2\2}~\5\n\6\2~\177\7e\2\2\177\u0080\5\f\7\5\u0080\u0088\3\2\2\2\u0081"+
		"\u0082\5\n\6\2\u0082\u0083\7z\2\2\u0083\u0088\3\2\2\2\u0084\u0085\5\n"+
		"\6\2\u0085\u0086\7{\2\2\u0086\u0088\3\2\2\2\u0087j\3\2\2\2\u0087l\3\2"+
		"\2\2\u0087m\3\2\2\2\u0087n\3\2\2\2\u0087r\3\2\2\2\u0087t\3\2\2\2\u0087"+
		"v\3\2\2\2\u0087x\3\2\2\2\u0087}\3\2\2\2\u0087\u0081\3\2\2\2\u0087\u0084"+
		"\3\2\2\2\u0088\u00c1\3\2\2\2\u0089\u008a\f\30\2\2\u008a\u008b\7]\2\2\u008b"+
		"\u00c0\5\f\7\31\u008c\u008d\f\27\2\2\u008d\u008e\7^\2\2\u008e\u00c0\5"+
		"\f\7\30\u008f\u0090\f\26\2\2\u0090\u0091\7_\2\2\u0091\u00c0\5\f\7\27\u0092"+
		"\u0093\f\25\2\2\u0093\u0094\7[\2\2\u0094\u00c0\5\f\7\26\u0095\u0096\f"+
		"\24\2\2\u0096\u0097\7\\\2\2\u0097\u00c0\5\f\7\25\u0098\u0099\f\23\2\2"+
		"\u0099\u009a\7f\2\2\u009a\u00c0\5\f\7\24\u009b\u009c\f\22\2\2\u009c\u009d"+
		"\7g\2\2\u009d\u00c0\5\f\7\23\u009e\u009f\f\21\2\2\u009f\u00a0\7v\2\2\u00a0"+
		"\u00c0\5\f\7\22\u00a1\u00a2\f\20\2\2\u00a2\u00a3\7w\2\2\u00a3\u00c0\5"+
		"\f\7\21\u00a4\u00a5\f\17\2\2\u00a5\u00a6\7t\2\2\u00a6\u00c0\5\f\7\20\u00a7"+
		"\u00a8\f\16\2\2\u00a8\u00a9\7u\2\2\u00a9\u00c0\5\f\7\17\u00aa\u00ab\f"+
		"\r\2\2\u00ab\u00ac\7b\2\2\u00ac\u00c0\5\f\7\16\u00ad\u00ae\f\f\2\2\u00ae"+
		"\u00af\7a\2\2\u00af\u00c0\5\f\7\r\u00b0\u00b1\f\13\2\2\u00b1\u00b2\7`"+
		"\2\2\u00b2\u00c0\5\f\7\f\u00b3\u00b4\f\n\2\2\u00b4\u00b5\7y\2\2\u00b5"+
		"\u00c0\5\f\7\13\u00b6\u00b7\f\t\2\2\u00b7\u00b8\7x\2\2\u00b8\u00c0\5\f"+
		"\7\n\u00b9\u00ba\f\b\2\2\u00ba\u00bb\7p\2\2\u00bb\u00c0\5\f\7\t\u00bc"+
		"\u00bd\f\7\2\2\u00bd\u00be\7r\2\2\u00be\u00c0\5\f\7\b\u00bf\u0089\3\2"+
		"\2\2\u00bf\u008c\3\2\2\2\u00bf\u008f\3\2\2\2\u00bf\u0092\3\2\2\2\u00bf"+
		"\u0095\3\2\2\2\u00bf\u0098\3\2\2\2\u00bf\u009b\3\2\2\2\u00bf\u009e\3\2"+
		"\2\2\u00bf\u00a1\3\2\2\2\u00bf\u00a4\3\2\2\2\u00bf\u00a7\3\2\2\2\u00bf"+
		"\u00aa\3\2\2\2\u00bf\u00ad\3\2\2\2\u00bf\u00b0\3\2\2\2\u00bf\u00b3\3\2"+
		"\2\2\u00bf\u00b6\3\2\2\2\u00bf\u00b9\3\2\2\2\u00bf\u00bc\3\2\2\2\u00c0"+
		"\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\r\3\2\2\2"+
		"\u00c3\u00c1\3\2\2\2\u00c4\u00c5\7\u0086\2\2\u00c5\u00ce\7U\2\2\u00c6"+
		"\u00cb\5\f\7\2\u00c7\u00c8\7|\2\2\u00c8\u00ca\5\f\7\2\u00c9\u00c7\3\2"+
		"\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc"+
		"\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00c6\3\2\2\2\u00ce\u00cf\3\2"+
		"\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\7V\2\2\u00d1\17\3\2\2\2\u00d2\u00d3"+
		"\5\f\7\2\u00d3\21\3\2\2\2\u00d4\u00dc\5\24\13\2\u00d5\u00dc\5\26\f\2\u00d6"+
		"\u00dc\5\32\16\2\u00d7\u00dc\5\34\17\2\u00d8\u00dc\5\36\20\2\u00d9\u00dc"+
		"\5\"\22\2\u00da\u00dc\5.\30\2\u00db\u00d4\3\2\2\2\u00db\u00d5\3\2\2\2"+
		"\u00db\u00d6\3\2\2\2\u00db\u00d7\3\2\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9"+
		"\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\23\3\2\2\2\u00dd\u00df\5\f\7\2\u00de"+
		"\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\7\u0082"+
		"\2\2\u00e1\25\3\2\2\2\u00e2\u00e6\7Y\2\2\u00e3\u00e5\5\22\n\2\u00e4\u00e3"+
		"\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7"+
		"\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7Z\2\2\u00ea\27\3\2\2\2"+
		"\u00eb\u00ec\7\20\2\2\u00ec\u00ed\5\b\5\2\u00ed\u00ee\7\u0080\2\2\u00ee"+
		"\u00ef\5\22\n\2\u00ef\31\3\2\2\2\u00f0\u00f1\7+\2\2\u00f1\u00f2\7U\2\2"+
		"\u00f2\u00f3\5\20\t\2\u00f3\u00f4\7V\2\2\u00f4\u00f7\5\22\n\2\u00f5\u00f6"+
		"\7 \2\2\u00f6\u00f8\5\22\n\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8"+
		"\u0107\3\2\2\2\u00f9\u00fa\7C\2\2\u00fa\u00fb\7U\2\2\u00fb\u00fc\5\20"+
		"\t\2\u00fc\u00fd\7V\2\2\u00fd\u0101\7Y\2\2\u00fe\u0100\5\30\r\2\u00ff"+
		"\u00fe\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2"+
		"\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\7Z\2\2\u0105"+
		"\u0107\3\2\2\2\u0106\u00f0\3\2\2\2\u0106\u00f9\3\2\2\2\u0107\33\3\2\2"+
		"\2\u0108\u0109\7T\2\2\u0109\u010a\7U\2\2\u010a\u010b\5\20\t\2\u010b\u010c"+
		"\7V\2\2\u010c\u010d\5\22\n\2\u010d\u0134\3\2\2\2\u010e\u010f\7\35\2\2"+
		"\u010f\u0110\5\22\n\2\u0110\u0111\7T\2\2\u0111\u0112\7U\2\2\u0112\u0113"+
		"\5\f\7\2\u0113\u0114\7V\2\2\u0114\u0115\7\u0082\2\2\u0115\u0134\3\2\2"+
		"\2\u0116\u0117\7(\2\2\u0117\u0120\7U\2\2\u0118\u011d\5\f\7\2\u0119\u011a"+
		"\7|\2\2\u011a\u011c\5\f\7\2\u011b\u0119\3\2\2\2\u011c\u011f\3\2\2\2\u011d"+
		"\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2"+
		"\2\2\u0120\u0118\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3\2\2\2\u0122"+
		"\u0124\7\u0082\2\2\u0123\u0125\5\f\7\2\u0124\u0123\3\2\2\2\u0124\u0125"+
		"\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u012f\7\u0082\2\2\u0127\u012c\5\f\7"+
		"\2\u0128\u0129\7|\2\2\u0129\u012b\5\f\7\2\u012a\u0128\3\2\2\2\u012b\u012e"+
		"\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u0130\3\2\2\2\u012e"+
		"\u012c\3\2\2\2\u012f\u0127\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2"+
		"\2\2\u0131\u0132\7V\2\2\u0132\u0134\5\22\n\2\u0133\u0108\3\2\2\2\u0133"+
		"\u010e\3\2\2\2\u0133\u0116\3\2\2\2\u0134\35\3\2\2\2\u0135\u013e\7\17\2"+
		"\2\u0136\u013e\7\31\2\2\u0137\u0139\7;\2\2\u0138\u013a\5\f\7\2\u0139\u0138"+
		"\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013e\3\2\2\2\u013b\u013c\7*\2\2\u013c"+
		"\u013e\7\u0086\2\2\u013d\u0135\3\2\2\2\u013d\u0136\3\2\2\2\u013d\u0137"+
		"\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\7\u0082\2"+
		"\2\u0140\37\3\2\2\2\u0141\u0145\5\"\22\2\u0142\u0145\5.\30\2\u0143\u0145"+
		"\58\35\2\u0144\u0141\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145"+
		"!\3\2\2\2\u0146\u0147\5D#\2\u0147\u0148\5$\23\2\u0148\u0149\7\u0082\2"+
		"\2\u0149#\3\2\2\2\u014a\u014f\5&\24\2\u014b\u014c\7|\2\2\u014c\u014e\5"+
		"&\24\2\u014d\u014b\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f"+
		"\u0150\3\2\2\2\u0150%\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0156\5(\25\2"+
		"\u0153\u0156\5*\26\2\u0154\u0156\5,\27\2\u0155\u0152\3\2\2\2\u0155\u0153"+
		"\3\2\2\2\u0155\u0154\3\2\2\2\u0156\'\3\2\2\2\u0157\u0158\7\u0086\2\2\u0158"+
		")\3\2\2\2\u0159\u015a\7\u0086\2\2\u015a\u015b\7e\2\2\u015b\u015c\5\b\5"+
		"\2\u015c+\3\2\2\2\u015d\u015e\7\u0086\2\2\u015e\u015f\7e\2\2\u015f\u0160"+
		"\5\f\7\2\u0160-\3\2\2\2\u0161\u0164\5\60\31\2\u0162\u0164\5\64\33\2\u0163"+
		"\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164/\3\2\2\2\u0165\u0166\5H%\2\u0166"+
		"\u016c\5\66\34\2\u0167\u0168\7e\2\2\u0168\u0169\7Y\2\2\u0169\u016a\5\62"+
		"\32\2\u016a\u016b\7Z\2\2\u016b\u016d\3\2\2\2\u016c\u0167\3\2\2\2\u016c"+
		"\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\7\u0082\2\2\u016f\61\3"+
		"\2\2\2\u0170\u0175\5\f\7\2\u0171\u0172\7|\2\2\u0172\u0174\5\f\7\2\u0173"+
		"\u0171\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2"+
		"\2\2\u0176\63\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\5P)\2\u0179\u017c"+
		"\5\66\34\2\u017a\u017b\7e\2\2\u017b\u017d\5\6\4\2\u017c\u017a\3\2\2\2"+
		"\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\7\u0082\2\2\u017f"+
		"\65\3\2\2\2\u0180\u0181\7\u0086\2\2\u0181\u0182\7W\2\2\u0182\u0183\7\3"+
		"\2\2\u0183\u0184\7X\2\2\u0184\67\3\2\2\2\u0185\u0188\5:\36\2\u0186\u0188"+
		"\5<\37\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u01889\3\2\2\2\u0189"+
		"\u018a\5> \2\u018a\u018b\7\u0082\2\2\u018b;\3\2\2\2\u018c\u018d\5> \2"+
		"\u018d\u018e\5\26\f\2\u018e=\3\2\2\2\u018f\u0190\5D#\2\u0190\u0191\7\u0086"+
		"\2\2\u0191\u0193\7U\2\2\u0192\u0194\5@!\2\u0193\u0192\3\2\2\2\u0193\u0194"+
		"\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\7V\2\2\u0196?\3\2\2\2\u0197\u019c"+
		"\5B\"\2\u0198\u0199\7|\2\2\u0199\u019b\5B\"\2\u019a\u0198\3\2\2\2\u019b"+
		"\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019dA\3\2\2\2"+
		"\u019e\u019c\3\2\2\2\u019f\u01a0\5F$\2\u01a0\u01a1\7\u0086\2\2\u01a1\u01a7"+
		"\3\2\2\2\u01a2\u01a3\5H%\2\u01a3\u01a4\7\u0086\2\2\u01a4\u01a7\3\2\2\2"+
		"\u01a5\u01a7\7\u0085\2\2\u01a6\u019f\3\2\2\2\u01a6\u01a2\3\2\2\2\u01a6"+
		"\u01a5\3\2\2\2\u01a7C\3\2\2\2\u01a8\u01ab\5F$\2\u01a9\u01ab\5H%\2\u01aa"+
		"\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abE\3\2\2\2\u01ac\u01ad\5H%\2\u01ad"+
		"\u01ae\7]\2\2\u01aeG\3\2\2\2\u01af\u01b5\5J&\2\u01b0\u01b5\5L\'\2\u01b1"+
		"\u01b5\5N(\2\u01b2\u01b5\5P)\2\u01b3\u01b5\5R*\2\u01b4\u01af\3\2\2\2\u01b4"+
		"\u01b0\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2"+
		"\2\2\u01b5I\3\2\2\2\u01b6\u01bc\7-\2\2\u01b7\u01bc\7.\2\2\u01b8\u01bc"+
		"\7<\2\2\u01b9\u01ba\7.\2\2\u01ba\u01bc\7.\2\2\u01bb\u01b6\3\2\2\2\u01bb"+
		"\u01b7\3\2\2\2\u01bb\u01b8\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bcK\3\2\2\2"+
		"\u01bd\u01c2\7\'\2\2\u01be\u01c2\7\36\2\2\u01bf\u01c0\7.\2\2\u01c0\u01c2"+
		"\7\36\2\2\u01c1\u01bd\3\2\2\2\u01c1\u01be\3\2\2\2\u01c1\u01bf\3\2\2\2"+
		"\u01c2M\3\2\2\2\u01c3\u01c4\7\16\2\2\u01c4O\3\2\2\2\u01c5\u01c6\7\22\2"+
		"\2\u01c6Q\3\2\2\2\u01c7\u01c8\7Q\2\2\u01c8S\3\2\2\2&Yh\u0087\u00bf\u00c1"+
		"\u00cb\u00ce\u00db\u00de\u00e6\u00f7\u0101\u0106\u011d\u0120\u0124\u012c"+
		"\u012f\u0133\u0139\u013d\u0144\u014f\u0155\u0163\u016c\u0175\u017c\u0187"+
		"\u0193\u019c\u01a6\u01aa\u01b4\u01bb\u01c1";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}