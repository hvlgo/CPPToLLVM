parser grammar cpp2llvmParser;
options {
	tokenVocab = cpp2llvmLexer;
}

translationUnit: declaration* EOF;

/*Lexer*/
literal:
	IntegerLiteral
	| CharacterLiteral
	| FloatingLiteral
	| StringLiteral
	| BooleanLiteral
	| PointerLiteral;

stringLiteral: StringLiteral;

/*Expressions*/
constExpression: literal;

leftExpression:
	Identifier
	| Identifier (LeftBracket expression RightBracket);

expression:
	functionCall
	| literal
	| Identifier
	| LeftParen expression RightParen
	| Not expression
	| Minus expression
	| And leftExpression
	| expression Star expression
	| expression Div expression
	| expression Mod expression
	| expression Plus expression
	| expression Minus expression
	| expression Less expression
	| expression Greater expression
	| expression LessEqual expression
	| expression GreaterEqual expression
	| expression Equal expression
	| expression NotEqual expression
	| expression Or expression
	| expression And expression
	| expression Caret expression
	| expression OrOr expression
	| expression AndAnd expression
	| expression LeftShift expression
	| expression RightShift expression
	| Identifier LeftBracket expression RightBracket
	| leftExpression Assign expression
	| leftExpression PlusPlus
	| leftExpression MinusMinus;

/* Statements */
functionCall:
	Identifier LeftParen (expression (Comma expression)*)? RightParen;

statement:
	expressionStatement
	| compoundStatement
	| ifStatement
	| switchStatement
	| whileStatement
	| doWhileStatement
	| forStatement
	| returnStatement
	| breakStatement
	| continueStatement
	| variableDeclarator
	| arrayDeclarator;

compoundStatement: LeftBrace statement* RightBrace;

expressionStatement: expression? Semi;

// selectionStatement:
// 	If LeftParen condition RightParen statement (Else statement)?
// 	| Switch LeftParen condition RightParen LeftBrace (
// 		caseStatement
// 	)* RightBrace;

ifStatement : If LeftParen expression RightParen statement (Else statement)?;

switchStatement : Switch LeftParen expression RightParen LeftBrace (caseStatement)* RightBrace;

caseStatement: Case constExpression Colon statement;

// iterationStatement:
// 	While LeftParen condition RightParen statement
// 	| Do statement While LeftParen expression RightParen Semi
// 	| For LeftParen (expression (Comma expression)*)? Semi expression? Semi (
// 		expression (Comma expression)*
// 	)? RightParen statement;

whileStatement : While LeftParen expression RightParen statement;

doWhileStatement : Do statement While LeftParen expression RightParen Semi;

forStatement : For LeftParen forExprSet? Semi expression? Semi forExprSet? RightParen statement;

forExprSet: expression (Comma expression)*;

// jumpStatement:
// 	(Break | Continue | Return expression? | Goto Identifier) Semi;

returnStatement : Return expression? Semi;

breakStatement : Break Semi;

continueStatement : Continue Semi;

/*Declarations*/
declaration:
	variableDeclarator
	| arrayDeclarator
	| functionDeclarator;

variableDeclarator: typeModifier variableDeclarationList Semi;

variableDeclarationList:
	variableDeclaration (Comma variableDeclaration)*;

variableDeclaration:
	varDeclWithoutInit
	| varDeclWithConstInit
	| varDeclWithNormalInit;

varDeclWithoutInit: Identifier;

varDeclWithConstInit: Identifier Assign constExpression;

varDeclWithNormalInit: Identifier Assign expression;

arrayDeclarator: normalArrayDeclaration | stringDeclaration;

normalArrayDeclaration:
	normalTypeModifier arrayName (
		Assign LeftBrace arrayAssginExpressionList RightBrace
	)? Semi;

arrayAssginExpressionList: expression (Comma expression)*;

stringDeclaration:
	charTypeModifier arrayName (Assign stringLiteral)? Semi;

arrayName: Identifier LeftBracket IntegerLiteral RightBracket;

functionDeclarator: functionDeclaration | functionDefinition;

functionDeclaration: functionHead Semi;

functionDefinition: functionHead compoundStatement;

functionHead:
	typeModifier Identifier LeftParen functionParameterList? RightParen;

functionParameterList:
	functionParameter (Comma functionParameter)*;

functionParameter:
	pointerTypeModifier Identifier
	| normalTypeModifier Identifier
	| Ellipsis;

typeModifier: pointerTypeModifier | normalTypeModifier;

pointerTypeModifier: normalTypeModifier Star;

normalTypeModifier:
	integerTypeModifier
	| realTypeModifier
	| boolTypeModifier
	| charTypeModifier
	| voidTypeModifier;

integerTypeModifier: Int | Long | Short | Long Long;

realTypeModifier: Float | Double | Long Double;

boolTypeModifier: Bool;

charTypeModifier: Char;

voidTypeModifier: Void;
