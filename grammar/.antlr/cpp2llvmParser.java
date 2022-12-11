// Generated from /mnt/d/programming/2022autumn/assembly_complie/CPPToLLVM/code/grammar/cpp2llvmParser.g4 by ANTLR 4.9.2
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
		RULE_translationUnit = 0, RULE_stringLiteral = 1, RULE_constExpression = 2, 
		RULE_leftExpression = 3, RULE_expression = 4, RULE_functionCall = 5, RULE_condition = 6, 
		RULE_statement = 7, RULE_expressionStatement = 8, RULE_compoundStatement = 9, 
		RULE_caseStatement = 10, RULE_selectionStatement = 11, RULE_iterationStatement = 12, 
		RULE_jumpStatement = 13, RULE_declaration = 14, RULE_variableDeclarator = 15, 
		RULE_variableDeclarationList = 16, RULE_variableDeclaration = 17, RULE_varDeclWithoutInit = 18, 
		RULE_varDeclWithConstInit = 19, RULE_varDeclWithNormalInit = 20, RULE_arrayDeclarator = 21, 
		RULE_normalArrayDeclaration = 22, RULE_arrayAssginExpressionList = 23, 
		RULE_stringDeclaration = 24, RULE_arrayName = 25, RULE_functionDeclarator = 26, 
		RULE_functionDeclaration = 27, RULE_functionDefinition = 28, RULE_functionHead = 29, 
		RULE_functionParameterList = 30, RULE_functionParameter = 31, RULE_typeModifier = 32, 
		RULE_pointerTypeModifier = 33, RULE_normalTypeModifier = 34, RULE_integerTypeModifier = 35, 
		RULE_realTypeModifier = 36, RULE_boolTypeModifier = 37, RULE_charTypeModifier = 38, 
		RULE_voidTypeModifier = 39, RULE_literal = 40;
	private static String[] makeRuleNames() {
		return new String[] {
			"translationUnit", "stringLiteral", "constExpression", "leftExpression", 
			"expression", "functionCall", "condition", "statement", "expressionStatement", 
			"compoundStatement", "caseStatement", "selectionStatement", "iterationStatement", 
			"jumpStatement", "declaration", "variableDeclarator", "variableDeclarationList", 
			"variableDeclaration", "varDeclWithoutInit", "varDeclWithConstInit", 
			"varDeclWithNormalInit", "arrayDeclarator", "normalArrayDeclaration", 
			"arrayAssginExpressionList", "stringDeclaration", "arrayName", "functionDeclarator", 
			"functionDeclaration", "functionDefinition", "functionHead", "functionParameterList", 
			"functionParameter", "typeModifier", "pointerTypeModifier", "normalTypeModifier", 
			"integerTypeModifier", "realTypeModifier", "boolTypeModifier", "charTypeModifier", 
			"voidTypeModifier", "literal"
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
		enterRule(_localctx, 0, RULE_translationUnit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Bool) | (1L << Char) | (1L << Double) | (1L << Float) | (1L << Int) | (1L << Long) | (1L << Short))) != 0) || _la==Void) {
				{
				{
				setState(82);
				declaration();
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(88);
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
		enterRule(_localctx, 2, RULE_stringLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
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
		enterRule(_localctx, 4, RULE_constExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
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
		enterRule(_localctx, 6, RULE_leftExpression);
		try {
			setState(100);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(Identifier);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				match(Identifier);
				{
				setState(96);
				match(LeftBracket);
				setState(97);
				expression(0);
				setState(98);
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
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(103);
				functionCall();
				}
				break;
			case 2:
				{
				setState(104);
				literal();
				}
				break;
			case 3:
				{
				setState(105);
				match(Identifier);
				}
				break;
			case 4:
				{
				setState(106);
				match(LeftParen);
				setState(107);
				expression(0);
				setState(108);
				match(RightParen);
				}
				break;
			case 5:
				{
				setState(110);
				match(Not);
				setState(111);
				expression(25);
				}
				break;
			case 6:
				{
				setState(112);
				match(Minus);
				setState(113);
				expression(24);
				}
				break;
			case 7:
				{
				setState(114);
				match(And);
				setState(115);
				leftExpression();
				}
				break;
			case 8:
				{
				setState(116);
				match(Identifier);
				setState(117);
				match(LeftBracket);
				setState(118);
				expression(0);
				setState(119);
				match(RightBracket);
				}
				break;
			case 9:
				{
				setState(121);
				leftExpression();
				setState(122);
				match(Assign);
				setState(123);
				expression(3);
				}
				break;
			case 10:
				{
				setState(125);
				leftExpression();
				setState(126);
				match(PlusPlus);
				}
				break;
			case 11:
				{
				setState(128);
				leftExpression();
				setState(129);
				match(MinusMinus);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(189);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(187);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(133);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(134);
						match(Star);
						setState(135);
						expression(23);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(136);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(137);
						match(Div);
						setState(138);
						expression(22);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(139);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(140);
						match(Mod);
						setState(141);
						expression(21);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(142);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(143);
						match(Plus);
						setState(144);
						expression(20);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(145);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(146);
						match(Minus);
						setState(147);
						expression(19);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(148);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(149);
						match(Less);
						setState(150);
						expression(18);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(151);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(152);
						match(Greater);
						setState(153);
						expression(17);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(154);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(155);
						match(LessEqual);
						setState(156);
						expression(16);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(157);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(158);
						match(GreaterEqual);
						setState(159);
						expression(15);
						}
						break;
					case 10:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(160);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(161);
						match(Equal);
						setState(162);
						expression(14);
						}
						break;
					case 11:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(163);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(164);
						match(NotEqual);
						setState(165);
						expression(13);
						}
						break;
					case 12:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(166);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(167);
						match(Or);
						setState(168);
						expression(12);
						}
						break;
					case 13:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(169);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(170);
						match(And);
						setState(171);
						expression(11);
						}
						break;
					case 14:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(172);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(173);
						match(Caret);
						setState(174);
						expression(10);
						}
						break;
					case 15:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(175);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(176);
						match(OrOr);
						setState(177);
						expression(9);
						}
						break;
					case 16:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(178);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(179);
						match(AndAnd);
						setState(180);
						expression(8);
						}
						break;
					case 17:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(181);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(182);
						match(LeftShift);
						setState(183);
						expression(7);
						}
						break;
					case 18:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(184);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(185);
						match(RightShift);
						setState(186);
						expression(6);
						}
						break;
					}
					} 
				}
				setState(191);
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
		enterRule(_localctx, 10, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(Identifier);
			setState(193);
			match(LeftParen);
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(194);
				expression(0);
				setState(199);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Comma) {
					{
					{
					setState(195);
					match(Comma);
					setState(196);
					expression(0);
					}
					}
					setState(201);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(204);
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
		enterRule(_localctx, 12, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
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
		enterRule(_localctx, 14, RULE_statement);
		try {
			setState(215);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(208);
				expressionStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(209);
				compoundStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(210);
				selectionStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(211);
				iterationStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(212);
				jumpStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(213);
				variableDeclarator();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(214);
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
		enterRule(_localctx, 16, RULE_expressionStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(217);
				expression(0);
				}
			}

			setState(220);
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
		enterRule(_localctx, 18, RULE_compoundStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(LeftBrace);
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral) | (1L << Bool) | (1L << Break) | (1L << Char) | (1L << Continue) | (1L << Do) | (1L << Double) | (1L << Float) | (1L << For) | (1L << Goto) | (1L << If) | (1L << Int) | (1L << Long) | (1L << Return) | (1L << Short))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (Switch - 65)) | (1L << (Void - 65)) | (1L << (While - 65)) | (1L << (LeftParen - 65)) | (1L << (LeftBrace - 65)) | (1L << (Minus - 65)) | (1L << (And - 65)) | (1L << (Not - 65)) | (1L << (Semi - 65)))) != 0) || _la==Identifier) {
				{
				{
				setState(223);
				statement();
				}
				}
				setState(228);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(229);
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
		enterRule(_localctx, 20, RULE_caseStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(Case);
			setState(232);
			constExpression();
			setState(233);
			match(Colon);
			setState(234);
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
		enterRule(_localctx, 22, RULE_selectionStatement);
		int _la;
		try {
			setState(258);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case If:
				enterOuterAlt(_localctx, 1);
				{
				setState(236);
				match(If);
				setState(237);
				match(LeftParen);
				setState(238);
				condition();
				setState(239);
				match(RightParen);
				setState(240);
				statement();
				setState(243);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(241);
					match(Else);
					setState(242);
					statement();
					}
					break;
				}
				}
				break;
			case Switch:
				enterOuterAlt(_localctx, 2);
				{
				setState(245);
				match(Switch);
				setState(246);
				match(LeftParen);
				setState(247);
				condition();
				setState(248);
				match(RightParen);
				setState(249);
				match(LeftBrace);
				setState(253);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Case) {
					{
					{
					setState(250);
					caseStatement();
					}
					}
					setState(255);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(256);
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
		enterRule(_localctx, 24, RULE_iterationStatement);
		int _la;
		try {
			setState(303);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case While:
				enterOuterAlt(_localctx, 1);
				{
				setState(260);
				match(While);
				setState(261);
				match(LeftParen);
				setState(262);
				condition();
				setState(263);
				match(RightParen);
				setState(264);
				statement();
				}
				break;
			case Do:
				enterOuterAlt(_localctx, 2);
				{
				setState(266);
				match(Do);
				setState(267);
				statement();
				setState(268);
				match(While);
				setState(269);
				match(LeftParen);
				setState(270);
				expression(0);
				setState(271);
				match(RightParen);
				setState(272);
				match(Semi);
				}
				break;
			case For:
				enterOuterAlt(_localctx, 3);
				{
				setState(274);
				match(For);
				setState(275);
				match(LeftParen);
				setState(284);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(276);
					expression(0);
					setState(281);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==Comma) {
						{
						{
						setState(277);
						match(Comma);
						setState(278);
						expression(0);
						}
						}
						setState(283);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(286);
				match(Semi);
				setState(288);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(287);
					expression(0);
					}
				}

				setState(290);
				match(Semi);
				setState(299);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(291);
					expression(0);
					setState(296);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==Comma) {
						{
						{
						setState(292);
						match(Comma);
						setState(293);
						expression(0);
						}
						}
						setState(298);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(301);
				match(RightParen);
				setState(302);
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
		enterRule(_localctx, 26, RULE_jumpStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(313);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Break:
				{
				setState(305);
				match(Break);
				}
				break;
			case Continue:
				{
				setState(306);
				match(Continue);
				}
				break;
			case Return:
				{
				setState(307);
				match(Return);
				setState(309);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << BooleanLiteral) | (1L << PointerLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
					{
					setState(308);
					expression(0);
					}
				}

				}
				break;
			case Goto:
				{
				setState(311);
				match(Goto);
				setState(312);
				match(Identifier);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(315);
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
		enterRule(_localctx, 28, RULE_declaration);
		try {
			setState(320);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(317);
				variableDeclarator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(318);
				arrayDeclarator();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(319);
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
		enterRule(_localctx, 30, RULE_variableDeclarator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			typeModifier();
			setState(323);
			variableDeclarationList();
			setState(324);
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
		enterRule(_localctx, 32, RULE_variableDeclarationList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			variableDeclaration();
			setState(331);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(327);
				match(Comma);
				setState(328);
				variableDeclaration();
				}
				}
				setState(333);
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
		enterRule(_localctx, 34, RULE_variableDeclaration);
		try {
			setState(337);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(334);
				varDeclWithoutInit();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(335);
				varDeclWithConstInit();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(336);
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
		enterRule(_localctx, 36, RULE_varDeclWithoutInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(339);
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
		enterRule(_localctx, 38, RULE_varDeclWithConstInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			match(Identifier);
			setState(342);
			match(Assign);
			setState(343);
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
		enterRule(_localctx, 40, RULE_varDeclWithNormalInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(345);
			match(Identifier);
			setState(346);
			match(Assign);
			setState(347);
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
		enterRule(_localctx, 42, RULE_arrayDeclarator);
		try {
			setState(351);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(349);
				normalArrayDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(350);
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
		enterRule(_localctx, 44, RULE_normalArrayDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			normalTypeModifier();
			setState(354);
			arrayName();
			setState(360);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(355);
				match(Assign);
				setState(356);
				match(LeftBrace);
				setState(357);
				arrayAssginExpressionList();
				setState(358);
				match(RightBrace);
				}
			}

			setState(362);
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
		enterRule(_localctx, 46, RULE_arrayAssginExpressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			expression(0);
			setState(369);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(365);
				match(Comma);
				setState(366);
				expression(0);
				}
				}
				setState(371);
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
		enterRule(_localctx, 48, RULE_stringDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(372);
			charTypeModifier();
			setState(373);
			arrayName();
			setState(376);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(374);
				match(Assign);
				setState(375);
				stringLiteral();
				}
			}

			setState(378);
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
		public TerminalNode DecimalLiteral() { return getToken(cpp2llvmParser.DecimalLiteral, 0); }
		public TerminalNode RightBracket() { return getToken(cpp2llvmParser.RightBracket, 0); }
		public ArrayNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayName; }
	}

	public final ArrayNameContext arrayName() throws RecognitionException {
		ArrayNameContext _localctx = new ArrayNameContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_arrayName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			match(Identifier);
			setState(381);
			match(LeftBracket);
			setState(382);
			match(DecimalLiteral);
			setState(383);
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
		enterRule(_localctx, 52, RULE_functionDeclarator);
		try {
			setState(387);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(385);
				functionDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(386);
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
		enterRule(_localctx, 54, RULE_functionDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			functionHead();
			setState(390);
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
		enterRule(_localctx, 56, RULE_functionDefinition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(392);
			functionHead();
			setState(393);
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
		enterRule(_localctx, 58, RULE_functionHead);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(395);
			typeModifier();
			setState(396);
			match(Identifier);
			setState(397);
			match(LeftParen);
			setState(399);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Bool) | (1L << Char) | (1L << Double) | (1L << Float) | (1L << Int) | (1L << Long) | (1L << Short))) != 0) || _la==Void || _la==Ellipsis) {
				{
				setState(398);
				functionParameterList();
				}
			}

			setState(401);
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
		enterRule(_localctx, 60, RULE_functionParameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(403);
			functionParameter();
			setState(408);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(404);
				match(Comma);
				setState(405);
				functionParameter();
				}
				}
				setState(410);
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
		enterRule(_localctx, 62, RULE_functionParameter);
		try {
			setState(418);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(411);
				pointerTypeModifier();
				setState(412);
				match(Identifier);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(414);
				normalTypeModifier();
				setState(415);
				match(Identifier);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(417);
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
		enterRule(_localctx, 64, RULE_typeModifier);
		try {
			setState(422);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(420);
				pointerTypeModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(421);
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
		enterRule(_localctx, 66, RULE_pointerTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			normalTypeModifier();
			setState(425);
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
		enterRule(_localctx, 68, RULE_normalTypeModifier);
		try {
			setState(432);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(427);
				integerTypeModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(428);
				realTypeModifier();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(429);
				boolTypeModifier();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(430);
				charTypeModifier();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(431);
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
		enterRule(_localctx, 70, RULE_integerTypeModifier);
		try {
			setState(439);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(434);
				match(Int);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(435);
				match(Long);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(436);
				match(Short);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(437);
				match(Long);
				setState(438);
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
		enterRule(_localctx, 72, RULE_realTypeModifier);
		try {
			setState(445);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Float:
				enterOuterAlt(_localctx, 1);
				{
				setState(441);
				match(Float);
				}
				break;
			case Double:
				enterOuterAlt(_localctx, 2);
				{
				setState(442);
				match(Double);
				}
				break;
			case Long:
				enterOuterAlt(_localctx, 3);
				{
				setState(443);
				match(Long);
				setState(444);
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
		enterRule(_localctx, 74, RULE_boolTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(447);
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
		enterRule(_localctx, 76, RULE_charTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(449);
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
		enterRule(_localctx, 78, RULE_voidTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(451);
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
		enterRule(_localctx, 80, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(453);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
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
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2"+
		"V\n\2\f\2\16\2Y\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5"+
		"\5g\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0086\n\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\7\6\u00be\n\6\f\6\16\6\u00c1\13\6\3\7\3\7\3\7\3\7\3\7\7\7\u00c8\n"+
		"\7\f\7\16\7\u00cb\13\7\5\7\u00cd\n\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\5\t\u00da\n\t\3\n\5\n\u00dd\n\n\3\n\3\n\3\13\3\13\7\13\u00e3"+
		"\n\13\f\13\16\13\u00e6\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\5\r\u00f6\n\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00fe\n\r\f"+
		"\r\16\r\u0101\13\r\3\r\3\r\5\r\u0105\n\r\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16"+
		"\u011a\n\16\f\16\16\16\u011d\13\16\5\16\u011f\n\16\3\16\3\16\5\16\u0123"+
		"\n\16\3\16\3\16\3\16\3\16\7\16\u0129\n\16\f\16\16\16\u012c\13\16\5\16"+
		"\u012e\n\16\3\16\3\16\5\16\u0132\n\16\3\17\3\17\3\17\3\17\5\17\u0138\n"+
		"\17\3\17\3\17\5\17\u013c\n\17\3\17\3\17\3\20\3\20\3\20\5\20\u0143\n\20"+
		"\3\21\3\21\3\21\3\21\3\22\3\22\3\22\7\22\u014c\n\22\f\22\16\22\u014f\13"+
		"\22\3\23\3\23\3\23\5\23\u0154\n\23\3\24\3\24\3\25\3\25\3\25\3\25\3\26"+
		"\3\26\3\26\3\26\3\27\3\27\5\27\u0162\n\27\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\5\30\u016b\n\30\3\30\3\30\3\31\3\31\3\31\7\31\u0172\n\31\f\31\16"+
		"\31\u0175\13\31\3\32\3\32\3\32\3\32\5\32\u017b\n\32\3\32\3\32\3\33\3\33"+
		"\3\33\3\33\3\33\3\34\3\34\5\34\u0186\n\34\3\35\3\35\3\35\3\36\3\36\3\36"+
		"\3\37\3\37\3\37\3\37\5\37\u0192\n\37\3\37\3\37\3 \3 \3 \7 \u0199\n \f"+
		" \16 \u019c\13 \3!\3!\3!\3!\3!\3!\3!\5!\u01a5\n!\3\"\3\"\5\"\u01a9\n\""+
		"\3#\3#\3#\3$\3$\3$\3$\3$\5$\u01b3\n$\3%\3%\3%\3%\3%\5%\u01ba\n%\3&\3&"+
		"\3&\3&\5&\u01c0\n&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\2\3\n+\2\4\6\b\n\f\16"+
		"\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\3\3\2\3"+
		"\b\2\u01ee\2W\3\2\2\2\4\\\3\2\2\2\6^\3\2\2\2\bf\3\2\2\2\n\u0085\3\2\2"+
		"\2\f\u00c2\3\2\2\2\16\u00d0\3\2\2\2\20\u00d9\3\2\2\2\22\u00dc\3\2\2\2"+
		"\24\u00e0\3\2\2\2\26\u00e9\3\2\2\2\30\u0104\3\2\2\2\32\u0131\3\2\2\2\34"+
		"\u013b\3\2\2\2\36\u0142\3\2\2\2 \u0144\3\2\2\2\"\u0148\3\2\2\2$\u0153"+
		"\3\2\2\2&\u0155\3\2\2\2(\u0157\3\2\2\2*\u015b\3\2\2\2,\u0161\3\2\2\2."+
		"\u0163\3\2\2\2\60\u016e\3\2\2\2\62\u0176\3\2\2\2\64\u017e\3\2\2\2\66\u0185"+
		"\3\2\2\28\u0187\3\2\2\2:\u018a\3\2\2\2<\u018d\3\2\2\2>\u0195\3\2\2\2@"+
		"\u01a4\3\2\2\2B\u01a8\3\2\2\2D\u01aa\3\2\2\2F\u01b2\3\2\2\2H\u01b9\3\2"+
		"\2\2J\u01bf\3\2\2\2L\u01c1\3\2\2\2N\u01c3\3\2\2\2P\u01c5\3\2\2\2R\u01c7"+
		"\3\2\2\2TV\5\36\20\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2"+
		"YW\3\2\2\2Z[\7\2\2\3[\3\3\2\2\2\\]\7\6\2\2]\5\3\2\2\2^_\5R*\2_\7\3\2\2"+
		"\2`g\7\u0086\2\2ab\7\u0086\2\2bc\7W\2\2cd\5\n\6\2de\7X\2\2eg\3\2\2\2f"+
		"`\3\2\2\2fa\3\2\2\2g\t\3\2\2\2hi\b\6\1\2i\u0086\5\f\7\2j\u0086\5R*\2k"+
		"\u0086\7\u0086\2\2lm\7U\2\2mn\5\n\6\2no\7V\2\2o\u0086\3\2\2\2pq\7d\2\2"+
		"q\u0086\5\n\6\33rs\7\\\2\2s\u0086\5\n\6\32tu\7a\2\2u\u0086\5\b\5\2vw\7"+
		"\u0086\2\2wx\7W\2\2xy\5\n\6\2yz\7X\2\2z\u0086\3\2\2\2{|\5\b\5\2|}\7e\2"+
		"\2}~\5\n\6\5~\u0086\3\2\2\2\177\u0080\5\b\5\2\u0080\u0081\7z\2\2\u0081"+
		"\u0086\3\2\2\2\u0082\u0083\5\b\5\2\u0083\u0084\7{\2\2\u0084\u0086\3\2"+
		"\2\2\u0085h\3\2\2\2\u0085j\3\2\2\2\u0085k\3\2\2\2\u0085l\3\2\2\2\u0085"+
		"p\3\2\2\2\u0085r\3\2\2\2\u0085t\3\2\2\2\u0085v\3\2\2\2\u0085{\3\2\2\2"+
		"\u0085\177\3\2\2\2\u0085\u0082\3\2\2\2\u0086\u00bf\3\2\2\2\u0087\u0088"+
		"\f\30\2\2\u0088\u0089\7]\2\2\u0089\u00be\5\n\6\31\u008a\u008b\f\27\2\2"+
		"\u008b\u008c\7^\2\2\u008c\u00be\5\n\6\30\u008d\u008e\f\26\2\2\u008e\u008f"+
		"\7_\2\2\u008f\u00be\5\n\6\27\u0090\u0091\f\25\2\2\u0091\u0092\7[\2\2\u0092"+
		"\u00be\5\n\6\26\u0093\u0094\f\24\2\2\u0094\u0095\7\\\2\2\u0095\u00be\5"+
		"\n\6\25\u0096\u0097\f\23\2\2\u0097\u0098\7f\2\2\u0098\u00be\5\n\6\24\u0099"+
		"\u009a\f\22\2\2\u009a\u009b\7g\2\2\u009b\u00be\5\n\6\23\u009c\u009d\f"+
		"\21\2\2\u009d\u009e\7v\2\2\u009e\u00be\5\n\6\22\u009f\u00a0\f\20\2\2\u00a0"+
		"\u00a1\7w\2\2\u00a1\u00be\5\n\6\21\u00a2\u00a3\f\17\2\2\u00a3\u00a4\7"+
		"t\2\2\u00a4\u00be\5\n\6\20\u00a5\u00a6\f\16\2\2\u00a6\u00a7\7u\2\2\u00a7"+
		"\u00be\5\n\6\17\u00a8\u00a9\f\r\2\2\u00a9\u00aa\7b\2\2\u00aa\u00be\5\n"+
		"\6\16\u00ab\u00ac\f\f\2\2\u00ac\u00ad\7a\2\2\u00ad\u00be\5\n\6\r\u00ae"+
		"\u00af\f\13\2\2\u00af\u00b0\7`\2\2\u00b0\u00be\5\n\6\f\u00b1\u00b2\f\n"+
		"\2\2\u00b2\u00b3\7y\2\2\u00b3\u00be\5\n\6\13\u00b4\u00b5\f\t\2\2\u00b5"+
		"\u00b6\7x\2\2\u00b6\u00be\5\n\6\n\u00b7\u00b8\f\b\2\2\u00b8\u00b9\7p\2"+
		"\2\u00b9\u00be\5\n\6\t\u00ba\u00bb\f\7\2\2\u00bb\u00bc\7r\2\2\u00bc\u00be"+
		"\5\n\6\b\u00bd\u0087\3\2\2\2\u00bd\u008a\3\2\2\2\u00bd\u008d\3\2\2\2\u00bd"+
		"\u0090\3\2\2\2\u00bd\u0093\3\2\2\2\u00bd\u0096\3\2\2\2\u00bd\u0099\3\2"+
		"\2\2\u00bd\u009c\3\2\2\2\u00bd\u009f\3\2\2\2\u00bd\u00a2\3\2\2\2\u00bd"+
		"\u00a5\3\2\2\2\u00bd\u00a8\3\2\2\2\u00bd\u00ab\3\2\2\2\u00bd\u00ae\3\2"+
		"\2\2\u00bd\u00b1\3\2\2\2\u00bd\u00b4\3\2\2\2\u00bd\u00b7\3\2\2\2\u00bd"+
		"\u00ba\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2"+
		"\2\2\u00c0\13\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c3\7\u0086\2\2\u00c3"+
		"\u00cc\7U\2\2\u00c4\u00c9\5\n\6\2\u00c5\u00c6\7|\2\2\u00c6\u00c8\5\n\6"+
		"\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca"+
		"\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00c4\3\2\2\2\u00cc"+
		"\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7V\2\2\u00cf\r\3\2\2\2"+
		"\u00d0\u00d1\5\n\6\2\u00d1\17\3\2\2\2\u00d2\u00da\5\22\n\2\u00d3\u00da"+
		"\5\24\13\2\u00d4\u00da\5\30\r\2\u00d5\u00da\5\32\16\2\u00d6\u00da\5\34"+
		"\17\2\u00d7\u00da\5 \21\2\u00d8\u00da\5,\27\2\u00d9\u00d2\3\2\2\2\u00d9"+
		"\u00d3\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9\u00d6\3\2"+
		"\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\21\3\2\2\2\u00db\u00dd"+
		"\5\n\6\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de"+
		"\u00df\7\u0082\2\2\u00df\23\3\2\2\2\u00e0\u00e4\7Y\2\2\u00e1\u00e3\5\20"+
		"\t\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4"+
		"\u00e5\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\7Z"+
		"\2\2\u00e8\25\3\2\2\2\u00e9\u00ea\7\20\2\2\u00ea\u00eb\5\6\4\2\u00eb\u00ec"+
		"\7\u0080\2\2\u00ec\u00ed\5\20\t\2\u00ed\27\3\2\2\2\u00ee\u00ef\7+\2\2"+
		"\u00ef\u00f0\7U\2\2\u00f0\u00f1\5\16\b\2\u00f1\u00f2\7V\2\2\u00f2\u00f5"+
		"\5\20\t\2\u00f3\u00f4\7 \2\2\u00f4\u00f6\5\20\t\2\u00f5\u00f3\3\2\2\2"+
		"\u00f5\u00f6\3\2\2\2\u00f6\u0105\3\2\2\2\u00f7\u00f8\7C\2\2\u00f8\u00f9"+
		"\7U\2\2\u00f9\u00fa\5\16\b\2\u00fa\u00fb\7V\2\2\u00fb\u00ff\7Y\2\2\u00fc"+
		"\u00fe\5\26\f\2\u00fd\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3"+
		"\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102"+
		"\u0103\7Z\2\2\u0103\u0105\3\2\2\2\u0104\u00ee\3\2\2\2\u0104\u00f7\3\2"+
		"\2\2\u0105\31\3\2\2\2\u0106\u0107\7T\2\2\u0107\u0108\7U\2\2\u0108\u0109"+
		"\5\16\b\2\u0109\u010a\7V\2\2\u010a\u010b\5\20\t\2\u010b\u0132\3\2\2\2"+
		"\u010c\u010d\7\35\2\2\u010d\u010e\5\20\t\2\u010e\u010f\7T\2\2\u010f\u0110"+
		"\7U\2\2\u0110\u0111\5\n\6\2\u0111\u0112\7V\2\2\u0112\u0113\7\u0082\2\2"+
		"\u0113\u0132\3\2\2\2\u0114\u0115\7(\2\2\u0115\u011e\7U\2\2\u0116\u011b"+
		"\5\n\6\2\u0117\u0118\7|\2\2\u0118\u011a\5\n\6\2\u0119\u0117\3\2\2\2\u011a"+
		"\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011f\3\2"+
		"\2\2\u011d\u011b\3\2\2\2\u011e\u0116\3\2\2\2\u011e\u011f\3\2\2\2\u011f"+
		"\u0120\3\2\2\2\u0120\u0122\7\u0082\2\2\u0121\u0123\5\n\6\2\u0122\u0121"+
		"\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u012d\7\u0082\2"+
		"\2\u0125\u012a\5\n\6\2\u0126\u0127\7|\2\2\u0127\u0129\5\n\6\2\u0128\u0126"+
		"\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b"+
		"\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u0125\3\2\2\2\u012d\u012e\3\2"+
		"\2\2\u012e\u012f\3\2\2\2\u012f\u0130\7V\2\2\u0130\u0132\5\20\t\2\u0131"+
		"\u0106\3\2\2\2\u0131\u010c\3\2\2\2\u0131\u0114\3\2\2\2\u0132\33\3\2\2"+
		"\2\u0133\u013c\7\17\2\2\u0134\u013c\7\31\2\2\u0135\u0137\7;\2\2\u0136"+
		"\u0138\5\n\6\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013c\3\2"+
		"\2\2\u0139\u013a\7*\2\2\u013a\u013c\7\u0086\2\2\u013b\u0133\3\2\2\2\u013b"+
		"\u0134\3\2\2\2\u013b\u0135\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d\3\2"+
		"\2\2\u013d\u013e\7\u0082\2\2\u013e\35\3\2\2\2\u013f\u0143\5 \21\2\u0140"+
		"\u0143\5,\27\2\u0141\u0143\5\66\34\2\u0142\u013f\3\2\2\2\u0142\u0140\3"+
		"\2\2\2\u0142\u0141\3\2\2\2\u0143\37\3\2\2\2\u0144\u0145\5B\"\2\u0145\u0146"+
		"\5\"\22\2\u0146\u0147\7\u0082\2\2\u0147!\3\2\2\2\u0148\u014d\5$\23\2\u0149"+
		"\u014a\7|\2\2\u014a\u014c\5$\23\2\u014b\u0149\3\2\2\2\u014c\u014f\3\2"+
		"\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e#\3\2\2\2\u014f\u014d"+
		"\3\2\2\2\u0150\u0154\5&\24\2\u0151\u0154\5(\25\2\u0152\u0154\5*\26\2\u0153"+
		"\u0150\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0154%\3\2\2\2"+
		"\u0155\u0156\7\u0086\2\2\u0156\'\3\2\2\2\u0157\u0158\7\u0086\2\2\u0158"+
		"\u0159\7e\2\2\u0159\u015a\5\6\4\2\u015a)\3\2\2\2\u015b\u015c\7\u0086\2"+
		"\2\u015c\u015d\7e\2\2\u015d\u015e\5\n\6\2\u015e+\3\2\2\2\u015f\u0162\5"+
		".\30\2\u0160\u0162\5\62\32\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162"+
		"-\3\2\2\2\u0163\u0164\5F$\2\u0164\u016a\5\64\33\2\u0165\u0166\7e\2\2\u0166"+
		"\u0167\7Y\2\2\u0167\u0168\5\60\31\2\u0168\u0169\7Z\2\2\u0169\u016b\3\2"+
		"\2\2\u016a\u0165\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c"+
		"\u016d\7\u0082\2\2\u016d/\3\2\2\2\u016e\u0173\5\n\6\2\u016f\u0170\7|\2"+
		"\2\u0170\u0172\5\n\6\2\u0171\u016f\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171"+
		"\3\2\2\2\u0173\u0174\3\2\2\2\u0174\61\3\2\2\2\u0175\u0173\3\2\2\2\u0176"+
		"\u0177\5N(\2\u0177\u017a\5\64\33\2\u0178\u0179\7e\2\2\u0179\u017b\5\4"+
		"\3\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c"+
		"\u017d\7\u0082\2\2\u017d\63\3\2\2\2\u017e\u017f\7\u0086\2\2\u017f\u0180"+
		"\7W\2\2\u0180\u0181\7\u0087\2\2\u0181\u0182\7X\2\2\u0182\65\3\2\2\2\u0183"+
		"\u0186\58\35\2\u0184\u0186\5:\36\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2"+
		"\2\2\u0186\67\3\2\2\2\u0187\u0188\5<\37\2\u0188\u0189\7\u0082\2\2\u0189"+
		"9\3\2\2\2\u018a\u018b\5<\37\2\u018b\u018c\5\24\13\2\u018c;\3\2\2\2\u018d"+
		"\u018e\5B\"\2\u018e\u018f\7\u0086\2\2\u018f\u0191\7U\2\2\u0190\u0192\5"+
		"> \2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193"+
		"\u0194\7V\2\2\u0194=\3\2\2\2\u0195\u019a\5@!\2\u0196\u0197\7|\2\2\u0197"+
		"\u0199\5@!\2\u0198\u0196\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2"+
		"\2\u019a\u019b\3\2\2\2\u019b?\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e"+
		"\5D#\2\u019e\u019f\7\u0086\2\2\u019f\u01a5\3\2\2\2\u01a0\u01a1\5F$\2\u01a1"+
		"\u01a2\7\u0086\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a5\7\u0085\2\2\u01a4\u019d"+
		"\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5A\3\2\2\2\u01a6"+
		"\u01a9\5D#\2\u01a7\u01a9\5F$\2\u01a8\u01a6\3\2\2\2\u01a8\u01a7\3\2\2\2"+
		"\u01a9C\3\2\2\2\u01aa\u01ab\5F$\2\u01ab\u01ac\7]\2\2\u01acE\3\2\2\2\u01ad"+
		"\u01b3\5H%\2\u01ae\u01b3\5J&\2\u01af\u01b3\5L\'\2\u01b0\u01b3\5N(\2\u01b1"+
		"\u01b3\5P)\2\u01b2\u01ad\3\2\2\2\u01b2\u01ae\3\2\2\2\u01b2\u01af\3\2\2"+
		"\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3G\3\2\2\2\u01b4\u01ba"+
		"\7-\2\2\u01b5\u01ba\7.\2\2\u01b6\u01ba\7<\2\2\u01b7\u01b8\7.\2\2\u01b8"+
		"\u01ba\7.\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01b5\3\2\2\2\u01b9\u01b6\3\2"+
		"\2\2\u01b9\u01b7\3\2\2\2\u01baI\3\2\2\2\u01bb\u01c0\7\'\2\2\u01bc\u01c0"+
		"\7\36\2\2\u01bd\u01be\7.\2\2\u01be\u01c0\7\36\2\2\u01bf\u01bb\3\2\2\2"+
		"\u01bf\u01bc\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0K\3\2\2\2\u01c1\u01c2\7"+
		"\16\2\2\u01c2M\3\2\2\2\u01c3\u01c4\7\22\2\2\u01c4O\3\2\2\2\u01c5\u01c6"+
		"\7Q\2\2\u01c6Q\3\2\2\2\u01c7\u01c8\t\2\2\2\u01c8S\3\2\2\2&Wf\u0085\u00bd"+
		"\u00bf\u00c9\u00cc\u00d9\u00dc\u00e4\u00f5\u00ff\u0104\u011b\u011e\u0122"+
		"\u012a\u012d\u0131\u0137\u013b\u0142\u014d\u0153\u0161\u016a\u0173\u017a"+
		"\u0185\u0191\u019a\u01a4\u01a8\u01b2\u01b9\u01bf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}