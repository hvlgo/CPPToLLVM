# Generated from ./grammar/cpp2llvmParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp2llvmParser import cpp2llvmParser
else:
    from cpp2llvmParser import cpp2llvmParser

# This class defines a complete generic visitor for a parse tree produced by cpp2llvmParser.

class cpp2llvmParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cpp2llvmParser#translationUnit.
    def visitTranslationUnit(self, ctx:cpp2llvmParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#literal.
    def visitLiteral(self, ctx:cpp2llvmParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#stringLiteral.
    def visitStringLiteral(self, ctx:cpp2llvmParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#constExpression.
    def visitConstExpression(self, ctx:cpp2llvmParser.ConstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#leftExpression.
    def visitLeftExpression(self, ctx:cpp2llvmParser.LeftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#expression.
    def visitExpression(self, ctx:cpp2llvmParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionCall.
    def visitFunctionCall(self, ctx:cpp2llvmParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#statement.
    def visitStatement(self, ctx:cpp2llvmParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#compoundStatement.
    def visitCompoundStatement(self, ctx:cpp2llvmParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#ifStatement.
    def visitIfStatement(self, ctx:cpp2llvmParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#switchStatement.
    def visitSwitchStatement(self, ctx:cpp2llvmParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#caseStatement.
    def visitCaseStatement(self, ctx:cpp2llvmParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#whileStatement.
    def visitWhileStatement(self, ctx:cpp2llvmParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:cpp2llvmParser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#forStatement.
    def visitForStatement(self, ctx:cpp2llvmParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#forExprSet.
    def visitForExprSet(self, ctx:cpp2llvmParser.ForExprSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#returnStatement.
    def visitReturnStatement(self, ctx:cpp2llvmParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#breakStatement.
    def visitBreakStatement(self, ctx:cpp2llvmParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#continueStatement.
    def visitContinueStatement(self, ctx:cpp2llvmParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#declaration.
    def visitDeclaration(self, ctx:cpp2llvmParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:cpp2llvmParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:cpp2llvmParser.VariableDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:cpp2llvmParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#varDeclWithoutInit.
    def visitVarDeclWithoutInit(self, ctx:cpp2llvmParser.VarDeclWithoutInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#varDeclWithConstInit.
    def visitVarDeclWithConstInit(self, ctx:cpp2llvmParser.VarDeclWithConstInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#varDeclWithNormalInit.
    def visitVarDeclWithNormalInit(self, ctx:cpp2llvmParser.VarDeclWithNormalInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#arrayDeclarator.
    def visitArrayDeclarator(self, ctx:cpp2llvmParser.ArrayDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#normalArrayDeclaration.
    def visitNormalArrayDeclaration(self, ctx:cpp2llvmParser.NormalArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#arrayAssginExpressionList.
    def visitArrayAssginExpressionList(self, ctx:cpp2llvmParser.ArrayAssginExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#stringDeclaration.
    def visitStringDeclaration(self, ctx:cpp2llvmParser.StringDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#arrayName.
    def visitArrayName(self, ctx:cpp2llvmParser.ArrayNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionDeclarator.
    def visitFunctionDeclarator(self, ctx:cpp2llvmParser.FunctionDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:cpp2llvmParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:cpp2llvmParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionHead.
    def visitFunctionHead(self, ctx:cpp2llvmParser.FunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionParameterList.
    def visitFunctionParameterList(self, ctx:cpp2llvmParser.FunctionParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#functionParameter.
    def visitFunctionParameter(self, ctx:cpp2llvmParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#typeModifier.
    def visitTypeModifier(self, ctx:cpp2llvmParser.TypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#pointerTypeModifier.
    def visitPointerTypeModifier(self, ctx:cpp2llvmParser.PointerTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#normalTypeModifier.
    def visitNormalTypeModifier(self, ctx:cpp2llvmParser.NormalTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#integerTypeModifier.
    def visitIntegerTypeModifier(self, ctx:cpp2llvmParser.IntegerTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#realTypeModifier.
    def visitRealTypeModifier(self, ctx:cpp2llvmParser.RealTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#boolTypeModifier.
    def visitBoolTypeModifier(self, ctx:cpp2llvmParser.BoolTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#charTypeModifier.
    def visitCharTypeModifier(self, ctx:cpp2llvmParser.CharTypeModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp2llvmParser#voidTypeModifier.
    def visitVoidTypeModifier(self, ctx:cpp2llvmParser.VoidTypeModifierContext):
        return self.visitChildren(ctx)



del cpp2llvmParser