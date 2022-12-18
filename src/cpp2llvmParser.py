# Generated from ./grammar/cpp2llvmParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,141,460,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,
        0,5,0,94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,113,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,144,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,200,
        8,5,10,5,12,5,203,9,5,1,6,1,6,1,6,1,6,1,6,5,6,210,8,6,10,6,12,6,
        213,9,6,3,6,215,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,3,7,231,8,7,1,8,1,8,5,8,235,8,8,10,8,12,8,238,9,8,1,
        8,1,8,1,9,3,9,243,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        3,10,254,8,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,262,8,11,10,11,
        12,11,265,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,3,15,291,8,15,1,15,1,15,3,15,295,8,15,1,15,1,15,3,15,299,8,
        15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,307,8,16,10,16,12,16,310,9,
        16,1,17,1,17,3,17,314,8,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,
        19,1,20,1,20,1,20,3,20,327,8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,
        22,5,22,336,8,22,10,22,12,22,339,9,22,1,23,1,23,1,23,3,23,344,8,
        23,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,3,
        27,358,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,367,8,28,1,28,
        1,28,1,29,1,29,1,29,5,29,374,8,29,10,29,12,29,377,9,29,1,30,1,30,
        1,30,1,30,3,30,383,8,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,3,32,394,8,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,3,35,406,8,35,1,35,1,35,1,36,1,36,1,36,5,36,413,8,36,10,36,
        12,36,416,9,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,3,37,425,8,37,
        1,38,1,38,3,38,429,8,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,
        3,40,439,8,40,1,41,1,41,1,41,1,41,1,41,3,41,446,8,41,1,42,1,42,1,
        42,1,42,3,42,452,8,42,1,43,1,43,1,44,1,44,1,45,1,45,1,45,0,1,10,
        46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,0,1,1,0,1,6,489,0,95,1,0,0,0,2,100,1,0,0,0,4,102,1,0,0,0,6,
        104,1,0,0,0,8,112,1,0,0,0,10,143,1,0,0,0,12,204,1,0,0,0,14,230,1,
        0,0,0,16,232,1,0,0,0,18,242,1,0,0,0,20,246,1,0,0,0,22,255,1,0,0,
        0,24,268,1,0,0,0,26,273,1,0,0,0,28,279,1,0,0,0,30,287,1,0,0,0,32,
        303,1,0,0,0,34,311,1,0,0,0,36,317,1,0,0,0,38,320,1,0,0,0,40,326,
        1,0,0,0,42,328,1,0,0,0,44,332,1,0,0,0,46,343,1,0,0,0,48,345,1,0,
        0,0,50,347,1,0,0,0,52,351,1,0,0,0,54,357,1,0,0,0,56,359,1,0,0,0,
        58,370,1,0,0,0,60,378,1,0,0,0,62,386,1,0,0,0,64,393,1,0,0,0,66,395,
        1,0,0,0,68,398,1,0,0,0,70,401,1,0,0,0,72,409,1,0,0,0,74,424,1,0,
        0,0,76,428,1,0,0,0,78,430,1,0,0,0,80,438,1,0,0,0,82,445,1,0,0,0,
        84,451,1,0,0,0,86,453,1,0,0,0,88,455,1,0,0,0,90,457,1,0,0,0,92,94,
        3,40,20,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,
        0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,0,0,1,99,1,1,0,0,0,100,101,
        7,0,0,0,101,3,1,0,0,0,102,103,5,4,0,0,103,5,1,0,0,0,104,105,3,2,
        1,0,105,7,1,0,0,0,106,113,5,132,0,0,107,108,5,132,0,0,108,109,5,
        85,0,0,109,110,3,10,5,0,110,111,5,86,0,0,111,113,1,0,0,0,112,106,
        1,0,0,0,112,107,1,0,0,0,113,9,1,0,0,0,114,115,6,5,-1,0,115,144,3,
        12,6,0,116,144,3,2,1,0,117,144,5,132,0,0,118,119,5,83,0,0,119,120,
        3,10,5,0,120,121,5,84,0,0,121,144,1,0,0,0,122,123,5,98,0,0,123,144,
        3,10,5,25,124,125,5,90,0,0,125,144,3,10,5,24,126,127,5,95,0,0,127,
        144,3,8,4,0,128,129,5,132,0,0,129,130,5,85,0,0,130,131,3,10,5,0,
        131,132,5,86,0,0,132,144,1,0,0,0,133,134,3,8,4,0,134,135,5,99,0,
        0,135,136,3,10,5,3,136,144,1,0,0,0,137,138,3,8,4,0,138,139,5,120,
        0,0,139,144,1,0,0,0,140,141,3,8,4,0,141,142,5,121,0,0,142,144,1,
        0,0,0,143,114,1,0,0,0,143,116,1,0,0,0,143,117,1,0,0,0,143,118,1,
        0,0,0,143,122,1,0,0,0,143,124,1,0,0,0,143,126,1,0,0,0,143,128,1,
        0,0,0,143,133,1,0,0,0,143,137,1,0,0,0,143,140,1,0,0,0,144,201,1,
        0,0,0,145,146,10,22,0,0,146,147,5,91,0,0,147,200,3,10,5,23,148,149,
        10,21,0,0,149,150,5,92,0,0,150,200,3,10,5,22,151,152,10,20,0,0,152,
        153,5,93,0,0,153,200,3,10,5,21,154,155,10,19,0,0,155,156,5,89,0,
        0,156,200,3,10,5,20,157,158,10,18,0,0,158,159,5,90,0,0,159,200,3,
        10,5,19,160,161,10,17,0,0,161,162,5,100,0,0,162,200,3,10,5,18,163,
        164,10,16,0,0,164,165,5,101,0,0,165,200,3,10,5,17,166,167,10,15,
        0,0,167,168,5,116,0,0,168,200,3,10,5,16,169,170,10,14,0,0,170,171,
        5,117,0,0,171,200,3,10,5,15,172,173,10,13,0,0,173,174,5,114,0,0,
        174,200,3,10,5,14,175,176,10,12,0,0,176,177,5,115,0,0,177,200,3,
        10,5,13,178,179,10,11,0,0,179,180,5,96,0,0,180,200,3,10,5,12,181,
        182,10,10,0,0,182,183,5,95,0,0,183,200,3,10,5,11,184,185,10,9,0,
        0,185,186,5,94,0,0,186,200,3,10,5,10,187,188,10,8,0,0,188,189,5,
        119,0,0,189,200,3,10,5,9,190,191,10,7,0,0,191,192,5,118,0,0,192,
        200,3,10,5,8,193,194,10,6,0,0,194,195,5,110,0,0,195,200,3,10,5,7,
        196,197,10,5,0,0,197,198,5,112,0,0,198,200,3,10,5,6,199,145,1,0,
        0,0,199,148,1,0,0,0,199,151,1,0,0,0,199,154,1,0,0,0,199,157,1,0,
        0,0,199,160,1,0,0,0,199,163,1,0,0,0,199,166,1,0,0,0,199,169,1,0,
        0,0,199,172,1,0,0,0,199,175,1,0,0,0,199,178,1,0,0,0,199,181,1,0,
        0,0,199,184,1,0,0,0,199,187,1,0,0,0,199,190,1,0,0,0,199,193,1,0,
        0,0,199,196,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,
        0,0,202,11,1,0,0,0,203,201,1,0,0,0,204,205,5,132,0,0,205,214,5,83,
        0,0,206,211,3,10,5,0,207,208,5,122,0,0,208,210,3,10,5,0,209,207,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,214,206,1,0,0,0,214,215,1,0,0,0,215,216,
        1,0,0,0,216,217,5,84,0,0,217,13,1,0,0,0,218,231,3,18,9,0,219,231,
        3,16,8,0,220,231,3,20,10,0,221,231,3,22,11,0,222,231,3,26,13,0,223,
        231,3,28,14,0,224,231,3,30,15,0,225,231,3,34,17,0,226,231,3,36,18,
        0,227,231,3,38,19,0,228,231,3,42,21,0,229,231,3,54,27,0,230,218,
        1,0,0,0,230,219,1,0,0,0,230,220,1,0,0,0,230,221,1,0,0,0,230,222,
        1,0,0,0,230,223,1,0,0,0,230,224,1,0,0,0,230,225,1,0,0,0,230,226,
        1,0,0,0,230,227,1,0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,15,1,
        0,0,0,232,236,5,87,0,0,233,235,3,14,7,0,234,233,1,0,0,0,235,238,
        1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,239,1,0,0,0,238,236,
        1,0,0,0,239,240,5,88,0,0,240,17,1,0,0,0,241,243,3,10,5,0,242,241,
        1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,244,245,5,128,0,0,245,19,
        1,0,0,0,246,247,5,41,0,0,247,248,5,83,0,0,248,249,3,10,5,0,249,250,
        5,84,0,0,250,253,3,14,7,0,251,252,5,30,0,0,252,254,3,14,7,0,253,
        251,1,0,0,0,253,254,1,0,0,0,254,21,1,0,0,0,255,256,5,65,0,0,256,
        257,5,83,0,0,257,258,3,10,5,0,258,259,5,84,0,0,259,263,5,87,0,0,
        260,262,3,24,12,0,261,260,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,
        0,263,264,1,0,0,0,264,266,1,0,0,0,265,263,1,0,0,0,266,267,5,88,0,
        0,267,23,1,0,0,0,268,269,5,14,0,0,269,270,3,6,3,0,270,271,5,126,
        0,0,271,272,3,14,7,0,272,25,1,0,0,0,273,274,5,82,0,0,274,275,5,83,
        0,0,275,276,3,10,5,0,276,277,5,84,0,0,277,278,3,14,7,0,278,27,1,
        0,0,0,279,280,5,27,0,0,280,281,3,14,7,0,281,282,5,82,0,0,282,283,
        5,83,0,0,283,284,3,10,5,0,284,285,5,84,0,0,285,286,5,128,0,0,286,
        29,1,0,0,0,287,288,5,38,0,0,288,290,5,83,0,0,289,291,3,32,16,0,290,
        289,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,294,5,128,0,0,293,
        295,3,10,5,0,294,293,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,
        298,5,128,0,0,297,299,3,32,16,0,298,297,1,0,0,0,298,299,1,0,0,0,
        299,300,1,0,0,0,300,301,5,84,0,0,301,302,3,14,7,0,302,31,1,0,0,0,
        303,308,3,10,5,0,304,305,5,122,0,0,305,307,3,10,5,0,306,304,1,0,
        0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,309,1,0,0,0,309,33,1,0,0,
        0,310,308,1,0,0,0,311,313,5,57,0,0,312,314,3,10,5,0,313,312,1,0,
        0,0,313,314,1,0,0,0,314,315,1,0,0,0,315,316,5,128,0,0,316,35,1,0,
        0,0,317,318,5,13,0,0,318,319,5,128,0,0,319,37,1,0,0,0,320,321,5,
        23,0,0,321,322,5,128,0,0,322,39,1,0,0,0,323,327,3,42,21,0,324,327,
        3,54,27,0,325,327,3,64,32,0,326,323,1,0,0,0,326,324,1,0,0,0,326,
        325,1,0,0,0,327,41,1,0,0,0,328,329,3,76,38,0,329,330,3,44,22,0,330,
        331,5,128,0,0,331,43,1,0,0,0,332,337,3,46,23,0,333,334,5,122,0,0,
        334,336,3,46,23,0,335,333,1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,
        0,337,338,1,0,0,0,338,45,1,0,0,0,339,337,1,0,0,0,340,344,3,48,24,
        0,341,344,3,50,25,0,342,344,3,52,26,0,343,340,1,0,0,0,343,341,1,
        0,0,0,343,342,1,0,0,0,344,47,1,0,0,0,345,346,5,132,0,0,346,49,1,
        0,0,0,347,348,5,132,0,0,348,349,5,99,0,0,349,350,3,6,3,0,350,51,
        1,0,0,0,351,352,5,132,0,0,352,353,5,99,0,0,353,354,3,10,5,0,354,
        53,1,0,0,0,355,358,3,56,28,0,356,358,3,60,30,0,357,355,1,0,0,0,357,
        356,1,0,0,0,358,55,1,0,0,0,359,360,3,80,40,0,360,366,3,62,31,0,361,
        362,5,99,0,0,362,363,5,87,0,0,363,364,3,58,29,0,364,365,5,88,0,0,
        365,367,1,0,0,0,366,361,1,0,0,0,366,367,1,0,0,0,367,368,1,0,0,0,
        368,369,5,128,0,0,369,57,1,0,0,0,370,375,3,10,5,0,371,372,5,122,
        0,0,372,374,3,10,5,0,373,371,1,0,0,0,374,377,1,0,0,0,375,373,1,0,
        0,0,375,376,1,0,0,0,376,59,1,0,0,0,377,375,1,0,0,0,378,379,3,88,
        44,0,379,382,3,62,31,0,380,381,5,99,0,0,381,383,3,4,2,0,382,380,
        1,0,0,0,382,383,1,0,0,0,383,384,1,0,0,0,384,385,5,128,0,0,385,61,
        1,0,0,0,386,387,5,132,0,0,387,388,5,85,0,0,388,389,5,1,0,0,389,390,
        5,86,0,0,390,63,1,0,0,0,391,394,3,66,33,0,392,394,3,68,34,0,393,
        391,1,0,0,0,393,392,1,0,0,0,394,65,1,0,0,0,395,396,3,70,35,0,396,
        397,5,128,0,0,397,67,1,0,0,0,398,399,3,70,35,0,399,400,3,16,8,0,
        400,69,1,0,0,0,401,402,3,76,38,0,402,403,5,132,0,0,403,405,5,83,
        0,0,404,406,3,72,36,0,405,404,1,0,0,0,405,406,1,0,0,0,406,407,1,
        0,0,0,407,408,5,84,0,0,408,71,1,0,0,0,409,414,3,74,37,0,410,411,
        5,122,0,0,411,413,3,74,37,0,412,410,1,0,0,0,413,416,1,0,0,0,414,
        412,1,0,0,0,414,415,1,0,0,0,415,73,1,0,0,0,416,414,1,0,0,0,417,418,
        3,78,39,0,418,419,5,132,0,0,419,425,1,0,0,0,420,421,3,80,40,0,421,
        422,5,132,0,0,422,425,1,0,0,0,423,425,5,131,0,0,424,417,1,0,0,0,
        424,420,1,0,0,0,424,423,1,0,0,0,425,75,1,0,0,0,426,429,3,78,39,0,
        427,429,3,80,40,0,428,426,1,0,0,0,428,427,1,0,0,0,429,77,1,0,0,0,
        430,431,3,80,40,0,431,432,5,91,0,0,432,79,1,0,0,0,433,439,3,82,41,
        0,434,439,3,84,42,0,435,439,3,86,43,0,436,439,3,88,44,0,437,439,
        3,90,45,0,438,433,1,0,0,0,438,434,1,0,0,0,438,435,1,0,0,0,438,436,
        1,0,0,0,438,437,1,0,0,0,439,81,1,0,0,0,440,446,5,43,0,0,441,446,
        5,44,0,0,442,446,5,58,0,0,443,444,5,44,0,0,444,446,5,44,0,0,445,
        440,1,0,0,0,445,441,1,0,0,0,445,442,1,0,0,0,445,443,1,0,0,0,446,
        83,1,0,0,0,447,452,5,37,0,0,448,452,5,28,0,0,449,450,5,44,0,0,450,
        452,5,28,0,0,451,447,1,0,0,0,451,448,1,0,0,0,451,449,1,0,0,0,452,
        85,1,0,0,0,453,454,5,12,0,0,454,87,1,0,0,0,455,456,5,16,0,0,456,
        89,1,0,0,0,457,458,5,79,0,0,458,91,1,0,0,0,32,95,112,143,199,201,
        211,214,230,236,242,253,263,290,294,298,308,313,326,337,343,357,
        366,375,382,393,405,414,424,428,438,445,451
    ]

