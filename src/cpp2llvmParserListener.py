# Generated from ./grammar/cpp2llvmParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp2llvmParser import cpp2llvmParser
else:
    from cpp2llvmParser import cpp2llvmParser

# This class defines a complete listener for a parse tree produced by cpp2llvmParser.
class cpp2llvmParserListener(ParseTreeListener):

    # Enter a parse tree produced by cpp2llvmParser#literal.
    def enterLiteral(self, ctx:cpp2llvmParser.LiteralContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#literal.
    def exitLiteral(self, ctx:cpp2llvmParser.LiteralContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#translationUnit.
    def enterTranslationUnit(self, ctx:cpp2llvmParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#translationUnit.
    def exitTranslationUnit(self, ctx:cpp2llvmParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#stringLiteral.
    def enterStringLiteral(self, ctx:cpp2llvmParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#stringLiteral.
    def exitStringLiteral(self, ctx:cpp2llvmParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#constExpression.
    def enterConstExpression(self, ctx:cpp2llvmParser.ConstExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#constExpression.
    def exitConstExpression(self, ctx:cpp2llvmParser.ConstExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#leftExpression.
    def enterLeftExpression(self, ctx:cpp2llvmParser.LeftExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#leftExpression.
    def exitLeftExpression(self, ctx:cpp2llvmParser.LeftExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#expression.
    def enterExpression(self, ctx:cpp2llvmParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#expression.
    def exitExpression(self, ctx:cpp2llvmParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionCall.
    def enterFunctionCall(self, ctx:cpp2llvmParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionCall.
    def exitFunctionCall(self, ctx:cpp2llvmParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#condition.
    def enterCondition(self, ctx:cpp2llvmParser.ConditionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#condition.
    def exitCondition(self, ctx:cpp2llvmParser.ConditionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#statement.
    def enterStatement(self, ctx:cpp2llvmParser.StatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#statement.
    def exitStatement(self, ctx:cpp2llvmParser.StatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#expressionStatement.
    def enterExpressionStatement(self, ctx:cpp2llvmParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#expressionStatement.
    def exitExpressionStatement(self, ctx:cpp2llvmParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#compoundStatement.
    def enterCompoundStatement(self, ctx:cpp2llvmParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#compoundStatement.
    def exitCompoundStatement(self, ctx:cpp2llvmParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#caseStatement.
    def enterCaseStatement(self, ctx:cpp2llvmParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#caseStatement.
    def exitCaseStatement(self, ctx:cpp2llvmParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#selectionStatement.
    def enterSelectionStatement(self, ctx:cpp2llvmParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#selectionStatement.
    def exitSelectionStatement(self, ctx:cpp2llvmParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#iterationStatement.
    def enterIterationStatement(self, ctx:cpp2llvmParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#iterationStatement.
    def exitIterationStatement(self, ctx:cpp2llvmParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#jumpStatement.
    def enterJumpStatement(self, ctx:cpp2llvmParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#jumpStatement.
    def exitJumpStatement(self, ctx:cpp2llvmParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declaration.
    def enterDeclaration(self, ctx:cpp2llvmParser.DeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declaration.
    def exitDeclaration(self, ctx:cpp2llvmParser.DeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:cpp2llvmParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:cpp2llvmParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:cpp2llvmParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:cpp2llvmParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:cpp2llvmParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:cpp2llvmParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#varDeclWithoutInit.
    def enterVarDeclWithoutInit(self, ctx:cpp2llvmParser.VarDeclWithoutInitContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#varDeclWithoutInit.
    def exitVarDeclWithoutInit(self, ctx:cpp2llvmParser.VarDeclWithoutInitContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#varDeclWithConstInit.
    def enterVarDeclWithConstInit(self, ctx:cpp2llvmParser.VarDeclWithConstInitContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#varDeclWithConstInit.
    def exitVarDeclWithConstInit(self, ctx:cpp2llvmParser.VarDeclWithConstInitContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#varDeclWithNormalInit.
    def enterVarDeclWithNormalInit(self, ctx:cpp2llvmParser.VarDeclWithNormalInitContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#varDeclWithNormalInit.
    def exitVarDeclWithNormalInit(self, ctx:cpp2llvmParser.VarDeclWithNormalInitContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#arrayDeclarator.
    def enterArrayDeclarator(self, ctx:cpp2llvmParser.ArrayDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#arrayDeclarator.
    def exitArrayDeclarator(self, ctx:cpp2llvmParser.ArrayDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#normalArrayDeclaration.
    def enterNormalArrayDeclaration(self, ctx:cpp2llvmParser.NormalArrayDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#normalArrayDeclaration.
    def exitNormalArrayDeclaration(self, ctx:cpp2llvmParser.NormalArrayDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#arrayAssginExpressionList.
    def enterArrayAssginExpressionList(self, ctx:cpp2llvmParser.ArrayAssginExpressionListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#arrayAssginExpressionList.
    def exitArrayAssginExpressionList(self, ctx:cpp2llvmParser.ArrayAssginExpressionListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#stringDeclaration.
    def enterStringDeclaration(self, ctx:cpp2llvmParser.StringDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#stringDeclaration.
    def exitStringDeclaration(self, ctx:cpp2llvmParser.StringDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#arrayName.
    def enterArrayName(self, ctx:cpp2llvmParser.ArrayNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#arrayName.
    def exitArrayName(self, ctx:cpp2llvmParser.ArrayNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionDeclarator.
    def enterFunctionDeclarator(self, ctx:cpp2llvmParser.FunctionDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionDeclarator.
    def exitFunctionDeclarator(self, ctx:cpp2llvmParser.FunctionDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:cpp2llvmParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:cpp2llvmParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:cpp2llvmParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:cpp2llvmParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionHead.
    def enterFunctionHead(self, ctx:cpp2llvmParser.FunctionHeadContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionHead.
    def exitFunctionHead(self, ctx:cpp2llvmParser.FunctionHeadContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionParameterList.
    def enterFunctionParameterList(self, ctx:cpp2llvmParser.FunctionParameterListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionParameterList.
    def exitFunctionParameterList(self, ctx:cpp2llvmParser.FunctionParameterListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionParameter.
    def enterFunctionParameter(self, ctx:cpp2llvmParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionParameter.
    def exitFunctionParameter(self, ctx:cpp2llvmParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeModifier.
    def enterTypeModifier(self, ctx:cpp2llvmParser.TypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeModifier.
    def exitTypeModifier(self, ctx:cpp2llvmParser.TypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pointerTypeModifier.
    def enterPointerTypeModifier(self, ctx:cpp2llvmParser.PointerTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pointerTypeModifier.
    def exitPointerTypeModifier(self, ctx:cpp2llvmParser.PointerTypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#normalTypeModifier.
    def enterNormalTypeModifier(self, ctx:cpp2llvmParser.NormalTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#normalTypeModifier.
    def exitNormalTypeModifier(self, ctx:cpp2llvmParser.NormalTypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#integerTypeModifier.
    def enterIntegerTypeModifier(self, ctx:cpp2llvmParser.IntegerTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#integerTypeModifier.
    def exitIntegerTypeModifier(self, ctx:cpp2llvmParser.IntegerTypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#realTypeModifier.
    def enterRealTypeModifier(self, ctx:cpp2llvmParser.RealTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#realTypeModifier.
    def exitRealTypeModifier(self, ctx:cpp2llvmParser.RealTypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#boolTypeModifier.
    def enterBoolTypeModifier(self, ctx:cpp2llvmParser.BoolTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#boolTypeModifier.
    def exitBoolTypeModifier(self, ctx:cpp2llvmParser.BoolTypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#charTypeModifier.
    def enterCharTypeModifier(self, ctx:cpp2llvmParser.CharTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#charTypeModifier.
    def exitCharTypeModifier(self, ctx:cpp2llvmParser.CharTypeModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#voidTypeModifier.
    def enterVoidTypeModifier(self, ctx:cpp2llvmParser.VoidTypeModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#voidTypeModifier.
    def exitVoidTypeModifier(self, ctx:cpp2llvmParser.VoidTypeModifierContext):
        pass



del cpp2llvmParser