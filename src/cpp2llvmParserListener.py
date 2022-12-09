# Generated from ./grammar/cpp2llvmParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp2llvmParser import cpp2llvmParser
else:
    from cpp2llvmParser import cpp2llvmParser

# This class defines a complete listener for a parse tree produced by cpp2llvmParser.
class cpp2llvmParserListener(ParseTreeListener):

    # Enter a parse tree produced by cpp2llvmParser#translationUnit.
    def enterTranslationUnit(self, ctx:cpp2llvmParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#translationUnit.
    def exitTranslationUnit(self, ctx:cpp2llvmParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:cpp2llvmParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:cpp2llvmParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#idExpression.
    def enterIdExpression(self, ctx:cpp2llvmParser.IdExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#idExpression.
    def exitIdExpression(self, ctx:cpp2llvmParser.IdExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#unqualifiedId.
    def enterUnqualifiedId(self, ctx:cpp2llvmParser.UnqualifiedIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#unqualifiedId.
    def exitUnqualifiedId(self, ctx:cpp2llvmParser.UnqualifiedIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#qualifiedId.
    def enterQualifiedId(self, ctx:cpp2llvmParser.QualifiedIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#qualifiedId.
    def exitQualifiedId(self, ctx:cpp2llvmParser.QualifiedIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#nestedNameSpecifier.
    def enterNestedNameSpecifier(self, ctx:cpp2llvmParser.NestedNameSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#nestedNameSpecifier.
    def exitNestedNameSpecifier(self, ctx:cpp2llvmParser.NestedNameSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:cpp2llvmParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:cpp2llvmParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#lambdaIntroducer.
    def enterLambdaIntroducer(self, ctx:cpp2llvmParser.LambdaIntroducerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#lambdaIntroducer.
    def exitLambdaIntroducer(self, ctx:cpp2llvmParser.LambdaIntroducerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#lambdaCapture.
    def enterLambdaCapture(self, ctx:cpp2llvmParser.LambdaCaptureContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#lambdaCapture.
    def exitLambdaCapture(self, ctx:cpp2llvmParser.LambdaCaptureContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#captureDefault.
    def enterCaptureDefault(self, ctx:cpp2llvmParser.CaptureDefaultContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#captureDefault.
    def exitCaptureDefault(self, ctx:cpp2llvmParser.CaptureDefaultContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#captureList.
    def enterCaptureList(self, ctx:cpp2llvmParser.CaptureListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#captureList.
    def exitCaptureList(self, ctx:cpp2llvmParser.CaptureListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#capture.
    def enterCapture(self, ctx:cpp2llvmParser.CaptureContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#capture.
    def exitCapture(self, ctx:cpp2llvmParser.CaptureContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#simpleCapture.
    def enterSimpleCapture(self, ctx:cpp2llvmParser.SimpleCaptureContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#simpleCapture.
    def exitSimpleCapture(self, ctx:cpp2llvmParser.SimpleCaptureContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#initcapture.
    def enterInitcapture(self, ctx:cpp2llvmParser.InitcaptureContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#initcapture.
    def exitInitcapture(self, ctx:cpp2llvmParser.InitcaptureContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#lambdaDeclarator.
    def enterLambdaDeclarator(self, ctx:cpp2llvmParser.LambdaDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#lambdaDeclarator.
    def exitLambdaDeclarator(self, ctx:cpp2llvmParser.LambdaDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#postfixExpression.
    def enterPostfixExpression(self, ctx:cpp2llvmParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#postfixExpression.
    def exitPostfixExpression(self, ctx:cpp2llvmParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeIdOfTheTypeId.
    def enterTypeIdOfTheTypeId(self, ctx:cpp2llvmParser.TypeIdOfTheTypeIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeIdOfTheTypeId.
    def exitTypeIdOfTheTypeId(self, ctx:cpp2llvmParser.TypeIdOfTheTypeIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#expressionList.
    def enterExpressionList(self, ctx:cpp2llvmParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#expressionList.
    def exitExpressionList(self, ctx:cpp2llvmParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pseudoDestructorName.
    def enterPseudoDestructorName(self, ctx:cpp2llvmParser.PseudoDestructorNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pseudoDestructorName.
    def exitPseudoDestructorName(self, ctx:cpp2llvmParser.PseudoDestructorNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#unaryExpression.
    def enterUnaryExpression(self, ctx:cpp2llvmParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#unaryExpression.
    def exitUnaryExpression(self, ctx:cpp2llvmParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#unaryOperator.
    def enterUnaryOperator(self, ctx:cpp2llvmParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#unaryOperator.
    def exitUnaryOperator(self, ctx:cpp2llvmParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#newExpression.
    def enterNewExpression(self, ctx:cpp2llvmParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#newExpression.
    def exitNewExpression(self, ctx:cpp2llvmParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#newPlacement.
    def enterNewPlacement(self, ctx:cpp2llvmParser.NewPlacementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#newPlacement.
    def exitNewPlacement(self, ctx:cpp2llvmParser.NewPlacementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#newTypeId.
    def enterNewTypeId(self, ctx:cpp2llvmParser.NewTypeIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#newTypeId.
    def exitNewTypeId(self, ctx:cpp2llvmParser.NewTypeIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#newDeclarator.
    def enterNewDeclarator(self, ctx:cpp2llvmParser.NewDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#newDeclarator.
    def exitNewDeclarator(self, ctx:cpp2llvmParser.NewDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#noPointerNewDeclarator.
    def enterNoPointerNewDeclarator(self, ctx:cpp2llvmParser.NoPointerNewDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#noPointerNewDeclarator.
    def exitNoPointerNewDeclarator(self, ctx:cpp2llvmParser.NoPointerNewDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#newInitializer.
    def enterNewInitializer(self, ctx:cpp2llvmParser.NewInitializerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#newInitializer.
    def exitNewInitializer(self, ctx:cpp2llvmParser.NewInitializerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#deleteExpression.
    def enterDeleteExpression(self, ctx:cpp2llvmParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#deleteExpression.
    def exitDeleteExpression(self, ctx:cpp2llvmParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#noExceptExpression.
    def enterNoExceptExpression(self, ctx:cpp2llvmParser.NoExceptExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#noExceptExpression.
    def exitNoExceptExpression(self, ctx:cpp2llvmParser.NoExceptExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#castExpression.
    def enterCastExpression(self, ctx:cpp2llvmParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#castExpression.
    def exitCastExpression(self, ctx:cpp2llvmParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pointerMemberExpression.
    def enterPointerMemberExpression(self, ctx:cpp2llvmParser.PointerMemberExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pointerMemberExpression.
    def exitPointerMemberExpression(self, ctx:cpp2llvmParser.PointerMemberExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:cpp2llvmParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:cpp2llvmParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:cpp2llvmParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:cpp2llvmParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#shiftExpression.
    def enterShiftExpression(self, ctx:cpp2llvmParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#shiftExpression.
    def exitShiftExpression(self, ctx:cpp2llvmParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#shiftOperator.
    def enterShiftOperator(self, ctx:cpp2llvmParser.ShiftOperatorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#shiftOperator.
    def exitShiftOperator(self, ctx:cpp2llvmParser.ShiftOperatorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#relationalExpression.
    def enterRelationalExpression(self, ctx:cpp2llvmParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#relationalExpression.
    def exitRelationalExpression(self, ctx:cpp2llvmParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#equalityExpression.
    def enterEqualityExpression(self, ctx:cpp2llvmParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#equalityExpression.
    def exitEqualityExpression(self, ctx:cpp2llvmParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#andExpression.
    def enterAndExpression(self, ctx:cpp2llvmParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#andExpression.
    def exitAndExpression(self, ctx:cpp2llvmParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:cpp2llvmParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:cpp2llvmParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:cpp2llvmParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:cpp2llvmParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:cpp2llvmParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:cpp2llvmParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:cpp2llvmParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:cpp2llvmParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:cpp2llvmParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:cpp2llvmParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:cpp2llvmParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:cpp2llvmParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:cpp2llvmParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:cpp2llvmParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#expression.
    def enterExpression(self, ctx:cpp2llvmParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#expression.
    def exitExpression(self, ctx:cpp2llvmParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#constantExpression.
    def enterConstantExpression(self, ctx:cpp2llvmParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#constantExpression.
    def exitConstantExpression(self, ctx:cpp2llvmParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#statement.
    def enterStatement(self, ctx:cpp2llvmParser.StatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#statement.
    def exitStatement(self, ctx:cpp2llvmParser.StatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#labeledStatement.
    def enterLabeledStatement(self, ctx:cpp2llvmParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#labeledStatement.
    def exitLabeledStatement(self, ctx:cpp2llvmParser.LabeledStatementContext):
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


    # Enter a parse tree produced by cpp2llvmParser#statementSeq.
    def enterStatementSeq(self, ctx:cpp2llvmParser.StatementSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#statementSeq.
    def exitStatementSeq(self, ctx:cpp2llvmParser.StatementSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#selectionStatement.
    def enterSelectionStatement(self, ctx:cpp2llvmParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#selectionStatement.
    def exitSelectionStatement(self, ctx:cpp2llvmParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#condition.
    def enterCondition(self, ctx:cpp2llvmParser.ConditionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#condition.
    def exitCondition(self, ctx:cpp2llvmParser.ConditionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#iterationStatement.
    def enterIterationStatement(self, ctx:cpp2llvmParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#iterationStatement.
    def exitIterationStatement(self, ctx:cpp2llvmParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#forInitStatement.
    def enterForInitStatement(self, ctx:cpp2llvmParser.ForInitStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#forInitStatement.
    def exitForInitStatement(self, ctx:cpp2llvmParser.ForInitStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#forRangeDeclaration.
    def enterForRangeDeclaration(self, ctx:cpp2llvmParser.ForRangeDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#forRangeDeclaration.
    def exitForRangeDeclaration(self, ctx:cpp2llvmParser.ForRangeDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#forRangeInitializer.
    def enterForRangeInitializer(self, ctx:cpp2llvmParser.ForRangeInitializerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#forRangeInitializer.
    def exitForRangeInitializer(self, ctx:cpp2llvmParser.ForRangeInitializerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#jumpStatement.
    def enterJumpStatement(self, ctx:cpp2llvmParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#jumpStatement.
    def exitJumpStatement(self, ctx:cpp2llvmParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:cpp2llvmParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:cpp2llvmParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declarationseq.
    def enterDeclarationseq(self, ctx:cpp2llvmParser.DeclarationseqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declarationseq.
    def exitDeclarationseq(self, ctx:cpp2llvmParser.DeclarationseqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declaration.
    def enterDeclaration(self, ctx:cpp2llvmParser.DeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declaration.
    def exitDeclaration(self, ctx:cpp2llvmParser.DeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#blockDeclaration.
    def enterBlockDeclaration(self, ctx:cpp2llvmParser.BlockDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#blockDeclaration.
    def exitBlockDeclaration(self, ctx:cpp2llvmParser.BlockDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#aliasDeclaration.
    def enterAliasDeclaration(self, ctx:cpp2llvmParser.AliasDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#aliasDeclaration.
    def exitAliasDeclaration(self, ctx:cpp2llvmParser.AliasDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#simpleDeclaration.
    def enterSimpleDeclaration(self, ctx:cpp2llvmParser.SimpleDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#simpleDeclaration.
    def exitSimpleDeclaration(self, ctx:cpp2llvmParser.SimpleDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:cpp2llvmParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:cpp2llvmParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#emptyDeclaration.
    def enterEmptyDeclaration(self, ctx:cpp2llvmParser.EmptyDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#emptyDeclaration.
    def exitEmptyDeclaration(self, ctx:cpp2llvmParser.EmptyDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:cpp2llvmParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:cpp2llvmParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declSpecifier.
    def enterDeclSpecifier(self, ctx:cpp2llvmParser.DeclSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declSpecifier.
    def exitDeclSpecifier(self, ctx:cpp2llvmParser.DeclSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declSpecifierSeq.
    def enterDeclSpecifierSeq(self, ctx:cpp2llvmParser.DeclSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declSpecifierSeq.
    def exitDeclSpecifierSeq(self, ctx:cpp2llvmParser.DeclSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:cpp2llvmParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:cpp2llvmParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:cpp2llvmParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:cpp2llvmParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typedefName.
    def enterTypedefName(self, ctx:cpp2llvmParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typedefName.
    def exitTypedefName(self, ctx:cpp2llvmParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cpp2llvmParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cpp2llvmParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#trailingTypeSpecifier.
    def enterTrailingTypeSpecifier(self, ctx:cpp2llvmParser.TrailingTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#trailingTypeSpecifier.
    def exitTrailingTypeSpecifier(self, ctx:cpp2llvmParser.TrailingTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeSpecifierSeq.
    def enterTypeSpecifierSeq(self, ctx:cpp2llvmParser.TypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeSpecifierSeq.
    def exitTypeSpecifierSeq(self, ctx:cpp2llvmParser.TypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#trailingTypeSpecifierSeq.
    def enterTrailingTypeSpecifierSeq(self, ctx:cpp2llvmParser.TrailingTypeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#trailingTypeSpecifierSeq.
    def exitTrailingTypeSpecifierSeq(self, ctx:cpp2llvmParser.TrailingTypeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#simpleTypeLengthModifier.
    def enterSimpleTypeLengthModifier(self, ctx:cpp2llvmParser.SimpleTypeLengthModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#simpleTypeLengthModifier.
    def exitSimpleTypeLengthModifier(self, ctx:cpp2llvmParser.SimpleTypeLengthModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#simpleTypeSignednessModifier.
    def enterSimpleTypeSignednessModifier(self, ctx:cpp2llvmParser.SimpleTypeSignednessModifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#simpleTypeSignednessModifier.
    def exitSimpleTypeSignednessModifier(self, ctx:cpp2llvmParser.SimpleTypeSignednessModifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#simpleTypeSpecifier.
    def enterSimpleTypeSpecifier(self, ctx:cpp2llvmParser.SimpleTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#simpleTypeSpecifier.
    def exitSimpleTypeSpecifier(self, ctx:cpp2llvmParser.SimpleTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#theTypeName.
    def enterTheTypeName(self, ctx:cpp2llvmParser.TheTypeNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#theTypeName.
    def exitTheTypeName(self, ctx:cpp2llvmParser.TheTypeNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#decltypeSpecifier.
    def enterDecltypeSpecifier(self, ctx:cpp2llvmParser.DecltypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#decltypeSpecifier.
    def exitDecltypeSpecifier(self, ctx:cpp2llvmParser.DecltypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#elaboratedTypeSpecifier.
    def enterElaboratedTypeSpecifier(self, ctx:cpp2llvmParser.ElaboratedTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#elaboratedTypeSpecifier.
    def exitElaboratedTypeSpecifier(self, ctx:cpp2llvmParser.ElaboratedTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumName.
    def enterEnumName(self, ctx:cpp2llvmParser.EnumNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumName.
    def exitEnumName(self, ctx:cpp2llvmParser.EnumNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:cpp2llvmParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:cpp2llvmParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumHead.
    def enterEnumHead(self, ctx:cpp2llvmParser.EnumHeadContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumHead.
    def exitEnumHead(self, ctx:cpp2llvmParser.EnumHeadContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#opaqueEnumDeclaration.
    def enterOpaqueEnumDeclaration(self, ctx:cpp2llvmParser.OpaqueEnumDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#opaqueEnumDeclaration.
    def exitOpaqueEnumDeclaration(self, ctx:cpp2llvmParser.OpaqueEnumDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumkey.
    def enterEnumkey(self, ctx:cpp2llvmParser.EnumkeyContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumkey.
    def exitEnumkey(self, ctx:cpp2llvmParser.EnumkeyContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumbase.
    def enterEnumbase(self, ctx:cpp2llvmParser.EnumbaseContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumbase.
    def exitEnumbase(self, ctx:cpp2llvmParser.EnumbaseContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumeratorList.
    def enterEnumeratorList(self, ctx:cpp2llvmParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumeratorList.
    def exitEnumeratorList(self, ctx:cpp2llvmParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumeratorDefinition.
    def enterEnumeratorDefinition(self, ctx:cpp2llvmParser.EnumeratorDefinitionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumeratorDefinition.
    def exitEnumeratorDefinition(self, ctx:cpp2llvmParser.EnumeratorDefinitionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#enumerator.
    def enterEnumerator(self, ctx:cpp2llvmParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#enumerator.
    def exitEnumerator(self, ctx:cpp2llvmParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#namespaceName.
    def enterNamespaceName(self, ctx:cpp2llvmParser.NamespaceNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#namespaceName.
    def exitNamespaceName(self, ctx:cpp2llvmParser.NamespaceNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#originalNamespaceName.
    def enterOriginalNamespaceName(self, ctx:cpp2llvmParser.OriginalNamespaceNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#originalNamespaceName.
    def exitOriginalNamespaceName(self, ctx:cpp2llvmParser.OriginalNamespaceNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#namespaceDefinition.
    def enterNamespaceDefinition(self, ctx:cpp2llvmParser.NamespaceDefinitionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#namespaceDefinition.
    def exitNamespaceDefinition(self, ctx:cpp2llvmParser.NamespaceDefinitionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#namespaceAlias.
    def enterNamespaceAlias(self, ctx:cpp2llvmParser.NamespaceAliasContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#namespaceAlias.
    def exitNamespaceAlias(self, ctx:cpp2llvmParser.NamespaceAliasContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#namespaceAliasDefinition.
    def enterNamespaceAliasDefinition(self, ctx:cpp2llvmParser.NamespaceAliasDefinitionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#namespaceAliasDefinition.
    def exitNamespaceAliasDefinition(self, ctx:cpp2llvmParser.NamespaceAliasDefinitionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#qualifiednamespacespecifier.
    def enterQualifiednamespacespecifier(self, ctx:cpp2llvmParser.QualifiednamespacespecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#qualifiednamespacespecifier.
    def exitQualifiednamespacespecifier(self, ctx:cpp2llvmParser.QualifiednamespacespecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#usingDeclaration.
    def enterUsingDeclaration(self, ctx:cpp2llvmParser.UsingDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#usingDeclaration.
    def exitUsingDeclaration(self, ctx:cpp2llvmParser.UsingDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#usingDirective.
    def enterUsingDirective(self, ctx:cpp2llvmParser.UsingDirectiveContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#usingDirective.
    def exitUsingDirective(self, ctx:cpp2llvmParser.UsingDirectiveContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#asmDefinition.
    def enterAsmDefinition(self, ctx:cpp2llvmParser.AsmDefinitionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#asmDefinition.
    def exitAsmDefinition(self, ctx:cpp2llvmParser.AsmDefinitionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#linkageSpecification.
    def enterLinkageSpecification(self, ctx:cpp2llvmParser.LinkageSpecificationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#linkageSpecification.
    def exitLinkageSpecification(self, ctx:cpp2llvmParser.LinkageSpecificationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attributeSpecifierSeq.
    def enterAttributeSpecifierSeq(self, ctx:cpp2llvmParser.AttributeSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attributeSpecifierSeq.
    def exitAttributeSpecifierSeq(self, ctx:cpp2llvmParser.AttributeSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attributeSpecifier.
    def enterAttributeSpecifier(self, ctx:cpp2llvmParser.AttributeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attributeSpecifier.
    def exitAttributeSpecifier(self, ctx:cpp2llvmParser.AttributeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#alignmentspecifier.
    def enterAlignmentspecifier(self, ctx:cpp2llvmParser.AlignmentspecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#alignmentspecifier.
    def exitAlignmentspecifier(self, ctx:cpp2llvmParser.AlignmentspecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attributeList.
    def enterAttributeList(self, ctx:cpp2llvmParser.AttributeListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attributeList.
    def exitAttributeList(self, ctx:cpp2llvmParser.AttributeListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attribute.
    def enterAttribute(self, ctx:cpp2llvmParser.AttributeContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attribute.
    def exitAttribute(self, ctx:cpp2llvmParser.AttributeContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attributeNamespace.
    def enterAttributeNamespace(self, ctx:cpp2llvmParser.AttributeNamespaceContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attributeNamespace.
    def exitAttributeNamespace(self, ctx:cpp2llvmParser.AttributeNamespaceContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#attributeArgumentClause.
    def enterAttributeArgumentClause(self, ctx:cpp2llvmParser.AttributeArgumentClauseContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#attributeArgumentClause.
    def exitAttributeArgumentClause(self, ctx:cpp2llvmParser.AttributeArgumentClauseContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#balancedTokenSeq.
    def enterBalancedTokenSeq(self, ctx:cpp2llvmParser.BalancedTokenSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#balancedTokenSeq.
    def exitBalancedTokenSeq(self, ctx:cpp2llvmParser.BalancedTokenSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#balancedtoken.
    def enterBalancedtoken(self, ctx:cpp2llvmParser.BalancedtokenContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#balancedtoken.
    def exitBalancedtoken(self, ctx:cpp2llvmParser.BalancedtokenContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:cpp2llvmParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:cpp2llvmParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#initDeclarator.
    def enterInitDeclarator(self, ctx:cpp2llvmParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#initDeclarator.
    def exitInitDeclarator(self, ctx:cpp2llvmParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declarator.
    def enterDeclarator(self, ctx:cpp2llvmParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declarator.
    def exitDeclarator(self, ctx:cpp2llvmParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pointerDeclarator.
    def enterPointerDeclarator(self, ctx:cpp2llvmParser.PointerDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pointerDeclarator.
    def exitPointerDeclarator(self, ctx:cpp2llvmParser.PointerDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#noPointerDeclarator.
    def enterNoPointerDeclarator(self, ctx:cpp2llvmParser.NoPointerDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#noPointerDeclarator.
    def exitNoPointerDeclarator(self, ctx:cpp2llvmParser.NoPointerDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#parametersAndQualifiers.
    def enterParametersAndQualifiers(self, ctx:cpp2llvmParser.ParametersAndQualifiersContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#parametersAndQualifiers.
    def exitParametersAndQualifiers(self, ctx:cpp2llvmParser.ParametersAndQualifiersContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#trailingReturnType.
    def enterTrailingReturnType(self, ctx:cpp2llvmParser.TrailingReturnTypeContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#trailingReturnType.
    def exitTrailingReturnType(self, ctx:cpp2llvmParser.TrailingReturnTypeContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pointerOperator.
    def enterPointerOperator(self, ctx:cpp2llvmParser.PointerOperatorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pointerOperator.
    def exitPointerOperator(self, ctx:cpp2llvmParser.PointerOperatorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#cvqualifierseq.
    def enterCvqualifierseq(self, ctx:cpp2llvmParser.CvqualifierseqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#cvqualifierseq.
    def exitCvqualifierseq(self, ctx:cpp2llvmParser.CvqualifierseqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#cvQualifier.
    def enterCvQualifier(self, ctx:cpp2llvmParser.CvQualifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#cvQualifier.
    def exitCvQualifier(self, ctx:cpp2llvmParser.CvQualifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#refqualifier.
    def enterRefqualifier(self, ctx:cpp2llvmParser.RefqualifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#refqualifier.
    def exitRefqualifier(self, ctx:cpp2llvmParser.RefqualifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#declaratorid.
    def enterDeclaratorid(self, ctx:cpp2llvmParser.DeclaratoridContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#declaratorid.
    def exitDeclaratorid(self, ctx:cpp2llvmParser.DeclaratoridContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#theTypeId.
    def enterTheTypeId(self, ctx:cpp2llvmParser.TheTypeIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#theTypeId.
    def exitTheTypeId(self, ctx:cpp2llvmParser.TheTypeIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:cpp2llvmParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:cpp2llvmParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pointerAbstractDeclarator.
    def enterPointerAbstractDeclarator(self, ctx:cpp2llvmParser.PointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pointerAbstractDeclarator.
    def exitPointerAbstractDeclarator(self, ctx:cpp2llvmParser.PointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#noPointerAbstractDeclarator.
    def enterNoPointerAbstractDeclarator(self, ctx:cpp2llvmParser.NoPointerAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#noPointerAbstractDeclarator.
    def exitNoPointerAbstractDeclarator(self, ctx:cpp2llvmParser.NoPointerAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#abstractPackDeclarator.
    def enterAbstractPackDeclarator(self, ctx:cpp2llvmParser.AbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#abstractPackDeclarator.
    def exitAbstractPackDeclarator(self, ctx:cpp2llvmParser.AbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#noPointerAbstractPackDeclarator.
    def enterNoPointerAbstractPackDeclarator(self, ctx:cpp2llvmParser.NoPointerAbstractPackDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#noPointerAbstractPackDeclarator.
    def exitNoPointerAbstractPackDeclarator(self, ctx:cpp2llvmParser.NoPointerAbstractPackDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#parameterDeclarationClause.
    def enterParameterDeclarationClause(self, ctx:cpp2llvmParser.ParameterDeclarationClauseContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#parameterDeclarationClause.
    def exitParameterDeclarationClause(self, ctx:cpp2llvmParser.ParameterDeclarationClauseContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#parameterDeclarationList.
    def enterParameterDeclarationList(self, ctx:cpp2llvmParser.ParameterDeclarationListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#parameterDeclarationList.
    def exitParameterDeclarationList(self, ctx:cpp2llvmParser.ParameterDeclarationListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:cpp2llvmParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:cpp2llvmParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:cpp2llvmParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:cpp2llvmParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionBody.
    def enterFunctionBody(self, ctx:cpp2llvmParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionBody.
    def exitFunctionBody(self, ctx:cpp2llvmParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#initializer.
    def enterInitializer(self, ctx:cpp2llvmParser.InitializerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#initializer.
    def exitInitializer(self, ctx:cpp2llvmParser.InitializerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#braceOrEqualInitializer.
    def enterBraceOrEqualInitializer(self, ctx:cpp2llvmParser.BraceOrEqualInitializerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#braceOrEqualInitializer.
    def exitBraceOrEqualInitializer(self, ctx:cpp2llvmParser.BraceOrEqualInitializerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#initializerClause.
    def enterInitializerClause(self, ctx:cpp2llvmParser.InitializerClauseContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#initializerClause.
    def exitInitializerClause(self, ctx:cpp2llvmParser.InitializerClauseContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#initializerList.
    def enterInitializerList(self, ctx:cpp2llvmParser.InitializerListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#initializerList.
    def exitInitializerList(self, ctx:cpp2llvmParser.InitializerListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#bracedInitList.
    def enterBracedInitList(self, ctx:cpp2llvmParser.BracedInitListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#bracedInitList.
    def exitBracedInitList(self, ctx:cpp2llvmParser.BracedInitListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#className.
    def enterClassName(self, ctx:cpp2llvmParser.ClassNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#className.
    def exitClassName(self, ctx:cpp2llvmParser.ClassNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#classSpecifier.
    def enterClassSpecifier(self, ctx:cpp2llvmParser.ClassSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#classSpecifier.
    def exitClassSpecifier(self, ctx:cpp2llvmParser.ClassSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#classHead.
    def enterClassHead(self, ctx:cpp2llvmParser.ClassHeadContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#classHead.
    def exitClassHead(self, ctx:cpp2llvmParser.ClassHeadContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#classHeadName.
    def enterClassHeadName(self, ctx:cpp2llvmParser.ClassHeadNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#classHeadName.
    def exitClassHeadName(self, ctx:cpp2llvmParser.ClassHeadNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#classVirtSpecifier.
    def enterClassVirtSpecifier(self, ctx:cpp2llvmParser.ClassVirtSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#classVirtSpecifier.
    def exitClassVirtSpecifier(self, ctx:cpp2llvmParser.ClassVirtSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#classKey.
    def enterClassKey(self, ctx:cpp2llvmParser.ClassKeyContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#classKey.
    def exitClassKey(self, ctx:cpp2llvmParser.ClassKeyContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#memberSpecification.
    def enterMemberSpecification(self, ctx:cpp2llvmParser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#memberSpecification.
    def exitMemberSpecification(self, ctx:cpp2llvmParser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#memberdeclaration.
    def enterMemberdeclaration(self, ctx:cpp2llvmParser.MemberdeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#memberdeclaration.
    def exitMemberdeclaration(self, ctx:cpp2llvmParser.MemberdeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#memberDeclaratorList.
    def enterMemberDeclaratorList(self, ctx:cpp2llvmParser.MemberDeclaratorListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#memberDeclaratorList.
    def exitMemberDeclaratorList(self, ctx:cpp2llvmParser.MemberDeclaratorListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#memberDeclarator.
    def enterMemberDeclarator(self, ctx:cpp2llvmParser.MemberDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#memberDeclarator.
    def exitMemberDeclarator(self, ctx:cpp2llvmParser.MemberDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#virtualSpecifierSeq.
    def enterVirtualSpecifierSeq(self, ctx:cpp2llvmParser.VirtualSpecifierSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#virtualSpecifierSeq.
    def exitVirtualSpecifierSeq(self, ctx:cpp2llvmParser.VirtualSpecifierSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#virtualSpecifier.
    def enterVirtualSpecifier(self, ctx:cpp2llvmParser.VirtualSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#virtualSpecifier.
    def exitVirtualSpecifier(self, ctx:cpp2llvmParser.VirtualSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#pureSpecifier.
    def enterPureSpecifier(self, ctx:cpp2llvmParser.PureSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#pureSpecifier.
    def exitPureSpecifier(self, ctx:cpp2llvmParser.PureSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#baseClause.
    def enterBaseClause(self, ctx:cpp2llvmParser.BaseClauseContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#baseClause.
    def exitBaseClause(self, ctx:cpp2llvmParser.BaseClauseContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:cpp2llvmParser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:cpp2llvmParser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#baseSpecifier.
    def enterBaseSpecifier(self, ctx:cpp2llvmParser.BaseSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#baseSpecifier.
    def exitBaseSpecifier(self, ctx:cpp2llvmParser.BaseSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#classOrDeclType.
    def enterClassOrDeclType(self, ctx:cpp2llvmParser.ClassOrDeclTypeContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#classOrDeclType.
    def exitClassOrDeclType(self, ctx:cpp2llvmParser.ClassOrDeclTypeContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#baseTypeSpecifier.
    def enterBaseTypeSpecifier(self, ctx:cpp2llvmParser.BaseTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#baseTypeSpecifier.
    def exitBaseTypeSpecifier(self, ctx:cpp2llvmParser.BaseTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:cpp2llvmParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:cpp2llvmParser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#conversionFunctionId.
    def enterConversionFunctionId(self, ctx:cpp2llvmParser.ConversionFunctionIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#conversionFunctionId.
    def exitConversionFunctionId(self, ctx:cpp2llvmParser.ConversionFunctionIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#conversionTypeId.
    def enterConversionTypeId(self, ctx:cpp2llvmParser.ConversionTypeIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#conversionTypeId.
    def exitConversionTypeId(self, ctx:cpp2llvmParser.ConversionTypeIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#conversionDeclarator.
    def enterConversionDeclarator(self, ctx:cpp2llvmParser.ConversionDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#conversionDeclarator.
    def exitConversionDeclarator(self, ctx:cpp2llvmParser.ConversionDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#constructorInitializer.
    def enterConstructorInitializer(self, ctx:cpp2llvmParser.ConstructorInitializerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#constructorInitializer.
    def exitConstructorInitializer(self, ctx:cpp2llvmParser.ConstructorInitializerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#memInitializerList.
    def enterMemInitializerList(self, ctx:cpp2llvmParser.MemInitializerListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#memInitializerList.
    def exitMemInitializerList(self, ctx:cpp2llvmParser.MemInitializerListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#memInitializer.
    def enterMemInitializer(self, ctx:cpp2llvmParser.MemInitializerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#memInitializer.
    def exitMemInitializer(self, ctx:cpp2llvmParser.MemInitializerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#meminitializerid.
    def enterMeminitializerid(self, ctx:cpp2llvmParser.MeminitializeridContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#meminitializerid.
    def exitMeminitializerid(self, ctx:cpp2llvmParser.MeminitializeridContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#operatorFunctionId.
    def enterOperatorFunctionId(self, ctx:cpp2llvmParser.OperatorFunctionIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#operatorFunctionId.
    def exitOperatorFunctionId(self, ctx:cpp2llvmParser.OperatorFunctionIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#literalOperatorId.
    def enterLiteralOperatorId(self, ctx:cpp2llvmParser.LiteralOperatorIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#literalOperatorId.
    def exitLiteralOperatorId(self, ctx:cpp2llvmParser.LiteralOperatorIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateDeclaration.
    def enterTemplateDeclaration(self, ctx:cpp2llvmParser.TemplateDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateDeclaration.
    def exitTemplateDeclaration(self, ctx:cpp2llvmParser.TemplateDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateparameterList.
    def enterTemplateparameterList(self, ctx:cpp2llvmParser.TemplateparameterListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateparameterList.
    def exitTemplateparameterList(self, ctx:cpp2llvmParser.TemplateparameterListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateParameter.
    def enterTemplateParameter(self, ctx:cpp2llvmParser.TemplateParameterContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateParameter.
    def exitTemplateParameter(self, ctx:cpp2llvmParser.TemplateParameterContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeParameter.
    def enterTypeParameter(self, ctx:cpp2llvmParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeParameter.
    def exitTypeParameter(self, ctx:cpp2llvmParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#simpleTemplateId.
    def enterSimpleTemplateId(self, ctx:cpp2llvmParser.SimpleTemplateIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#simpleTemplateId.
    def exitSimpleTemplateId(self, ctx:cpp2llvmParser.SimpleTemplateIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateId.
    def enterTemplateId(self, ctx:cpp2llvmParser.TemplateIdContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateId.
    def exitTemplateId(self, ctx:cpp2llvmParser.TemplateIdContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateName.
    def enterTemplateName(self, ctx:cpp2llvmParser.TemplateNameContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateName.
    def exitTemplateName(self, ctx:cpp2llvmParser.TemplateNameContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateArgumentList.
    def enterTemplateArgumentList(self, ctx:cpp2llvmParser.TemplateArgumentListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateArgumentList.
    def exitTemplateArgumentList(self, ctx:cpp2llvmParser.TemplateArgumentListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#templateArgument.
    def enterTemplateArgument(self, ctx:cpp2llvmParser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#templateArgument.
    def exitTemplateArgument(self, ctx:cpp2llvmParser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeNameSpecifier.
    def enterTypeNameSpecifier(self, ctx:cpp2llvmParser.TypeNameSpecifierContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeNameSpecifier.
    def exitTypeNameSpecifier(self, ctx:cpp2llvmParser.TypeNameSpecifierContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#explicitInstantiation.
    def enterExplicitInstantiation(self, ctx:cpp2llvmParser.ExplicitInstantiationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#explicitInstantiation.
    def exitExplicitInstantiation(self, ctx:cpp2llvmParser.ExplicitInstantiationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#explicitSpecialization.
    def enterExplicitSpecialization(self, ctx:cpp2llvmParser.ExplicitSpecializationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#explicitSpecialization.
    def exitExplicitSpecialization(self, ctx:cpp2llvmParser.ExplicitSpecializationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#tryBlock.
    def enterTryBlock(self, ctx:cpp2llvmParser.TryBlockContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#tryBlock.
    def exitTryBlock(self, ctx:cpp2llvmParser.TryBlockContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#functionTryBlock.
    def enterFunctionTryBlock(self, ctx:cpp2llvmParser.FunctionTryBlockContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#functionTryBlock.
    def exitFunctionTryBlock(self, ctx:cpp2llvmParser.FunctionTryBlockContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#handlerSeq.
    def enterHandlerSeq(self, ctx:cpp2llvmParser.HandlerSeqContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#handlerSeq.
    def exitHandlerSeq(self, ctx:cpp2llvmParser.HandlerSeqContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#handler.
    def enterHandler(self, ctx:cpp2llvmParser.HandlerContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#handler.
    def exitHandler(self, ctx:cpp2llvmParser.HandlerContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#exceptionDeclaration.
    def enterExceptionDeclaration(self, ctx:cpp2llvmParser.ExceptionDeclarationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#exceptionDeclaration.
    def exitExceptionDeclaration(self, ctx:cpp2llvmParser.ExceptionDeclarationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#throwExpression.
    def enterThrowExpression(self, ctx:cpp2llvmParser.ThrowExpressionContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#throwExpression.
    def exitThrowExpression(self, ctx:cpp2llvmParser.ThrowExpressionContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#exceptionSpecification.
    def enterExceptionSpecification(self, ctx:cpp2llvmParser.ExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#exceptionSpecification.
    def exitExceptionSpecification(self, ctx:cpp2llvmParser.ExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#dynamicExceptionSpecification.
    def enterDynamicExceptionSpecification(self, ctx:cpp2llvmParser.DynamicExceptionSpecificationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#dynamicExceptionSpecification.
    def exitDynamicExceptionSpecification(self, ctx:cpp2llvmParser.DynamicExceptionSpecificationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#typeIdList.
    def enterTypeIdList(self, ctx:cpp2llvmParser.TypeIdListContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#typeIdList.
    def exitTypeIdList(self, ctx:cpp2llvmParser.TypeIdListContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#noeExceptSpecification.
    def enterNoeExceptSpecification(self, ctx:cpp2llvmParser.NoeExceptSpecificationContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#noeExceptSpecification.
    def exitNoeExceptSpecification(self, ctx:cpp2llvmParser.NoeExceptSpecificationContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#theOperator.
    def enterTheOperator(self, ctx:cpp2llvmParser.TheOperatorContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#theOperator.
    def exitTheOperator(self, ctx:cpp2llvmParser.TheOperatorContext):
        pass


    # Enter a parse tree produced by cpp2llvmParser#literal.
    def enterLiteral(self, ctx:cpp2llvmParser.LiteralContext):
        pass

    # Exit a parse tree produced by cpp2llvmParser#literal.
    def exitLiteral(self, ctx:cpp2llvmParser.LiteralContext):
        pass



del cpp2llvmParser