class cpp2llvmParser ( Parser ):

    grammarFileName = "cpp2llvmParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'alignas'", "'alignof'", "'asm'", "'auto'", "'bool'", 
                     "'break'", "'case'", "'catch'", "'char'", "'char16_t'", 
                     "'char32_t'", "'class'", "'const'", "'constexpr'", 
                     "'const_cast'", "'continue'", "'decltype'", "'default'", 
                     "'delete'", "'do'", "'double'", "'dynamic_cast'", "'else'", 
                     "'enum'", "'explicit'", "'export'", "'extern'", "'false'", 
                     "'final'", "'float'", "'for'", "'friend'", "'goto'", 
                     "'if'", "'inline'", "'int'", "'long'", "'mutable'", 
                     "'namespace'", "'new'", "'noexcept'", "'nullptr'", 
                     "'operator'", "'override'", "'private'", "'protected'", 
                     "'public'", "'register'", "'reinterpret_cast'", "'return'", 
                     "'short'", "'signed'", "'sizeof'", "'static'", "'static_assert'", 
                     "'static_cast'", "'struct'", "'switch'", "'template'", 
                     "'this'", "'thread_local'", "'throw'", "'true'", "'try'", 
                     "'typedef'", "'typeid'", "'typename'", "'union'", "'unsigned'", 
                     "'using'", "'virtual'", "'void'", "'volatile'", "'wchar_t'", 
                     "'while'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'&'", "'|'", 
                     "'~'", "<INVALID>", "'='", "'<'", "'>'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'^='", "'&='", "'|='", "'<<'", 
                     "'<<='", "'>>'", "'>>='", "'=='", "'!='", "'<='", "'>='", 
                     "<INVALID>", "<INVALID>", "'++'", "'--'", "','", "'->*'", 
                     "'->'", "'?'", "':'", "'::'", "';'", "'.'", "'.*'", 
                     "'...'" ]

    symbolicNames = [ "<INVALID>", "IntegerLiteral", "CharacterLiteral", 
                      "FloatingLiteral", "StringLiteral", "BooleanLiteral", 
                      "PointerLiteral", "Directive", "Alignas", "Alignof", 
                      "Asm", "Auto", "Bool", "Break", "Case", "Catch", "Char", 
                      "Char16", "Char32", "Class", "Const", "Constexpr", 
                      "Const_cast", "Continue", "Decltype", "Default", "Delete", 
                      "Do", "Double", "Dynamic_cast", "Else", "Enum", "Explicit", 
                      "Export", "Extern", "False_", "Final", "Float", "For", 
                      "Friend", "Goto", "If", "Inline", "Int", "Long", "Mutable", 
                      "Namespace", "New", "Noexcept", "Nullptr", "Operator", 
                      "Override", "Private", "Protected", "Public", "Register", 
                      "Reinterpret_cast", "Return", "Short", "Signed", "Sizeof", 
                      "Static", "Static_assert", "Static_cast", "Struct", 
                      "Switch", "Template", "This", "Thread_local", "Throw", 
                      "True_", "Try", "Typedef", "Typeid_", "Typename_", 
                      "Union", "Unsigned", "Using", "Virtual", "Void", "Volatile", 
                      "Wchar", "While", "LeftParen", "RightParen", "LeftBracket", 
                      "RightBracket", "LeftBrace", "RightBrace", "Plus", 
                      "Minus", "Star", "Div", "Mod", "Caret", "And", "Or", 
                      "Tilde", "Not", "Assign", "Less", "Greater", "PlusAssign", 
                      "MinusAssign", "StarAssign", "DivAssign", "ModAssign", 
                      "XorAssign", "AndAssign", "OrAssign", "LeftShift", 
                      "LeftShiftAssign", "RightShift", "RightShiftAssign", 
                      "Equal", "NotEqual", "LessEqual", "GreaterEqual", 
                      "AndAnd", "OrOr", "PlusPlus", "MinusMinus", "Comma", 
                      "ArrowStar", "Arrow", "Question", "Colon", "Doublecolon", 
                      "Semi", "Dot", "DotStar", "Ellipsis", "Identifier", 
                      "DecimalLiteral", "OctalLiteral", "HexadecimalLiteral", 
                      "BinaryLiteral", "Integersuffix", "Whitespace", "Newline", 
                      "BlockComment", "LineComment" ]

    RULE_translationUnit = 0
    RULE_literal = 1
    RULE_stringLiteral = 2
    RULE_constExpression = 3
    RULE_leftExpression = 4
    RULE_expression = 5
    RULE_functionCall = 6
    RULE_statement = 7
    RULE_compoundStatement = 8
    RULE_expressionStatement = 9
    RULE_ifStatement = 10
    RULE_switchStatement = 11
    RULE_caseStatement = 12
    RULE_whileStatement = 13
    RULE_doWhileStatement = 14
    RULE_forStatement = 15
    RULE_forExprSet = 16
    RULE_returnStatement = 17
    RULE_breakStatement = 18
    RULE_continueStatement = 19
    RULE_declaration = 20
    RULE_variableDeclarator = 21
    RULE_variableDeclarationList = 22
    RULE_variableDeclaration = 23
    RULE_varDeclWithoutInit = 24
    RULE_varDeclWithConstInit = 25
    RULE_varDeclWithNormalInit = 26
    RULE_arrayDeclarator = 27
    RULE_normalArrayDeclaration = 28
    RULE_arrayAssginExpressionList = 29
    RULE_stringDeclaration = 30
    RULE_arrayName = 31
    RULE_functionDeclarator = 32
    RULE_functionDeclaration = 33
    RULE_functionDefinition = 34
    RULE_functionHead = 35
    RULE_functionParameterList = 36
    RULE_functionParameter = 37
    RULE_typeModifier = 38
    RULE_pointerTypeModifier = 39
    RULE_normalTypeModifier = 40
    RULE_integerTypeModifier = 41
    RULE_realTypeModifier = 42
    RULE_boolTypeModifier = 43
    RULE_charTypeModifier = 44
    RULE_voidTypeModifier = 45

    ruleNames =  [ "translationUnit", "literal", "stringLiteral", "constExpression", 
                   "leftExpression", "expression", "functionCall", "statement", 
                   "compoundStatement", "expressionStatement", "ifStatement", 
                   "switchStatement", "caseStatement", "whileStatement", 
                   "doWhileStatement", "forStatement", "forExprSet", "returnStatement", 
                   "breakStatement", "continueStatement", "declaration", 
                   "variableDeclarator", "variableDeclarationList", "variableDeclaration", 
                   "varDeclWithoutInit", "varDeclWithConstInit", "varDeclWithNormalInit", 
                   "arrayDeclarator", "normalArrayDeclaration", "arrayAssginExpressionList", 
                   "stringDeclaration", "arrayName", "functionDeclarator", 
                   "functionDeclaration", "functionDefinition", "functionHead", 
                   "functionParameterList", "functionParameter", "typeModifier", 
                   "pointerTypeModifier", "normalTypeModifier", "integerTypeModifier", 
                   "realTypeModifier", "boolTypeModifier", "charTypeModifier", 
                   "voidTypeModifier" ]

    EOF = Token.EOF
    IntegerLiteral=1
    CharacterLiteral=2
    FloatingLiteral=3
    StringLiteral=4
    BooleanLiteral=5
    PointerLiteral=6
    Directive=7
    Alignas=8
    Alignof=9
    Asm=10
    Auto=11
    Bool=12
    Break=13
    Case=14
    Catch=15
    Char=16
    Char16=17
    Char32=18
    Class=19
    Const=20
    Constexpr=21
    Const_cast=22
    Continue=23
    Decltype=24
    Default=25
    Delete=26
    Do=27
    Double=28
    Dynamic_cast=29
    Else=30
    Enum=31
    Explicit=32
    Export=33
    Extern=34
    False_=35
    Final=36
    Float=37
    For=38
    Friend=39
    Goto=40
    If=41
    Inline=42
    Int=43
    Long=44
    Mutable=45
    Namespace=46
    New=47
    Noexcept=48
    Nullptr=49
    Operator=50
    Override=51
    Private=52
    Protected=53
    Public=54
    Register=55
    Reinterpret_cast=56
    Return=57
    Short=58
    Signed=59
    Sizeof=60
    Static=61
    Static_assert=62
    Static_cast=63
    Struct=64
    Switch=65
    Template=66
    This=67
    Thread_local=68
    Throw=69
    True_=70
    Try=71
    Typedef=72
    Typeid_=73
    Typename_=74
    Union=75
    Unsigned=76
    Using=77
    Virtual=78
    Void=79
    Volatile=80
    Wchar=81
    While=82
    LeftParen=83
    RightParen=84
    LeftBracket=85
    RightBracket=86
    LeftBrace=87
    RightBrace=88
    Plus=89
    Minus=90
    Star=91
    Div=92
    Mod=93
    Caret=94
    And=95
    Or=96
    Tilde=97
    Not=98
    Assign=99
    Less=100
    Greater=101
    PlusAssign=102
    MinusAssign=103
    StarAssign=104
    DivAssign=105
    ModAssign=106
    XorAssign=107
    AndAssign=108
    OrAssign=109
    LeftShift=110
    LeftShiftAssign=111
    RightShift=112
    RightShiftAssign=113
    Equal=114
    NotEqual=115
    LessEqual=116
    GreaterEqual=117
    AndAnd=118
    OrOr=119
    PlusPlus=120
    MinusMinus=121
    Comma=122
    ArrowStar=123
    Arrow=124
    Question=125
    Colon=126
    Doublecolon=127
    Semi=128
    Dot=129
    DotStar=130
    Ellipsis=131
    Identifier=132
    DecimalLiteral=133
    OctalLiteral=134
    HexadecimalLiteral=135
    BinaryLiteral=136
    Integersuffix=137
    Whitespace=138
    Newline=139
    BlockComment=140
    LineComment=141

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(cpp2llvmParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.DeclarationContext,i)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_translationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationUnit" ):
                listener.enterTranslationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationUnit" ):
                listener.exitTranslationUnit(self)




    def translationUnit(self):

        localctx = cpp2llvmParser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79:
                self.state = 92
                self.declaration()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(cpp2llvmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(cpp2llvmParser.IntegerLiteral, 0)

        def CharacterLiteral(self):
            return self.getToken(cpp2llvmParser.CharacterLiteral, 0)

        def FloatingLiteral(self):
            return self.getToken(cpp2llvmParser.FloatingLiteral, 0)

        def StringLiteral(self):
            return self.getToken(cpp2llvmParser.StringLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(cpp2llvmParser.BooleanLiteral, 0)

        def PointerLiteral(self):
            return self.getToken(cpp2llvmParser.PointerLiteral, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = cpp2llvmParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(cpp2llvmParser.StringLiteral, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)




    def stringLiteral(self):

        localctx = cpp2llvmParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(cpp2llvmParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(cpp2llvmParser.LiteralContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_constExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstExpression" ):
                listener.enterConstExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstExpression" ):
                listener.exitConstExpression(self)




    def constExpression(self):

        localctx = cpp2llvmParser.ConstExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def LeftBracket(self):
            return self.getToken(cpp2llvmParser.LeftBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def RightBracket(self):
            return self.getToken(cpp2llvmParser.RightBracket, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_leftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeftExpression" ):
                listener.enterLeftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeftExpression" ):
                listener.exitLeftExpression(self)




    def leftExpression(self):

        localctx = cpp2llvmParser.LeftExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_leftExpression)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(cpp2llvmParser.Identifier)

                self.state = 108
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 109
                self.expression(0)
                self.state = 110
                self.match(cpp2llvmParser.RightBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionCallContext,0)


        def literal(self):
            return self.getTypedRuleContext(cpp2llvmParser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,i)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def Not(self):
            return self.getToken(cpp2llvmParser.Not, 0)

        def Minus(self):
            return self.getToken(cpp2llvmParser.Minus, 0)

        def And(self):
            return self.getToken(cpp2llvmParser.And, 0)

        def leftExpression(self):
            return self.getTypedRuleContext(cpp2llvmParser.LeftExpressionContext,0)


        def LeftBracket(self):
            return self.getToken(cpp2llvmParser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(cpp2llvmParser.RightBracket, 0)

        def Assign(self):
            return self.getToken(cpp2llvmParser.Assign, 0)

        def PlusPlus(self):
            return self.getToken(cpp2llvmParser.PlusPlus, 0)

        def MinusMinus(self):
            return self.getToken(cpp2llvmParser.MinusMinus, 0)

        def Star(self):
            return self.getToken(cpp2llvmParser.Star, 0)

        def Div(self):
            return self.getToken(cpp2llvmParser.Div, 0)

        def Mod(self):
            return self.getToken(cpp2llvmParser.Mod, 0)

        def Plus(self):
            return self.getToken(cpp2llvmParser.Plus, 0)

        def Less(self):
            return self.getToken(cpp2llvmParser.Less, 0)

        def Greater(self):
            return self.getToken(cpp2llvmParser.Greater, 0)

        def LessEqual(self):
            return self.getToken(cpp2llvmParser.LessEqual, 0)

        def GreaterEqual(self):
            return self.getToken(cpp2llvmParser.GreaterEqual, 0)

        def Equal(self):
            return self.getToken(cpp2llvmParser.Equal, 0)

        def NotEqual(self):
            return self.getToken(cpp2llvmParser.NotEqual, 0)

        def Or(self):
            return self.getToken(cpp2llvmParser.Or, 0)

        def Caret(self):
            return self.getToken(cpp2llvmParser.Caret, 0)

        def OrOr(self):
            return self.getToken(cpp2llvmParser.OrOr, 0)

        def AndAnd(self):
            return self.getToken(cpp2llvmParser.AndAnd, 0)

        def LeftShift(self):
            return self.getToken(cpp2llvmParser.LeftShift, 0)

        def RightShift(self):
            return self.getToken(cpp2llvmParser.RightShift, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cpp2llvmParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 115
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 116
                self.literal()
                pass

            elif la_ == 3:
                self.state = 117
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 4:
                self.state = 118
                self.match(cpp2llvmParser.LeftParen)
                self.state = 119
                self.expression(0)
                self.state = 120
                self.match(cpp2llvmParser.RightParen)
                pass

            elif la_ == 5:
                self.state = 122
                self.match(cpp2llvmParser.Not)
                self.state = 123
                self.expression(25)
                pass

            elif la_ == 6:
                self.state = 124
                self.match(cpp2llvmParser.Minus)
                self.state = 125
                self.expression(24)
                pass

            elif la_ == 7:
                self.state = 126
                self.match(cpp2llvmParser.And)
                self.state = 127
                self.leftExpression()
                pass

            elif la_ == 8:
                self.state = 128
                self.match(cpp2llvmParser.Identifier)
                self.state = 129
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 130
                self.expression(0)
                self.state = 131
                self.match(cpp2llvmParser.RightBracket)
                pass

            elif la_ == 9:
                self.state = 133
                self.leftExpression()
                self.state = 134
                self.match(cpp2llvmParser.Assign)
                self.state = 135
                self.expression(3)
                pass

            elif la_ == 10:
                self.state = 137
                self.leftExpression()
                self.state = 138
                self.match(cpp2llvmParser.PlusPlus)
                pass

            elif la_ == 11:
                self.state = 140
                self.leftExpression()
                self.state = 141
                self.match(cpp2llvmParser.MinusMinus)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 199
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 146
                        self.match(cpp2llvmParser.Star)
                        self.state = 147
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 149
                        self.match(cpp2llvmParser.Div)
                        self.state = 150
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 152
                        self.match(cpp2llvmParser.Mod)
                        self.state = 153
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 155
                        self.match(cpp2llvmParser.Plus)
                        self.state = 156
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 158
                        self.match(cpp2llvmParser.Minus)
                        self.state = 159
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 161
                        self.match(cpp2llvmParser.Less)
                        self.state = 162
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 164
                        self.match(cpp2llvmParser.Greater)
                        self.state = 165
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 167
                        self.match(cpp2llvmParser.LessEqual)
                        self.state = 168
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 170
                        self.match(cpp2llvmParser.GreaterEqual)
                        self.state = 171
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 173
                        self.match(cpp2llvmParser.Equal)
                        self.state = 174
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 176
                        self.match(cpp2llvmParser.NotEqual)
                        self.state = 177
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 178
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 179
                        self.match(cpp2llvmParser.Or)
                        self.state = 180
                        self.expression(12)
                        pass

                    elif la_ == 13:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 182
                        self.match(cpp2llvmParser.And)
                        self.state = 183
                        self.expression(11)
                        pass

                    elif la_ == 14:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 185
                        self.match(cpp2llvmParser.Caret)
                        self.state = 186
                        self.expression(10)
                        pass

                    elif la_ == 15:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 187
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 188
                        self.match(cpp2llvmParser.OrOr)
                        self.state = 189
                        self.expression(9)
                        pass

                    elif la_ == 16:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 190
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 191
                        self.match(cpp2llvmParser.AndAnd)
                        self.state = 192
                        self.expression(8)
                        pass

                    elif la_ == 17:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 193
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 194
                        self.match(cpp2llvmParser.LeftShift)
                        self.state = 195
                        self.expression(7)
                        pass

                    elif la_ == 18:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 196
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 197
                        self.match(cpp2llvmParser.RightShift)
                        self.state = 198
                        self.expression(6)
                        pass

             
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Comma)
            else:
                return self.getToken(cpp2llvmParser.Comma, i)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = cpp2llvmParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(cpp2llvmParser.Identifier)
            self.state = 205
            self.match(cpp2llvmParser.LeftParen)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 206
                self.expression(0)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==122:
                    self.state = 207
                    self.match(cpp2llvmParser.Comma)
                    self.state = 208
                    self.expression(0)
                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 216
            self.match(cpp2llvmParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.CompoundStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.IfStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.SwitchStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.ContinueStatementContext,0)


        def variableDeclarator(self):
            return self.getTypedRuleContext(cpp2llvmParser.VariableDeclaratorContext,0)


        def arrayDeclarator(self):
            return self.getTypedRuleContext(cpp2llvmParser.ArrayDeclaratorContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = cpp2llvmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.switchStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.doWhileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 224
                self.forStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 225
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 226
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 227
                self.continueStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 228
                self.variableDeclarator()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 229
                self.arrayDeclarator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftBrace(self):
            return self.getToken(cpp2llvmParser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(cpp2llvmParser.RightBrace, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.StatementContext,i)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)




    def compoundStatement(self):

        localctx = cpp2llvmParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 432374564257869950) != 0 or (((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & -9223372027152941055) != 0 or _la==132:
                self.state = 233
                self.statement()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(cpp2llvmParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = cpp2llvmParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 241
                self.expression(0)


            self.state = 244
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(cpp2llvmParser.If, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.StatementContext,i)


        def Else(self):
            return self.getToken(cpp2llvmParser.Else, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = cpp2llvmParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(cpp2llvmParser.If)
            self.state = 247
            self.match(cpp2llvmParser.LeftParen)
            self.state = 248
            self.expression(0)
            self.state = 249
            self.match(cpp2llvmParser.RightParen)
            self.state = 250
            self.statement()
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 251
                self.match(cpp2llvmParser.Else)
                self.state = 252
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Switch(self):
            return self.getToken(cpp2llvmParser.Switch, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def LeftBrace(self):
            return self.getToken(cpp2llvmParser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(cpp2llvmParser.RightBrace, 0)

        def caseStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.CaseStatementContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.CaseStatementContext,i)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = cpp2llvmParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(cpp2llvmParser.Switch)
            self.state = 256
            self.match(cpp2llvmParser.LeftParen)
            self.state = 257
            self.expression(0)
            self.state = 258
            self.match(cpp2llvmParser.RightParen)
            self.state = 259
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 260
                self.caseStatement()
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self.match(cpp2llvmParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Case(self):
            return self.getToken(cpp2llvmParser.Case, 0)

        def constExpression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ConstExpressionContext,0)


        def Colon(self):
            return self.getToken(cpp2llvmParser.Colon, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp2llvmParser.StatementContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_caseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStatement" ):
                listener.enterCaseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStatement" ):
                listener.exitCaseStatement(self)




    def caseStatement(self):

        localctx = cpp2llvmParser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(cpp2llvmParser.Case)
            self.state = 269
            self.constExpression()
            self.state = 270
            self.match(cpp2llvmParser.Colon)
            self.state = 271
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(cpp2llvmParser.While, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp2llvmParser.StatementContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = cpp2llvmParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(cpp2llvmParser.While)
            self.state = 274
            self.match(cpp2llvmParser.LeftParen)
            self.state = 275
            self.expression(0)
            self.state = 276
            self.match(cpp2llvmParser.RightParen)
            self.state = 277
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Do(self):
            return self.getToken(cpp2llvmParser.Do, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp2llvmParser.StatementContext,0)


        def While(self):
            return self.getToken(cpp2llvmParser.While, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = cpp2llvmParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(cpp2llvmParser.Do)
            self.state = 280
            self.statement()
            self.state = 281
            self.match(cpp2llvmParser.While)
            self.state = 282
            self.match(cpp2llvmParser.LeftParen)
            self.state = 283
            self.expression(0)
            self.state = 284
            self.match(cpp2llvmParser.RightParen)
            self.state = 285
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(cpp2llvmParser.For, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def Semi(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Semi)
            else:
                return self.getToken(cpp2llvmParser.Semi, i)

        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp2llvmParser.StatementContext,0)


        def forExprSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.ForExprSetContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.ForExprSetContext,i)


        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = cpp2llvmParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(cpp2llvmParser.For)
            self.state = 288
            self.match(cpp2llvmParser.LeftParen)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 289
                self.forExprSet()


            self.state = 292
            self.match(cpp2llvmParser.Semi)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 293
                self.expression(0)


            self.state = 296
            self.match(cpp2llvmParser.Semi)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 297
                self.forExprSet()


            self.state = 300
            self.match(cpp2llvmParser.RightParen)
            self.state = 301
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExprSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Comma)
            else:
                return self.getToken(cpp2llvmParser.Comma, i)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_forExprSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForExprSet" ):
                listener.enterForExprSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForExprSet" ):
                listener.exitForExprSet(self)




    def forExprSet(self):

        localctx = cpp2llvmParser.ForExprSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forExprSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.expression(0)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 304
                self.match(cpp2llvmParser.Comma)
                self.state = 305
                self.expression(0)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(cpp2llvmParser.Return, 0)

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = cpp2llvmParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(cpp2llvmParser.Return)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 312
                self.expression(0)


            self.state = 315
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(cpp2llvmParser.Break, 0)

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = cpp2llvmParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(cpp2llvmParser.Break)
            self.state = 318
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(cpp2llvmParser.Continue, 0)

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = cpp2llvmParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(cpp2llvmParser.Continue)
            self.state = 321
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self):
            return self.getTypedRuleContext(cpp2llvmParser.VariableDeclaratorContext,0)


        def arrayDeclarator(self):
            return self.getTypedRuleContext(cpp2llvmParser.ArrayDeclaratorContext,0)


        def functionDeclarator(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionDeclaratorContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = cpp2llvmParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_declaration)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.variableDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.arrayDeclarator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.functionDeclarator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.TypeModifierContext,0)


        def variableDeclarationList(self):
            return self.getTypedRuleContext(cpp2llvmParser.VariableDeclarationListContext,0)


        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)




    def variableDeclarator(self):

        localctx = cpp2llvmParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variableDeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.typeModifier()
            self.state = 329
            self.variableDeclarationList()
            self.state = 330
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.VariableDeclarationContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Comma)
            else:
                return self.getToken(cpp2llvmParser.Comma, i)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_variableDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationList" ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationList" ):
                listener.exitVariableDeclarationList(self)




    def variableDeclarationList(self):

        localctx = cpp2llvmParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.variableDeclaration()
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 333
                self.match(cpp2llvmParser.Comma)
                self.state = 334
                self.variableDeclaration()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclWithoutInit(self):
            return self.getTypedRuleContext(cpp2llvmParser.VarDeclWithoutInitContext,0)


        def varDeclWithConstInit(self):
            return self.getTypedRuleContext(cpp2llvmParser.VarDeclWithConstInitContext,0)


        def varDeclWithNormalInit(self):
            return self.getTypedRuleContext(cpp2llvmParser.VarDeclWithNormalInitContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = cpp2llvmParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variableDeclaration)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.varDeclWithoutInit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.varDeclWithConstInit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.varDeclWithNormalInit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclWithoutInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_varDeclWithoutInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclWithoutInit" ):
                listener.enterVarDeclWithoutInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclWithoutInit" ):
                listener.exitVarDeclWithoutInit(self)




    def varDeclWithoutInit(self):

        localctx = cpp2llvmParser.VarDeclWithoutInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_varDeclWithoutInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(cpp2llvmParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclWithConstInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def Assign(self):
            return self.getToken(cpp2llvmParser.Assign, 0)

        def constExpression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ConstExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_varDeclWithConstInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclWithConstInit" ):
                listener.enterVarDeclWithConstInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclWithConstInit" ):
                listener.exitVarDeclWithConstInit(self)




    def varDeclWithConstInit(self):

        localctx = cpp2llvmParser.VarDeclWithConstInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_varDeclWithConstInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(cpp2llvmParser.Identifier)
            self.state = 348
            self.match(cpp2llvmParser.Assign)
            self.state = 349
            self.constExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclWithNormalInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def Assign(self):
            return self.getToken(cpp2llvmParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_varDeclWithNormalInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclWithNormalInit" ):
                listener.enterVarDeclWithNormalInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclWithNormalInit" ):
                listener.exitVarDeclWithNormalInit(self)




    def varDeclWithNormalInit(self):

        localctx = cpp2llvmParser.VarDeclWithNormalInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_varDeclWithNormalInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(cpp2llvmParser.Identifier)
            self.state = 352
            self.match(cpp2llvmParser.Assign)
            self.state = 353
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalArrayDeclaration(self):
            return self.getTypedRuleContext(cpp2llvmParser.NormalArrayDeclarationContext,0)


        def stringDeclaration(self):
            return self.getTypedRuleContext(cpp2llvmParser.StringDeclarationContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_arrayDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclarator" ):
                listener.enterArrayDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclarator" ):
                listener.exitArrayDeclarator(self)




    def arrayDeclarator(self):

        localctx = cpp2llvmParser.ArrayDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrayDeclarator)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.normalArrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.stringDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalArrayDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.NormalTypeModifierContext,0)


        def arrayName(self):
            return self.getTypedRuleContext(cpp2llvmParser.ArrayNameContext,0)


        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def Assign(self):
            return self.getToken(cpp2llvmParser.Assign, 0)

        def LeftBrace(self):
            return self.getToken(cpp2llvmParser.LeftBrace, 0)

        def arrayAssginExpressionList(self):
            return self.getTypedRuleContext(cpp2llvmParser.ArrayAssginExpressionListContext,0)


        def RightBrace(self):
            return self.getToken(cpp2llvmParser.RightBrace, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_normalArrayDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalArrayDeclaration" ):
                listener.enterNormalArrayDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalArrayDeclaration" ):
                listener.exitNormalArrayDeclaration(self)




    def normalArrayDeclaration(self):

        localctx = cpp2llvmParser.NormalArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_normalArrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.normalTypeModifier()
            self.state = 360
            self.arrayName()
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 361
                self.match(cpp2llvmParser.Assign)
                self.state = 362
                self.match(cpp2llvmParser.LeftBrace)
                self.state = 363
                self.arrayAssginExpressionList()
                self.state = 364
                self.match(cpp2llvmParser.RightBrace)


            self.state = 368
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssginExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Comma)
            else:
                return self.getToken(cpp2llvmParser.Comma, i)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_arrayAssginExpressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssginExpressionList" ):
                listener.enterArrayAssginExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssginExpressionList" ):
                listener.exitArrayAssginExpressionList(self)




    def arrayAssginExpressionList(self):

        localctx = cpp2llvmParser.ArrayAssginExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arrayAssginExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.expression(0)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 371
                self.match(cpp2llvmParser.Comma)
                self.state = 372
                self.expression(0)
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.CharTypeModifierContext,0)


        def arrayName(self):
            return self.getTypedRuleContext(cpp2llvmParser.ArrayNameContext,0)


        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def Assign(self):
            return self.getToken(cpp2llvmParser.Assign, 0)

        def stringLiteral(self):
            return self.getTypedRuleContext(cpp2llvmParser.StringLiteralContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_stringDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringDeclaration" ):
                listener.enterStringDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringDeclaration" ):
                listener.exitStringDeclaration(self)




    def stringDeclaration(self):

        localctx = cpp2llvmParser.StringDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stringDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.charTypeModifier()
            self.state = 379
            self.arrayName()
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 380
                self.match(cpp2llvmParser.Assign)
                self.state = 381
                self.stringLiteral()


            self.state = 384
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def LeftBracket(self):
            return self.getToken(cpp2llvmParser.LeftBracket, 0)

        def IntegerLiteral(self):
            return self.getToken(cpp2llvmParser.IntegerLiteral, 0)

        def RightBracket(self):
            return self.getToken(cpp2llvmParser.RightBracket, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_arrayName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayName" ):
                listener.enterArrayName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayName" ):
                listener.exitArrayName(self)




    def arrayName(self):

        localctx = cpp2llvmParser.ArrayNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arrayName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(cpp2llvmParser.Identifier)
            self.state = 387
            self.match(cpp2llvmParser.LeftBracket)
            self.state = 388
            self.match(cpp2llvmParser.IntegerLiteral)
            self.state = 389
            self.match(cpp2llvmParser.RightBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclaration(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionDeclarationContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclarator" ):
                listener.enterFunctionDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclarator" ):
                listener.exitFunctionDeclarator(self)




    def functionDeclarator(self):

        localctx = cpp2llvmParser.FunctionDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_functionDeclarator)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.functionDefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionHead(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionHeadContext,0)


        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = cpp2llvmParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.functionHead()
            self.state = 396
            self.match(cpp2llvmParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionHead(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionHeadContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = cpp2llvmParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.functionHead()
            self.state = 399
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionHeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.TypeModifierContext,0)


        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def functionParameterList(self):
            return self.getTypedRuleContext(cpp2llvmParser.FunctionParameterListContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionHead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionHead" ):
                listener.enterFunctionHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionHead" ):
                listener.exitFunctionHead(self)




    def functionHead(self):

        localctx = cpp2llvmParser.FunctionHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_functionHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.typeModifier()
            self.state = 402
            self.match(cpp2llvmParser.Identifier)
            self.state = 403
            self.match(cpp2llvmParser.LeftParen)
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79 or _la==131:
                self.state = 404
                self.functionParameterList()


            self.state = 407
            self.match(cpp2llvmParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.FunctionParameterContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.FunctionParameterContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Comma)
            else:
                return self.getToken(cpp2llvmParser.Comma, i)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameterList" ):
                listener.enterFunctionParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameterList" ):
                listener.exitFunctionParameterList(self)




    def functionParameterList(self):

        localctx = cpp2llvmParser.FunctionParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_functionParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.functionParameter()
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 410
                self.match(cpp2llvmParser.Comma)
                self.state = 411
                self.functionParameter()
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointerTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.PointerTypeModifierContext,0)


        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def normalTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.NormalTypeModifierContext,0)


        def Ellipsis(self):
            return self.getToken(cpp2llvmParser.Ellipsis, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_functionParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameter" ):
                listener.enterFunctionParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameter" ):
                listener.exitFunctionParameter(self)




    def functionParameter(self):

        localctx = cpp2llvmParser.FunctionParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_functionParameter)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.pointerTypeModifier()
                self.state = 418
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.normalTypeModifier()
                self.state = 421
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 423
                self.match(cpp2llvmParser.Ellipsis)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointerTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.PointerTypeModifierContext,0)


        def normalTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.NormalTypeModifierContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_typeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeModifier" ):
                listener.enterTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeModifier" ):
                listener.exitTypeModifier(self)




    def typeModifier(self):

        localctx = cpp2llvmParser.TypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_typeModifier)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.pointerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.normalTypeModifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.NormalTypeModifierContext,0)


        def Star(self):
            return self.getToken(cpp2llvmParser.Star, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_pointerTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerTypeModifier" ):
                listener.enterPointerTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerTypeModifier" ):
                listener.exitPointerTypeModifier(self)




    def pointerTypeModifier(self):

        localctx = cpp2llvmParser.PointerTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_pointerTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.normalTypeModifier()
            self.state = 431
            self.match(cpp2llvmParser.Star)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.IntegerTypeModifierContext,0)


        def realTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.RealTypeModifierContext,0)


        def boolTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.BoolTypeModifierContext,0)


        def charTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.CharTypeModifierContext,0)


        def voidTypeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.VoidTypeModifierContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_normalTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalTypeModifier" ):
                listener.enterNormalTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalTypeModifier" ):
                listener.exitNormalTypeModifier(self)




    def normalTypeModifier(self):

        localctx = cpp2llvmParser.NormalTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_normalTypeModifier)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.integerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.realTypeModifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 435
                self.boolTypeModifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.charTypeModifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 437
                self.voidTypeModifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Int(self):
            return self.getToken(cpp2llvmParser.Int, 0)

        def Long(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Long)
            else:
                return self.getToken(cpp2llvmParser.Long, i)

        def Short(self):
            return self.getToken(cpp2llvmParser.Short, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_integerTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerTypeModifier" ):
                listener.enterIntegerTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerTypeModifier" ):
                listener.exitIntegerTypeModifier(self)




    def integerTypeModifier(self):

        localctx = cpp2llvmParser.IntegerTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_integerTypeModifier)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(cpp2llvmParser.Int)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(cpp2llvmParser.Long)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.match(cpp2llvmParser.Short)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
                self.match(cpp2llvmParser.Long)
                self.state = 444
                self.match(cpp2llvmParser.Long)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(cpp2llvmParser.Float, 0)

        def Double(self):
            return self.getToken(cpp2llvmParser.Double, 0)

        def Long(self):
            return self.getToken(cpp2llvmParser.Long, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_realTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealTypeModifier" ):
                listener.enterRealTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealTypeModifier" ):
                listener.exitRealTypeModifier(self)




    def realTypeModifier(self):

        localctx = cpp2llvmParser.RealTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_realTypeModifier)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(cpp2llvmParser.Float)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(cpp2llvmParser.Double)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.match(cpp2llvmParser.Long)
                self.state = 450
                self.match(cpp2llvmParser.Double)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bool(self):
            return self.getToken(cpp2llvmParser.Bool, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_boolTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolTypeModifier" ):
                listener.enterBoolTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolTypeModifier" ):
                listener.exitBoolTypeModifier(self)




    def boolTypeModifier(self):

        localctx = cpp2llvmParser.BoolTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_boolTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(cpp2llvmParser.Bool)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Char(self):
            return self.getToken(cpp2llvmParser.Char, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_charTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharTypeModifier" ):
                listener.enterCharTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharTypeModifier" ):
                listener.exitCharTypeModifier(self)




    def charTypeModifier(self):

        localctx = cpp2llvmParser.CharTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_charTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(cpp2llvmParser.Char)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidTypeModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Void(self):
            return self.getToken(cpp2llvmParser.Void, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_voidTypeModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidTypeModifier" ):
                listener.enterVoidTypeModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidTypeModifier" ):
                listener.exitVoidTypeModifier(self)




    def voidTypeModifier(self):

        localctx = cpp2llvmParser.VoidTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_voidTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(cpp2llvmParser.Void)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 5)
         




