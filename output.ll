; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"p" = internal global [100 x i8] zeroinitializer
@"s" = internal global [100 x i8] zeroinitializer
@"next" = internal global [100 x i32] zeroinitializer
define void @"getNext"(i32 %".1")
{
__getNext:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %".4" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 0
  %".5" = load i32, i32* %".4"
  store i32 0, i32* %".4"
  %".7" = load i32, i32* %".4"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  store i32 0, i32* %"j"
  %".11" = load i32, i32* %"j"
  store i32 1, i32* %"i"
  %".13" = load i32, i32* %"i"
  br label %".14"
.14:
  %".19" = load i32, i32* %"i"
  %".20" = load i32, i32* %"n"
  %".21" = icmp slt i32 %".19", %".20"
  %".22" = icmp ne i1 %".21", 0
  br i1 %".22", label %".15", label %".17"
.15:
  br label %".24"
.16:
  %".70" = load i32, i32* %"i"
  %".71" = add i32 %".70", 1
  store i32 %".71", i32* %"i"
  br label %".14"
.17:
  ret void
.24:
  %".28" = load i32, i32* %"j"
  %".29" = load i32, i32* %"i"
  %".30" = getelementptr inbounds [100 x i8], [100 x i8]* @"p", i32 0, i32 %".29"
  %".31" = load i8, i8* %".30"
  %".32" = load i32, i32* %"j"
  %".33" = getelementptr inbounds [100 x i8], [100 x i8]* @"p", i32 0, i32 %".32"
  %".34" = load i8, i8* %".33"
  %".35" = icmp ne i8 %".31", %".34"
  %".36" = icmp ne i32 %".28", 0
  %".37" = icmp ne i1 %".35", 0
  %".38" = and i1 %".36", %".37"
  %".39" = icmp ne i1 %".38", 0
  br i1 %".39", label %".25", label %".26"
.25:
  %".41" = load i32, i32* %"j"
  %".42" = sub i32 %".41", 1
  %".43" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".42"
  %".44" = load i32, i32* %".43"
  store i32 %".44", i32* %"j"
  %".46" = load i32, i32* %"j"
  br label %".24"
.26:
  %".50" = load i32, i32* %"i"
  %".51" = getelementptr inbounds [100 x i8], [100 x i8]* @"p", i32 0, i32 %".50"
  %".52" = load i8, i8* %".51"
  %".53" = load i32, i32* %"j"
  %".54" = getelementptr inbounds [100 x i8], [100 x i8]* @"p", i32 0, i32 %".53"
  %".55" = load i8, i8* %".54"
  %".56" = icmp eq i8 %".52", %".55"
  %".57" = icmp ne i1 %".56", 0
  br i1 %".57", label %".48", label %".49"
.48:
  %".59" = load i32, i32* %"j"
  %".60" = add i32 %".59", 1
  store i32 %".60", i32* %"j"
  br label %".49"
.49:
  %".63" = load i32, i32* %"i"
  %".64" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".63"
  %".65" = load i32, i32* %".64"
  %".66" = load i32, i32* %"j"
  store i32 %".66", i32* %".64"
  %".68" = load i32, i32* %".64"
  br label %".16"
}

define i32 @"main"()
{
__main:
  %"n" = alloca i32
  store i32 0, i32* %"n"
  %"m" = alloca i32
  store i32 0, i32* %"m"
  %".4" = getelementptr inbounds [15 x i8], [15 x i8]* @"__string_0", i32 0, i32 0
  %".5" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_1", i32 0, i32 0
  %".6" = getelementptr inbounds [12 x i8], [12 x i8]* @"__string_2", i32 0, i32 0
  %".7" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_3", i32 0, i32 0
  %".8" = load i32, i32* %"n"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  store i32 0, i32* %"i"
  %".12" = load i32, i32* %"i"
  store i32 0, i32* %"j"
  %".14" = load i32, i32* %"j"
  br label %".15"
.15:
  %".20" = load i32, i32* %"i"
  %".21" = load i32, i32* %"m"
  %".22" = icmp slt i32 %".20", %".21"
  %".23" = icmp ne i1 %".22", 0
  br i1 %".23", label %".16", label %".18"
.16:
  br label %".25"
.17:
  %".84" = load i32, i32* %"i"
  %".85" = add i32 %".84", 1
  store i32 %".85", i32* %"i"
  br label %".15"
.18:
  ret i32 0
.25:
  %".29" = load i32, i32* %"j"
  %".30" = load i32, i32* %"i"
  %".31" = getelementptr inbounds [100 x i8], [100 x i8]* @"s", i32 0, i32 %".30"
  %".32" = load i8, i8* %".31"
  %".33" = load i32, i32* %"j"
  %".34" = getelementptr inbounds [100 x i8], [100 x i8]* @"p", i32 0, i32 %".33"
  %".35" = load i8, i8* %".34"
  %".36" = icmp ne i8 %".32", %".35"
  %".37" = icmp ne i32 %".29", 0
  %".38" = icmp ne i1 %".36", 0
  %".39" = and i1 %".37", %".38"
  %".40" = icmp ne i1 %".39", 0
  br i1 %".40", label %".26", label %".27"
.26:
  %".42" = load i32, i32* %"j"
  %".43" = sub i32 %".42", 1
  %".44" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".43"
  %".45" = load i32, i32* %".44"
  store i32 %".45", i32* %"j"
  %".47" = load i32, i32* %"j"
  br label %".25"
.27:
  %".51" = load i32, i32* %"i"
  %".52" = getelementptr inbounds [100 x i8], [100 x i8]* @"s", i32 0, i32 %".51"
  %".53" = load i8, i8* %".52"
  %".54" = load i32, i32* %"j"
  %".55" = getelementptr inbounds [100 x i8], [100 x i8]* @"p", i32 0, i32 %".54"
  %".56" = load i8, i8* %".55"
  %".57" = icmp eq i8 %".53", %".56"
  %".58" = icmp ne i1 %".57", 0
  br i1 %".58", label %".49", label %".50"
.49:
  %".60" = load i32, i32* %"j"
  %".61" = add i32 %".60", 1
  store i32 %".61", i32* %"j"
  br label %".50"
.50:
  %".66" = load i32, i32* %"j"
  %".67" = load i32, i32* %"n"
  %".68" = icmp eq i32 %".66", %".67"
  %".69" = icmp ne i1 %".68", 0
  br i1 %".69", label %".64", label %".65"
.64:
  %".71" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_4", i32 0, i32 0
  %".72" = load i32, i32* %"i"
  %".73" = load i32, i32* %"n"
  %".74" = add i32 %".73", 1
  %".75" = sub i32 %".72", %".74"
  %".76" = load i32, i32* %"j"
  %".77" = sub i32 %".76", 1
  %".78" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".77"
  %".79" = load i32, i32* %".78"
  store i32 %".79", i32* %"j"
  %".81" = load i32, i32* %"j"
  br label %".65"
.65:
  br label %".17"
}

@"__string_0" = internal global [15 x i8] c"enter pattern\0a\00"
@"__string_1" = internal global [6 x i8] c"%d %s\00"
@"__string_2" = internal global [12 x i8] c"enter text\0a\00"
@"__string_3" = internal global [6 x i8] c"%d %s\00"
@"__string_4" = internal global [4 x i8] c"%d \00"