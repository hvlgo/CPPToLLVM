lexer grammar Cpp2llvmLexer;

// KEYWORD 
AND: '&&' | 'AND';

AND_EQ: '&=' | 'AND_EQ';

ASM: 'ASM';

AUTO: 'AUTO';

ALIGNAS: '_ALIGNAS';

ALIGNOF: '_ALIGNOF';

BITAND: '&' | 'BITAND';

BITOR: '|' | 'BITOR';

BOOL: 'BOOL';

BREAK: 'BREAK';

CASE: 'CASE';

CATCH: 'CATCH';

CHAR: 'CHAR';

CHAR16_T: 'CHAR16_T';

CHAR32_T: 'CHAR32_T';

CLASS: 'CLASS';

COMPL: '~' | 'COMPL';

CONST: 'CONST';

CONSTEXPR: 'CONSTEXPR';

CONST_CAST: 'CONST_CAST';

CONTINUE: 'CONTINUE';

DEFAULT: 'DEFAULT';

DELETE: 'DELETE';

DO: 'DO';

DOUBLE: 'DOUBLE';

DYNAMIC_CAST: 'DYNAMIC_CAST';

ELSE: 'ELSE';

ENUM: 'ENUM';

EXPLICIT: 'EXPLICIT';

EXPORT: 'EXPORT';

EXTERN: 'EXTERN';

FALSE_: 'FALSE';

FINAL: 'FINAL';

FLOAT: 'FLOAT';

FOR: 'FOR';

FRIEND: 'FRIEND';

GOTO: 'GOTO';

IF: 'IF';

INLINE: 'INLINE';

INT: 'INT';

LONG: 'LONG';

MUTABLE: 'MUTABLE';

NAMESPACE: 'NAMESPACE';

NEW: 'NEW';

NOT: '!' | 'NOT';

NOT_EQ: '!=' | 'NOT_EQ';

NULLPTR: 'NULLPTR';

OPERATOR: 'OPERATOR';

OR: '||' | 'OR';

OR_EQ: '|=' | 'OR_EQ';

OVERRIDE: 'OVERRIDE';

PRIVATE: 'PRIVATE';

PROTECTED: 'PROTECTED';

PUBLIC: 'PUBLIC';

REGISTER: 'REGISTER';

REINTERPRET_CAST: 'REINTERPRET_CAST';

RETURN: 'RETURN';

SHORT: 'SHORT';

SIGNED: 'SIGNED';

SIZEOF: 'SIZEOF';

STATIC: 'STATIC';

STATIC_ASSERT: 'STATIC_ASSERT';

STATIC_CAST: 'STATIC_CAST';

STRUCT: 'STRUCT';

SWITCH: 'SWITCH';

TEMPLATE: 'TEMPLATE';

THIS: 'THIS';

THREAD_LOCAL: 'THREAD_LOCAL';

THROW: 'THROW';

TRUE_: 'TRUE';

TRY: 'TRY';

TYPEDEF: 'TYPEDEF';

TYPEID: 'TYPEID';

TYPENAME: 'TYPENAME';

UNION: 'UNION';

UNSIGNED: 'UNSIGNED';

USING: 'USING';

VIRTUAL: 'VIRTUAL';

VOID: 'VOID';

VOLATILE: 'VOLATILE';

WCHAR_T: 'WCHAR_T';

WHILE: 'WHILE';

XOR: '^' | 'XOR';

XOR_EQ: '^=' | 'XOR_EQ';


// TOKENS
LEFTPAREN: '(';

RIGHTPAREN: ')';

LEFTBRACKET: '[';

RIGHTBRACKET: ']';

LEFTBRACE: '{';

RIGHTBRACE: '}';

QUESTION: '?';

COLON: ':';

SEMI: ';';

COMMA: ',';

ARROW: '->';

DOT: '.';

ELLIPSIS: '...';


// OPERATORS
LESS: '<';

LESSEQUAL: '<=';

GREATER: '>';

GREATEREQUAL: '>=';

LEFTSHIFT: '<<';

RIGHTSHIFT: '>>';

PLUS: '+';

PLUSPLUS: '++';

MINUS: '-';

MINUSMINUS: '--';

STAR: '*';

DIV: '/';

MOD: '%';

BITAND: '&';

BITOR: '|';

ANDAND: '&&';

OROR: '||';

CARET: '^';

TILDE: '~';

ASSIGN: '=';

STARASSIGN: '*=';

DIVASSIGN: '/=';

MODASSIGN: '%=';

PLUSASSIGN: '+=';

MINUSASSIGN: '-=';

LEFTSHIFTASSIGN: '<<=';

RIGHTSHIFTASSIGN: '>>=';

ANDASSIGN: '&=';

XORASSIGN: '^=';

ORASSIGN: '|=';

EQUAL: '==';

NOTEQUAL: '!=';


// identifier
Identifier: IdentifierNondigit (IdentifierNondigit | Digit)*;

fragment IdentifierNondigit: Nondigit | UniversalCharacterName;

fragment Nondigit: [a-zA-Z_];

fragment Digit: [0-9];

fragment UniversalCharacterName: '\\u' HexQuad | '\\U' HexQuad HexQuad;

fragment HexQuad: HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit;

Constant: IntegerConstant | FloatingConstant | CharacterConstant;

fragment IntegerConstant: DecimalConstant IntegerSuffix? | OctalConstant IntegerSuffix? 
                    | HexadecimalConstant IntegerSuffix? | BinaryConstant;

fragment BinaryConstant: '0' [bB] [0-1]+;

fragment DecimalConstant: NonzeroDigit Digit*;

fragment OctalConstant: '0' OctalDigit*;

fragment HexadecimalConstant: HexadecimalPrefix HexadecimalDigit+;

fragment HexadecimalPrefix: '0' [xX];

fragment NonzeroDigit: [1-9];

fragment OctalDigit: [0-7];

fragment HexadecimalDigit: [0-9a-fA-F];

fragment IntegerSuffix: UnsignedSuffix LongSuffix? | UnsignedSuffix LongLongSuffix 
                | LongSuffix UnsignedSuffix? | LongLongSuffix UnsignedSuffix?;