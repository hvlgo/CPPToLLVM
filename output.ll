; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"main"()
{
__main:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  br label %".4"
.3:
  %".6" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_0", i32 0, i32 0
  %".7" = load i32, i32* %"a"
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".7")
  %".9" = load i32, i32* %"a"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %"a"
  %".12" = load i32, i32* %"a"
  br label %".4"
.4:
  %".15" = load i32, i32* %"a"
  %".16" = icmp ne i32 %".15", 5
  %".17" = icmp ne i1 %".16", 0
  br i1 %".17", label %".3", label %".5"
.5:
  %"b" = alloca i32
  store i32 1, i32* %"b"
  br label %".21"
.20:
  %".23" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".24" = load i32, i32* %"b"
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %".24")
  %".26" = load i32, i32* %"b"
  %".27" = add i32 %".26", 2
  store i32 %".27", i32* %"b"
  %".29" = load i32, i32* %"b"
  br label %".21"
.21:
  %".32" = load i32, i32* %"b"
  %".33" = icmp slt i32 %".32", 23
  %".34" = icmp ne i1 %".33", 0
  br i1 %".34", label %".20", label %".22"
.22:
  ret i32 0
}

@"__string_0" = internal global [4 x i8] c"%d \00"
@"__string_1" = internal global [4 x i8] c"%d \00"