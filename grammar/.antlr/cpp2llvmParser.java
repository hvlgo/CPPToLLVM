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
		RULE_translationUnit = 0, RULE_literal = 1, RULE_integerLiteral = 2, RULE_characterLiteral = 3, 
		RULE_floatingLiteral = 4, RULE_stringLiteral = 5, RULE_constExpression = 6, 
		RULE_leftExpression = 7, RULE_expression = 8, RULE_functionCall = 9, RULE_statement = 10, 
		RULE_compoundStatement = 11, RULE_expressionStatement = 12, RULE_ifStatement = 13, 
		RULE_switchStatement = 14, RULE_caseStatement = 15, RULE_whileStatement = 16, 
		RULE_doWhileStatement = 17, RULE_forStatement = 18, RULE_forExprSet = 19, 
		RULE_returnStatement = 20, RULE_breakStatement = 21, RULE_continueStatement = 22, 
		RULE_declaration = 23, RULE_variableDeclarator = 24, RULE_variableDeclarationList = 25, 
		RULE_variableDeclaration = 26, RULE_varDeclWithoutInit = 27, RULE_varDeclWithConstInit = 28, 
		RULE_varDeclWithNormalInit = 29, RULE_arrayDeclarator = 30, RULE_normalArrayDeclaration = 31, 
		RULE_arrayAssginExpressionList = 32, RULE_stringDeclaration = 33, RULE_arrayName = 34, 
		RULE_functionDeclarator = 35, RULE_functionDeclaration = 36, RULE_functionDefinition = 37, 
		RULE_functionHead = 38, RULE_functionParameterList = 39, RULE_functionParameter = 40, 
		RULE_typeModifier = 41, RULE_pointerTypeModifier = 42, RULE_normalTypeModifier = 43, 
		RULE_integerTypeModifier = 44, RULE_realTypeModifier = 45, RULE_boolTypeModifier = 46, 
		RULE_charTypeModifier = 47, RULE_voidTypeModifier = 48;
	private static String[] makeRuleNames() {
		return new String[] {
			"translationUnit", "literal", "integerLiteral", "characterLiteral", "floatingLiteral", 
			"stringLiteral", "constExpression", "leftExpression", "expression", "functionCall", 
			"statement", "compoundStatement", "expressionStatement", "ifStatement", 
			"switchStatement", "caseStatement", "whileStatement", "doWhileStatement", 
			"forStatement", "forExprSet", "returnStatement", "breakStatement", "continueStatement", 
			"declaration", "variableDeclarator", "variableDeclarationList", "variableDeclaration", 
			"varDeclWithoutInit", "varDeclWithConstInit", "varDeclWithNormalInit", 
			"arrayDeclarator", "normalArrayDeclaration", "arrayAssginExpressionList", 
			"stringDeclaration", "arrayName", "functionDeclarator", "functionDeclaration", 
			"functionDefinition", "functionHead", "functionParameterList", "functionParameter", 
			"typeModifier", "pointerTypeModifier", "normalTypeModifier", "integerTypeModifier", 
			"realTypeModifier", "boolTypeModifier", "charTypeModifier", "voidTypeModifier"
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
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Bool) | (1L << Char) | (1L << Double) | (1L << Float) | (1L << Int) | (1L << Long) | (1L << Short))) != 0) || _la==Void) {
				{
				{
				setState(98);
				declaration();
				}
				}
				setState(103);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(104);
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

	public static class LiteralContext extends ParserRuleContext {
		public IntegerLiteralContext integerLiteral() {
			return getRuleContext(IntegerLiteralContext.class,0);
		}
		public CharacterLiteralContext characterLiteral() {
			return getRuleContext(CharacterLiteralContext.class,0);
		}
		public FloatingLiteralContext floatingLiteral() {
			return getRuleContext(FloatingLiteralContext.class,0);
		}
		public StringLiteralContext stringLiteral() {
			return getRuleContext(StringLiteralContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_literal);
		try {
			setState(110);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IntegerLiteral:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				integerLiteral();
				}
				break;
			case CharacterLiteral:
				enterOuterAlt(_localctx, 2);
				{
				setState(107);
				characterLiteral();
				}
				break;
			case FloatingLiteral:
				enterOuterAlt(_localctx, 3);
				{
				setState(108);
				floatingLiteral();
				}
				break;
			case StringLiteral:
				enterOuterAlt(_localctx, 4);
				{
				setState(109);
				stringLiteral();
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

	public static class IntegerLiteralContext extends ParserRuleContext {
		public TerminalNode IntegerLiteral() { return getToken(cpp2llvmParser.IntegerLiteral, 0); }
		public IntegerLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integerLiteral; }
	}

	public final IntegerLiteralContext integerLiteral() throws RecognitionException {
		IntegerLiteralContext _localctx = new IntegerLiteralContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_integerLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(IntegerLiteral);
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

	public static class CharacterLiteralContext extends ParserRuleContext {
		public TerminalNode CharacterLiteral() { return getToken(cpp2llvmParser.CharacterLiteral, 0); }
		public CharacterLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_characterLiteral; }
	}

	public final CharacterLiteralContext characterLiteral() throws RecognitionException {
		CharacterLiteralContext _localctx = new CharacterLiteralContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_characterLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(CharacterLiteral);
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

	public static class FloatingLiteralContext extends ParserRuleContext {
		public TerminalNode FloatingLiteral() { return getToken(cpp2llvmParser.FloatingLiteral, 0); }
		public FloatingLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_floatingLiteral; }
	}

	public final FloatingLiteralContext floatingLiteral() throws RecognitionException {
		FloatingLiteralContext _localctx = new FloatingLiteralContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_floatingLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(FloatingLiteral);
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
		enterRule(_localctx, 10, RULE_stringLiteral);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
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
		enterRule(_localctx, 12, RULE_constExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
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
		enterRule(_localctx, 14, RULE_leftExpression);
		try {
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(122);
				match(Identifier);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(123);
				match(Identifier);
				{
				setState(124);
				match(LeftBracket);
				setState(125);
				expression(0);
				setState(126);
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
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(131);
				functionCall();
				}
				break;
			case 2:
				{
				setState(132);
				literal();
				}
				break;
			case 3:
				{
				setState(133);
				match(Identifier);
				}
				break;
			case 4:
				{
				setState(134);
				match(LeftParen);
				setState(135);
				expression(0);
				setState(136);
				match(RightParen);
				}
				break;
			case 5:
				{
				setState(138);
				match(Not);
				setState(139);
				expression(25);
				}
				break;
			case 6:
				{
				setState(140);
				match(Minus);
				setState(141);
				expression(24);
				}
				break;
			case 7:
				{
				setState(142);
				match(And);
				setState(143);
				leftExpression();
				}
				break;
			case 8:
				{
				setState(144);
				match(Identifier);
				setState(145);
				match(LeftBracket);
				setState(146);
				expression(0);
				setState(147);
				match(RightBracket);
				}
				break;
			case 9:
				{
				setState(149);
				leftExpression();
				setState(150);
				match(Assign);
				setState(151);
				expression(3);
				}
				break;
			case 10:
				{
				setState(153);
				leftExpression();
				setState(154);
				match(PlusPlus);
				}
				break;
			case 11:
				{
				setState(156);
				leftExpression();
				setState(157);
				match(MinusMinus);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(217);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(215);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(161);
						if (!(precpred(_ctx, 22))) throw new FailedPredicateException(this, "precpred(_ctx, 22)");
						setState(162);
						match(Star);
						setState(163);
						expression(23);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(164);
						if (!(precpred(_ctx, 21))) throw new FailedPredicateException(this, "precpred(_ctx, 21)");
						setState(165);
						match(Div);
						setState(166);
						expression(22);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(167);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(168);
						match(Mod);
						setState(169);
						expression(21);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(170);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(171);
						match(Plus);
						setState(172);
						expression(20);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(173);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(174);
						match(Minus);
						setState(175);
						expression(19);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(176);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(177);
						match(Less);
						setState(178);
						expression(18);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(179);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(180);
						match(Greater);
						setState(181);
						expression(17);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(182);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(183);
						match(LessEqual);
						setState(184);
						expression(16);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(185);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(186);
						match(GreaterEqual);
						setState(187);
						expression(15);
						}
						break;
					case 10:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(188);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(189);
						match(Equal);
						setState(190);
						expression(14);
						}
						break;
					case 11:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(191);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(192);
						match(NotEqual);
						setState(193);
						expression(13);
						}
						break;
					case 12:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(194);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(195);
						match(Or);
						setState(196);
						expression(12);
						}
						break;
					case 13:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(197);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(198);
						match(And);
						setState(199);
						expression(11);
						}
						break;
					case 14:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(200);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(201);
						match(Caret);
						setState(202);
						expression(10);
						}
						break;
					case 15:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(203);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(204);
						match(OrOr);
						setState(205);
						expression(9);
						}
						break;
					case 16:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(206);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(207);
						match(AndAnd);
						setState(208);
						expression(8);
						}
						break;
					case 17:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(209);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(210);
						match(LeftShift);
						setState(211);
						expression(7);
						}
						break;
					case 18:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(212);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(213);
						match(RightShift);
						setState(214);
						expression(6);
						}
						break;
					}
					} 
				}
				setState(219);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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
		enterRule(_localctx, 18, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(Identifier);
			setState(221);
			match(LeftParen);
			setState(230);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(222);
				expression(0);
				setState(227);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==Comma) {
					{
					{
					setState(223);
					match(Comma);
					setState(224);
					expression(0);
					}
					}
					setState(229);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(232);
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

	public static class StatementContext extends ParserRuleContext {
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public SwitchStatementContext switchStatement() {
			return getRuleContext(SwitchStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public DoWhileStatementContext doWhileStatement() {
			return getRuleContext(DoWhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public BreakStatementContext breakStatement() {
			return getRuleContext(BreakStatementContext.class,0);
		}
		public ContinueStatementContext continueStatement() {
			return getRuleContext(ContinueStatementContext.class,0);
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
		enterRule(_localctx, 20, RULE_statement);
		try {
			setState(246);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				expressionStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(235);
				compoundStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(236);
				ifStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(237);
				switchStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(238);
				whileStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(239);
				doWhileStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(240);
				forStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(241);
				returnStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(242);
				breakStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(243);
				continueStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(244);
				variableDeclarator();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(245);
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
		enterRule(_localctx, 22, RULE_compoundStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(LeftBrace);
			setState(252);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral) | (1L << Bool) | (1L << Break) | (1L << Char) | (1L << Continue) | (1L << Do) | (1L << Double) | (1L << Float) | (1L << For) | (1L << If) | (1L << Int) | (1L << Long) | (1L << Return) | (1L << Short))) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & ((1L << (Switch - 65)) | (1L << (Void - 65)) | (1L << (While - 65)) | (1L << (LeftParen - 65)) | (1L << (LeftBrace - 65)) | (1L << (Minus - 65)) | (1L << (And - 65)) | (1L << (Not - 65)) | (1L << (Semi - 65)))) != 0) || _la==Identifier) {
				{
				{
				setState(249);
				statement();
				}
				}
				setState(254);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(255);
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
		enterRule(_localctx, 24, RULE_expressionStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(257);
				expression(0);
				}
			}

			setState(260);
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

	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode If() { return getToken(cpp2llvmParser.If, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode Else() { return getToken(cpp2llvmParser.Else, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(262);
			match(If);
			setState(263);
			match(LeftParen);
			setState(264);
			expression(0);
			setState(265);
			match(RightParen);
			setState(266);
			statement();
			setState(269);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(267);
				match(Else);
				setState(268);
				statement();
				}
				break;
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

	public static class SwitchStatementContext extends ParserRuleContext {
		public TerminalNode Switch() { return getToken(cpp2llvmParser.Switch, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public TerminalNode LeftBrace() { return getToken(cpp2llvmParser.LeftBrace, 0); }
		public TerminalNode RightBrace() { return getToken(cpp2llvmParser.RightBrace, 0); }
		public List<CaseStatementContext> caseStatement() {
			return getRuleContexts(CaseStatementContext.class);
		}
		public CaseStatementContext caseStatement(int i) {
			return getRuleContext(CaseStatementContext.class,i);
		}
		public SwitchStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatement; }
	}

	public final SwitchStatementContext switchStatement() throws RecognitionException {
		SwitchStatementContext _localctx = new SwitchStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_switchStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(Switch);
			setState(272);
			match(LeftParen);
			setState(273);
			expression(0);
			setState(274);
			match(RightParen);
			setState(275);
			match(LeftBrace);
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Case) {
				{
				{
				setState(276);
				caseStatement();
				}
				}
				setState(281);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(282);
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
		enterRule(_localctx, 30, RULE_caseStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(Case);
			setState(285);
			constExpression();
			setState(286);
			match(Colon);
			setState(287);
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

	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode While() { return getToken(cpp2llvmParser.While, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(289);
			match(While);
			setState(290);
			match(LeftParen);
			setState(291);
			expression(0);
			setState(292);
			match(RightParen);
			setState(293);
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

	public static class DoWhileStatementContext extends ParserRuleContext {
		public TerminalNode Do() { return getToken(cpp2llvmParser.Do, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode While() { return getToken(cpp2llvmParser.While, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public DoWhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doWhileStatement; }
	}

	public final DoWhileStatementContext doWhileStatement() throws RecognitionException {
		DoWhileStatementContext _localctx = new DoWhileStatementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_doWhileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			match(Do);
			setState(296);
			statement();
			setState(297);
			match(While);
			setState(298);
			match(LeftParen);
			setState(299);
			expression(0);
			setState(300);
			match(RightParen);
			setState(301);
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

	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode For() { return getToken(cpp2llvmParser.For, 0); }
		public TerminalNode LeftParen() { return getToken(cpp2llvmParser.LeftParen, 0); }
		public List<TerminalNode> Semi() { return getTokens(cpp2llvmParser.Semi); }
		public TerminalNode Semi(int i) {
			return getToken(cpp2llvmParser.Semi, i);
		}
		public TerminalNode RightParen() { return getToken(cpp2llvmParser.RightParen, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public List<ForExprSetContext> forExprSet() {
			return getRuleContexts(ForExprSetContext.class);
		}
		public ForExprSetContext forExprSet(int i) {
			return getRuleContext(ForExprSetContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			match(For);
			setState(304);
			match(LeftParen);
			setState(306);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(305);
				forExprSet();
				}
			}

			setState(308);
			match(Semi);
			setState(310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(309);
				expression(0);
				}
			}

			setState(312);
			match(Semi);
			setState(314);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(313);
				forExprSet();
				}
			}

			setState(316);
			match(RightParen);
			setState(317);
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

	public static class ForExprSetContext extends ParserRuleContext {
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
		public ForExprSetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forExprSet; }
	}

	public final ForExprSetContext forExprSet() throws RecognitionException {
		ForExprSetContext _localctx = new ForExprSetContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_forExprSet);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(319);
			expression(0);
			setState(324);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(320);
				match(Comma);
				setState(321);
				expression(0);
				}
				}
				setState(326);
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

	public static class ReturnStatementContext extends ParserRuleContext {
		public TerminalNode Return() { return getToken(cpp2llvmParser.Return, 0); }
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_returnStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			match(Return);
			setState(329);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IntegerLiteral) | (1L << CharacterLiteral) | (1L << FloatingLiteral) | (1L << StringLiteral))) != 0) || ((((_la - 83)) & ~0x3f) == 0 && ((1L << (_la - 83)) & ((1L << (LeftParen - 83)) | (1L << (Minus - 83)) | (1L << (And - 83)) | (1L << (Not - 83)) | (1L << (Identifier - 83)))) != 0)) {
				{
				setState(328);
				expression(0);
				}
			}

			setState(331);
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

	public static class BreakStatementContext extends ParserRuleContext {
		public TerminalNode Break() { return getToken(cpp2llvmParser.Break, 0); }
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public BreakStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakStatement; }
	}

	public final BreakStatementContext breakStatement() throws RecognitionException {
		BreakStatementContext _localctx = new BreakStatementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_breakStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			match(Break);
			setState(334);
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

	public static class ContinueStatementContext extends ParserRuleContext {
		public TerminalNode Continue() { return getToken(cpp2llvmParser.Continue, 0); }
		public TerminalNode Semi() { return getToken(cpp2llvmParser.Semi, 0); }
		public ContinueStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continueStatement; }
	}

	public final ContinueStatementContext continueStatement() throws RecognitionException {
		ContinueStatementContext _localctx = new ContinueStatementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_continueStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			match(Continue);
			setState(337);
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
		enterRule(_localctx, 46, RULE_declaration);
		try {
			setState(342);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(339);
				variableDeclarator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(340);
				arrayDeclarator();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(341);
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
		enterRule(_localctx, 48, RULE_variableDeclarator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			typeModifier();
			setState(345);
			variableDeclarationList();
			setState(346);
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
		enterRule(_localctx, 50, RULE_variableDeclarationList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			variableDeclaration();
			setState(353);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(349);
				match(Comma);
				setState(350);
				variableDeclaration();
				}
				}
				setState(355);
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
		enterRule(_localctx, 52, RULE_variableDeclaration);
		try {
			setState(359);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(356);
				varDeclWithoutInit();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(357);
				varDeclWithConstInit();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(358);
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
		enterRule(_localctx, 54, RULE_varDeclWithoutInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(361);
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
		enterRule(_localctx, 56, RULE_varDeclWithConstInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(363);
			match(Identifier);
			setState(364);
			match(Assign);
			setState(365);
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
		enterRule(_localctx, 58, RULE_varDeclWithNormalInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(367);
			match(Identifier);
			setState(368);
			match(Assign);
			setState(369);
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
		enterRule(_localctx, 60, RULE_arrayDeclarator);
		try {
			setState(373);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(371);
				normalArrayDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(372);
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
		enterRule(_localctx, 62, RULE_normalArrayDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			normalTypeModifier();
			setState(376);
			arrayName();
			setState(382);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(377);
				match(Assign);
				setState(378);
				match(LeftBrace);
				setState(379);
				arrayAssginExpressionList();
				setState(380);
				match(RightBrace);
				}
			}

			setState(384);
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
		enterRule(_localctx, 64, RULE_arrayAssginExpressionList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(386);
			expression(0);
			setState(391);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(387);
				match(Comma);
				setState(388);
				expression(0);
				}
				}
				setState(393);
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
		enterRule(_localctx, 66, RULE_stringDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			charTypeModifier();
			setState(395);
			arrayName();
			setState(398);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Assign) {
				{
				setState(396);
				match(Assign);
				setState(397);
				stringLiteral();
				}
			}

			setState(400);
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
		enterRule(_localctx, 68, RULE_arrayName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			match(Identifier);
			setState(403);
			match(LeftBracket);
			setState(404);
			match(IntegerLiteral);
			setState(405);
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
		enterRule(_localctx, 70, RULE_functionDeclarator);
		try {
			setState(409);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(407);
				functionDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(408);
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
		enterRule(_localctx, 72, RULE_functionDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(411);
			functionHead();
			setState(412);
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
		enterRule(_localctx, 74, RULE_functionDefinition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			functionHead();
			setState(415);
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
		enterRule(_localctx, 76, RULE_functionHead);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(417);
			typeModifier();
			setState(418);
			match(Identifier);
			setState(419);
			match(LeftParen);
			setState(421);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Bool) | (1L << Char) | (1L << Double) | (1L << Float) | (1L << Int) | (1L << Long) | (1L << Short))) != 0) || _la==Void || _la==Ellipsis) {
				{
				setState(420);
				functionParameterList();
				}
			}

			setState(423);
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
		enterRule(_localctx, 78, RULE_functionParameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(425);
			functionParameter();
			setState(430);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Comma) {
				{
				{
				setState(426);
				match(Comma);
				setState(427);
				functionParameter();
				}
				}
				setState(432);
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
		public TypeModifierContext typeModifier() {
			return getRuleContext(TypeModifierContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(cpp2llvmParser.Identifier, 0); }
		public TerminalNode Ellipsis() { return getToken(cpp2llvmParser.Ellipsis, 0); }
		public FunctionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionParameter; }
	}

	public final FunctionParameterContext functionParameter() throws RecognitionException {
		FunctionParameterContext _localctx = new FunctionParameterContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_functionParameter);
		try {
			setState(437);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Bool:
			case Char:
			case Double:
			case Float:
			case Int:
			case Long:
			case Short:
			case Void:
				enterOuterAlt(_localctx, 1);
				{
				setState(433);
				typeModifier();
				setState(434);
				match(Identifier);
				}
				break;
			case Ellipsis:
				enterOuterAlt(_localctx, 2);
				{
				setState(436);
				match(Ellipsis);
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
		enterRule(_localctx, 82, RULE_typeModifier);
		try {
			setState(441);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(439);
				pointerTypeModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(440);
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
		enterRule(_localctx, 84, RULE_pointerTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(443);
			normalTypeModifier();
			setState(444);
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
		enterRule(_localctx, 86, RULE_normalTypeModifier);
		try {
			setState(451);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(446);
				integerTypeModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(447);
				realTypeModifier();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(448);
				boolTypeModifier();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(449);
				charTypeModifier();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(450);
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
		enterRule(_localctx, 88, RULE_integerTypeModifier);
		try {
			setState(458);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(453);
				match(Int);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(454);
				match(Long);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(455);
				match(Short);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(456);
				match(Long);
				setState(457);
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
		enterRule(_localctx, 90, RULE_realTypeModifier);
		try {
			setState(464);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Float:
				enterOuterAlt(_localctx, 1);
				{
				setState(460);
				match(Float);
				}
				break;
			case Double:
				enterOuterAlt(_localctx, 2);
				{
				setState(461);
				match(Double);
				}
				break;
			case Long:
				enterOuterAlt(_localctx, 3);
				{
				setState(462);
				match(Long);
				setState(463);
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
		enterRule(_localctx, 92, RULE_boolTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(466);
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
		enterRule(_localctx, 94, RULE_charTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(468);
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
		enterRule(_localctx, 96, RULE_voidTypeModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(470);
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
		case 8:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u008f\u01db\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\7\2f\n\2\f\2"+
		"\16\2i\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3q\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3"+
		"\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0083\n\t\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a2\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00da\n\n\f\n\16"+
		"\n\u00dd\13\n\3\13\3\13\3\13\3\13\3\13\7\13\u00e4\n\13\f\13\16\13\u00e7"+
		"\13\13\5\13\u00e9\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\5\f\u00f9\n\f\3\r\3\r\7\r\u00fd\n\r\f\r\16\r\u0100\13\r\3\r"+
		"\3\r\3\16\5\16\u0105\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\5\17\u0110\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0118\n\20\f\20\16"+
		"\20\u011b\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\5\24"+
		"\u0135\n\24\3\24\3\24\5\24\u0139\n\24\3\24\3\24\5\24\u013d\n\24\3\24\3"+
		"\24\3\24\3\25\3\25\3\25\7\25\u0145\n\25\f\25\16\25\u0148\13\25\3\26\3"+
		"\26\5\26\u014c\n\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31"+
		"\3\31\5\31\u0159\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\7\33\u0162\n"+
		"\33\f\33\16\33\u0165\13\33\3\34\3\34\3\34\5\34\u016a\n\34\3\35\3\35\3"+
		"\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \5 \u0178\n \3!\3!\3!\3!\3"+
		"!\3!\3!\5!\u0181\n!\3!\3!\3\"\3\"\3\"\7\"\u0188\n\"\f\"\16\"\u018b\13"+
		"\"\3#\3#\3#\3#\5#\u0191\n#\3#\3#\3$\3$\3$\3$\3$\3%\3%\5%\u019c\n%\3&\3"+
		"&\3&\3\'\3\'\3\'\3(\3(\3(\3(\5(\u01a8\n(\3(\3(\3)\3)\3)\7)\u01af\n)\f"+
		")\16)\u01b2\13)\3*\3*\3*\3*\5*\u01b8\n*\3+\3+\5+\u01bc\n+\3,\3,\3,\3-"+
		"\3-\3-\3-\3-\5-\u01c6\n-\3.\3.\3.\3.\3.\5.\u01cd\n.\3/\3/\3/\3/\5/\u01d3"+
		"\n/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\2\3\22\63\2\4\6\b\n\f\16\20\22"+
		"\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\2\2\u01f7"+
		"\2g\3\2\2\2\4p\3\2\2\2\6r\3\2\2\2\bt\3\2\2\2\nv\3\2\2\2\fx\3\2\2\2\16"+
		"z\3\2\2\2\20\u0082\3\2\2\2\22\u00a1\3\2\2\2\24\u00de\3\2\2\2\26\u00f8"+
		"\3\2\2\2\30\u00fa\3\2\2\2\32\u0104\3\2\2\2\34\u0108\3\2\2\2\36\u0111\3"+
		"\2\2\2 \u011e\3\2\2\2\"\u0123\3\2\2\2$\u0129\3\2\2\2&\u0131\3\2\2\2(\u0141"+
		"\3\2\2\2*\u0149\3\2\2\2,\u014f\3\2\2\2.\u0152\3\2\2\2\60\u0158\3\2\2\2"+
		"\62\u015a\3\2\2\2\64\u015e\3\2\2\2\66\u0169\3\2\2\28\u016b\3\2\2\2:\u016d"+
		"\3\2\2\2<\u0171\3\2\2\2>\u0177\3\2\2\2@\u0179\3\2\2\2B\u0184\3\2\2\2D"+
		"\u018c\3\2\2\2F\u0194\3\2\2\2H\u019b\3\2\2\2J\u019d\3\2\2\2L\u01a0\3\2"+
		"\2\2N\u01a3\3\2\2\2P\u01ab\3\2\2\2R\u01b7\3\2\2\2T\u01bb\3\2\2\2V\u01bd"+
		"\3\2\2\2X\u01c5\3\2\2\2Z\u01cc\3\2\2\2\\\u01d2\3\2\2\2^\u01d4\3\2\2\2"+
		"`\u01d6\3\2\2\2b\u01d8\3\2\2\2df\5\60\31\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2"+
		"\2gh\3\2\2\2hj\3\2\2\2ig\3\2\2\2jk\7\2\2\3k\3\3\2\2\2lq\5\6\4\2mq\5\b"+
		"\5\2nq\5\n\6\2oq\5\f\7\2pl\3\2\2\2pm\3\2\2\2pn\3\2\2\2po\3\2\2\2q\5\3"+
		"\2\2\2rs\7\3\2\2s\7\3\2\2\2tu\7\4\2\2u\t\3\2\2\2vw\7\5\2\2w\13\3\2\2\2"+
		"xy\7\6\2\2y\r\3\2\2\2z{\5\4\3\2{\17\3\2\2\2|\u0083\7\u0086\2\2}~\7\u0086"+
		"\2\2~\177\7W\2\2\177\u0080\5\22\n\2\u0080\u0081\7X\2\2\u0081\u0083\3\2"+
		"\2\2\u0082|\3\2\2\2\u0082}\3\2\2\2\u0083\21\3\2\2\2\u0084\u0085\b\n\1"+
		"\2\u0085\u00a2\5\24\13\2\u0086\u00a2\5\4\3\2\u0087\u00a2\7\u0086\2\2\u0088"+
		"\u0089\7U\2\2\u0089\u008a\5\22\n\2\u008a\u008b\7V\2\2\u008b\u00a2\3\2"+
		"\2\2\u008c\u008d\7d\2\2\u008d\u00a2\5\22\n\33\u008e\u008f\7\\\2\2\u008f"+
		"\u00a2\5\22\n\32\u0090\u0091\7a\2\2\u0091\u00a2\5\20\t\2\u0092\u0093\7"+
		"\u0086\2\2\u0093\u0094\7W\2\2\u0094\u0095\5\22\n\2\u0095\u0096\7X\2\2"+
		"\u0096\u00a2\3\2\2\2\u0097\u0098\5\20\t\2\u0098\u0099\7e\2\2\u0099\u009a"+
		"\5\22\n\5\u009a\u00a2\3\2\2\2\u009b\u009c\5\20\t\2\u009c\u009d\7z\2\2"+
		"\u009d\u00a2\3\2\2\2\u009e\u009f\5\20\t\2\u009f\u00a0\7{\2\2\u00a0\u00a2"+
		"\3\2\2\2\u00a1\u0084\3\2\2\2\u00a1\u0086\3\2\2\2\u00a1\u0087\3\2\2\2\u00a1"+
		"\u0088\3\2\2\2\u00a1\u008c\3\2\2\2\u00a1\u008e\3\2\2\2\u00a1\u0090\3\2"+
		"\2\2\u00a1\u0092\3\2\2\2\u00a1\u0097\3\2\2\2\u00a1\u009b\3\2\2\2\u00a1"+
		"\u009e\3\2\2\2\u00a2\u00db\3\2\2\2\u00a3\u00a4\f\30\2\2\u00a4\u00a5\7"+
		"]\2\2\u00a5\u00da\5\22\n\31\u00a6\u00a7\f\27\2\2\u00a7\u00a8\7^\2\2\u00a8"+
		"\u00da\5\22\n\30\u00a9\u00aa\f\26\2\2\u00aa\u00ab\7_\2\2\u00ab\u00da\5"+
		"\22\n\27\u00ac\u00ad\f\25\2\2\u00ad\u00ae\7[\2\2\u00ae\u00da\5\22\n\26"+
		"\u00af\u00b0\f\24\2\2\u00b0\u00b1\7\\\2\2\u00b1\u00da\5\22\n\25\u00b2"+
		"\u00b3\f\23\2\2\u00b3\u00b4\7f\2\2\u00b4\u00da\5\22\n\24\u00b5\u00b6\f"+
		"\22\2\2\u00b6\u00b7\7g\2\2\u00b7\u00da\5\22\n\23\u00b8\u00b9\f\21\2\2"+
		"\u00b9\u00ba\7v\2\2\u00ba\u00da\5\22\n\22\u00bb\u00bc\f\20\2\2\u00bc\u00bd"+
		"\7w\2\2\u00bd\u00da\5\22\n\21\u00be\u00bf\f\17\2\2\u00bf\u00c0\7t\2\2"+
		"\u00c0\u00da\5\22\n\20\u00c1\u00c2\f\16\2\2\u00c2\u00c3\7u\2\2\u00c3\u00da"+
		"\5\22\n\17\u00c4\u00c5\f\r\2\2\u00c5\u00c6\7b\2\2\u00c6\u00da\5\22\n\16"+
		"\u00c7\u00c8\f\f\2\2\u00c8\u00c9\7a\2\2\u00c9\u00da\5\22\n\r\u00ca\u00cb"+
		"\f\13\2\2\u00cb\u00cc\7`\2\2\u00cc\u00da\5\22\n\f\u00cd\u00ce\f\n\2\2"+
		"\u00ce\u00cf\7y\2\2\u00cf\u00da\5\22\n\13\u00d0\u00d1\f\t\2\2\u00d1\u00d2"+
		"\7x\2\2\u00d2\u00da\5\22\n\n\u00d3\u00d4\f\b\2\2\u00d4\u00d5\7p\2\2\u00d5"+
		"\u00da\5\22\n\t\u00d6\u00d7\f\7\2\2\u00d7\u00d8\7r\2\2\u00d8\u00da\5\22"+
		"\n\b\u00d9\u00a3\3\2\2\2\u00d9\u00a6\3\2\2\2\u00d9\u00a9\3\2\2\2\u00d9"+
		"\u00ac\3\2\2\2\u00d9\u00af\3\2\2\2\u00d9\u00b2\3\2\2\2\u00d9\u00b5\3\2"+
		"\2\2\u00d9\u00b8\3\2\2\2\u00d9\u00bb\3\2\2\2\u00d9\u00be\3\2\2\2\u00d9"+
		"\u00c1\3\2\2\2\u00d9\u00c4\3\2\2\2\u00d9\u00c7\3\2\2\2\u00d9\u00ca\3\2"+
		"\2\2\u00d9\u00cd\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9\u00d3\3\2\2\2\u00d9"+
		"\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2"+
		"\2\2\u00dc\23\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\7\u0086\2\2\u00df"+
		"\u00e8\7U\2\2\u00e0\u00e5\5\22\n\2\u00e1\u00e2\7|\2\2\u00e2\u00e4\5\22"+
		"\n\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5"+
		"\u00e6\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e0\3\2"+
		"\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\7V\2\2\u00eb"+
		"\25\3\2\2\2\u00ec\u00f9\5\32\16\2\u00ed\u00f9\5\30\r\2\u00ee\u00f9\5\34"+
		"\17\2\u00ef\u00f9\5\36\20\2\u00f0\u00f9\5\"\22\2\u00f1\u00f9\5$\23\2\u00f2"+
		"\u00f9\5&\24\2\u00f3\u00f9\5*\26\2\u00f4\u00f9\5,\27\2\u00f5\u00f9\5."+
		"\30\2\u00f6\u00f9\5\62\32\2\u00f7\u00f9\5> \2\u00f8\u00ec\3\2\2\2\u00f8"+
		"\u00ed\3\2\2\2\u00f8\u00ee\3\2\2\2\u00f8\u00ef\3\2\2\2\u00f8\u00f0\3\2"+
		"\2\2\u00f8\u00f1\3\2\2\2\u00f8\u00f2\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f8"+
		"\u00f4\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2"+
		"\2\2\u00f9\27\3\2\2\2\u00fa\u00fe\7Y\2\2\u00fb\u00fd\5\26\f\2\u00fc\u00fb"+
		"\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff"+
		"\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7Z\2\2\u0102\31\3\2\2\2"+
		"\u0103\u0105\5\22\n\2\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106"+
		"\3\2\2\2\u0106\u0107\7\u0082\2\2\u0107\33\3\2\2\2\u0108\u0109\7+\2\2\u0109"+
		"\u010a\7U\2\2\u010a\u010b\5\22\n\2\u010b\u010c\7V\2\2\u010c\u010f\5\26"+
		"\f\2\u010d\u010e\7 \2\2\u010e\u0110\5\26\f\2\u010f\u010d\3\2\2\2\u010f"+
		"\u0110\3\2\2\2\u0110\35\3\2\2\2\u0111\u0112\7C\2\2\u0112\u0113\7U\2\2"+
		"\u0113\u0114\5\22\n\2\u0114\u0115\7V\2\2\u0115\u0119\7Y\2\2\u0116\u0118"+
		"\5 \21\2\u0117\u0116\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119"+
		"\u011a\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\7Z"+
		"\2\2\u011d\37\3\2\2\2\u011e\u011f\7\20\2\2\u011f\u0120\5\16\b\2\u0120"+
		"\u0121\7\u0080\2\2\u0121\u0122\5\26\f\2\u0122!\3\2\2\2\u0123\u0124\7T"+
		"\2\2\u0124\u0125\7U\2\2\u0125\u0126\5\22\n\2\u0126\u0127\7V\2\2\u0127"+
		"\u0128\5\26\f\2\u0128#\3\2\2\2\u0129\u012a\7\35\2\2\u012a\u012b\5\26\f"+
		"\2\u012b\u012c\7T\2\2\u012c\u012d\7U\2\2\u012d\u012e\5\22\n\2\u012e\u012f"+
		"\7V\2\2\u012f\u0130\7\u0082\2\2\u0130%\3\2\2\2\u0131\u0132\7(\2\2\u0132"+
		"\u0134\7U\2\2\u0133\u0135\5(\25\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2"+
		"\2\2\u0135\u0136\3\2\2\2\u0136\u0138\7\u0082\2\2\u0137\u0139\5\22\n\2"+
		"\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c"+
		"\7\u0082\2\2\u013b\u013d\5(\25\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2"+
		"\2\u013d\u013e\3\2\2\2\u013e\u013f\7V\2\2\u013f\u0140\5\26\f\2\u0140\'"+
		"\3\2\2\2\u0141\u0146\5\22\n\2\u0142\u0143\7|\2\2\u0143\u0145\5\22\n\2"+
		"\u0144\u0142\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147"+
		"\3\2\2\2\u0147)\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b\7;\2\2\u014a\u014c"+
		"\5\22\n\2\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3\2\2\2"+
		"\u014d\u014e\7\u0082\2\2\u014e+\3\2\2\2\u014f\u0150\7\17\2\2\u0150\u0151"+
		"\7\u0082\2\2\u0151-\3\2\2\2\u0152\u0153\7\31\2\2\u0153\u0154\7\u0082\2"+
		"\2\u0154/\3\2\2\2\u0155\u0159\5\62\32\2\u0156\u0159\5> \2\u0157\u0159"+
		"\5H%\2\u0158\u0155\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159"+
		"\61\3\2\2\2\u015a\u015b\5T+\2\u015b\u015c\5\64\33\2\u015c\u015d\7\u0082"+
		"\2\2\u015d\63\3\2\2\2\u015e\u0163\5\66\34\2\u015f\u0160\7|\2\2\u0160\u0162"+
		"\5\66\34\2\u0161\u015f\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2"+
		"\u0163\u0164\3\2\2\2\u0164\65\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u016a"+
		"\58\35\2\u0167\u016a\5:\36\2\u0168\u016a\5<\37\2\u0169\u0166\3\2\2\2\u0169"+
		"\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016a\67\3\2\2\2\u016b\u016c\7\u0086"+
		"\2\2\u016c9\3\2\2\2\u016d\u016e\7\u0086\2\2\u016e\u016f\7e\2\2\u016f\u0170"+
		"\5\16\b\2\u0170;\3\2\2\2\u0171\u0172\7\u0086\2\2\u0172\u0173\7e\2\2\u0173"+
		"\u0174\5\22\n\2\u0174=\3\2\2\2\u0175\u0178\5@!\2\u0176\u0178\5D#\2\u0177"+
		"\u0175\3\2\2\2\u0177\u0176\3\2\2\2\u0178?\3\2\2\2\u0179\u017a\5X-\2\u017a"+
		"\u0180\5F$\2\u017b\u017c\7e\2\2\u017c\u017d\7Y\2\2\u017d\u017e\5B\"\2"+
		"\u017e\u017f\7Z\2\2\u017f\u0181\3\2\2\2\u0180\u017b\3\2\2\2\u0180\u0181"+
		"\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\7\u0082\2\2\u0183A\3\2\2\2\u0184"+
		"\u0189\5\22\n\2\u0185\u0186\7|\2\2\u0186\u0188\5\22\n\2\u0187\u0185\3"+
		"\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a"+
		"C\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\5`\61\2\u018d\u0190\5F$\2\u018e"+
		"\u018f\7e\2\2\u018f\u0191\5\f\7\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2"+
		"\2\2\u0191\u0192\3\2\2\2\u0192\u0193\7\u0082\2\2\u0193E\3\2\2\2\u0194"+
		"\u0195\7\u0086\2\2\u0195\u0196\7W\2\2\u0196\u0197\7\3\2\2\u0197\u0198"+
		"\7X\2\2\u0198G\3\2\2\2\u0199\u019c\5J&\2\u019a\u019c\5L\'\2\u019b\u0199"+
		"\3\2\2\2\u019b\u019a\3\2\2\2\u019cI\3\2\2\2\u019d\u019e\5N(\2\u019e\u019f"+
		"\7\u0082\2\2\u019fK\3\2\2\2\u01a0\u01a1\5N(\2\u01a1\u01a2\5\30\r\2\u01a2"+
		"M\3\2\2\2\u01a3\u01a4\5T+\2\u01a4\u01a5\7\u0086\2\2\u01a5\u01a7\7U\2\2"+
		"\u01a6\u01a8\5P)\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9"+
		"\3\2\2\2\u01a9\u01aa\7V\2\2\u01aaO\3\2\2\2\u01ab\u01b0\5R*\2\u01ac\u01ad"+
		"\7|\2\2\u01ad\u01af\5R*\2\u01ae\u01ac\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0"+
		"\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1Q\3\2\2\2\u01b2\u01b0\3\2\2\2"+
		"\u01b3\u01b4\5T+\2\u01b4\u01b5\7\u0086\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b8"+
		"\7\u0085\2\2\u01b7\u01b3\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8S\3\2\2\2\u01b9"+
		"\u01bc\5V,\2\u01ba\u01bc\5X-\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2"+
		"\u01bcU\3\2\2\2\u01bd\u01be\5X-\2\u01be\u01bf\7]\2\2\u01bfW\3\2\2\2\u01c0"+
		"\u01c6\5Z.\2\u01c1\u01c6\5\\/\2\u01c2\u01c6\5^\60\2\u01c3\u01c6\5`\61"+
		"\2\u01c4\u01c6\5b\62\2\u01c5\u01c0\3\2\2\2\u01c5\u01c1\3\2\2\2\u01c5\u01c2"+
		"\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6Y\3\2\2\2\u01c7"+
		"\u01cd\7-\2\2\u01c8\u01cd\7.\2\2\u01c9\u01cd\7<\2\2\u01ca\u01cb\7.\2\2"+
		"\u01cb\u01cd\7.\2\2\u01cc\u01c7\3\2\2\2\u01cc\u01c8\3\2\2\2\u01cc\u01c9"+
		"\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd[\3\2\2\2\u01ce\u01d3\7\'\2\2\u01cf"+
		"\u01d3\7\36\2\2\u01d0\u01d1\7.\2\2\u01d1\u01d3\7\36\2\2\u01d2\u01ce\3"+
		"\2\2\2\u01d2\u01cf\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3]\3\2\2\2\u01d4\u01d5"+
		"\7\16\2\2\u01d5_\3\2\2\2\u01d6\u01d7\7\22\2\2\u01d7a\3\2\2\2\u01d8\u01d9"+
		"\7Q\2\2\u01d9c\3\2\2\2#gp\u0082\u00a1\u00d9\u00db\u00e5\u00e8\u00f8\u00fe"+
		"\u0104\u010f\u0119\u0134\u0138\u013c\u0146\u014b\u0158\u0163\u0169\u0177"+
		"\u0180\u0189\u0190\u019b\u01a7\u01b0\u01b7\u01bb\u01c5\u01cc\u01d2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}