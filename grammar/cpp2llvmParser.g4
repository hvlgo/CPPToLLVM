parser grammar cpp2llvmParser;
options {
	tokenVocab = cpp2llvmLexer;
}
/*Basic concepts*/

translationUnit: declaration* EOF;
/*Expressions*/

constExpression : literal;

leftExpression :
    Identifier
    | Identifier (LSQUARE expression RSQUARE) 
    ;


expression :
    functionCall 
    | literal 
    | Identifier
    | LPAREN expression RPAREN
    | NOT expression
    | SUB expression
    | BITAND leftExpression
    | expression MULT expression 
    | expression DIV expression 
    | expression MOD expression 
    | expression ADD expression 
    | expression SUB expression 
    | expression LT expression
    | expression GT expression
    | expression LEQ expression
    | expression GEQ expression
    | expression EQ expression
    | expression NOT_EQ expression
    | expression BITOR expression
    | expression BITAND expression
    | expression XOR expression
    | expression OR expression
    | expression AND expression
    | expression LSHIFT expression
    | expression RSHIFT expression
    | Identifier LSQUARE expression RSQUARE
    | leftExpression ASSIGN expression
    | leftExpression PLUS_PLUS
    | leftExpression MINUS_MINUS;


/*Preprocessing directives*/

/*Lexer*/

theOperator:
	New (LeftBracket RightBracket)?
	| Delete (LeftBracket RightBracket)?
	| Plus
	| Minus
	| Star
	| Div
	| Mod
	| Caret
	| And
	| Or
	| Tilde
	| Not
	| Assign
	| Greater
	| Less
	| GreaterEqual
	| PlusAssign
	| MinusAssign
	| StarAssign
	| ModAssign
	| XorAssign
	| AndAssign
	| OrAssign
	| Less Less
	| Greater Greater
	| RightShiftAssign
	| LeftShiftAssign
	| Equal
	| NotEqual
	| LessEqual
	| AndAnd
	| OrOr
	| PlusPlus
	| MinusMinus
	| Comma
	| ArrowStar
	| Arrow
	| LeftParen RightParen
	| LeftBracket RightBracket;

literal:
	IntegerLiteral
	| CharacterLiteral
	| FloatingLiteral
	| StringLiteral
	| BooleanLiteral
	| PointerLiteral;
	
