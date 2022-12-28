; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

declare i32 @"scanf"(i8* %".1", ...)

declare i32 @"printf"(i8* %".1", ...)

@"a" = internal global i32 0
define i32 @"main"()
{
__main:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_0", i32 0, i32 0
  %".3" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".4" = load i32, i32* @"a"
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"%d\00"
@"__string_1" = internal global [4 x i8] c"%d\0a\00"