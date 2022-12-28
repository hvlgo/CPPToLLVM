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
        4,1,141,456,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,5,0,92,
        8,0,10,0,12,0,95,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,111,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,142,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,198,8,5,10,5,
        12,5,201,9,5,1,6,1,6,1,6,1,6,1,6,5,6,208,8,6,10,6,12,6,211,9,6,3,
        6,213,8,6,1,6,1,6,1,7,3,7,218,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,232,8,7,1,8,1,8,5,8,236,8,8,10,8,12,8,239,
        9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,250,8,9,1,10,1,10,1,
        10,1,10,1,10,1,10,5,10,258,8,10,10,10,12,10,261,9,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,287,8,14,1,14,1,
        14,3,14,291,8,14,1,14,1,14,3,14,295,8,14,1,14,1,14,1,14,1,15,1,15,
        1,15,5,15,303,8,15,10,15,12,15,306,9,15,1,16,1,16,3,16,310,8,16,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,3,19,323,
        8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,5,21,332,8,21,10,21,12,21,
        335,9,21,1,22,1,22,1,22,3,22,340,8,22,1,23,1,23,1,24,1,24,1,24,1,
        24,1,25,1,25,1,25,1,25,1,26,1,26,3,26,354,8,26,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,3,27,363,8,27,1,27,1,27,1,28,1,28,1,28,5,28,370,
        8,28,10,28,12,28,373,9,28,1,29,1,29,1,29,1,29,3,29,379,8,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,3,31,390,8,31,1,32,1,32,
        1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,3,34,402,8,34,1,34,1,34,
        1,35,1,35,1,35,5,35,409,8,35,10,35,12,35,412,9,35,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,3,36,421,8,36,1,37,1,37,3,37,425,8,37,1,38,1,
        38,1,38,1,39,1,39,1,39,1,39,1,39,3,39,435,8,39,1,40,1,40,1,40,1,
        40,1,40,3,40,442,8,40,1,41,1,41,1,41,1,41,3,41,448,8,41,1,42,1,42,
        1,43,1,43,1,44,1,44,1,44,0,1,10,45,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,0,1,1,0,1,6,486,0,93,1,0,0,0,2,
        98,1,0,0,0,4,100,1,0,0,0,6,102,1,0,0,0,8,110,1,0,0,0,10,141,1,0,
        0,0,12,202,1,0,0,0,14,231,1,0,0,0,16,233,1,0,0,0,18,242,1,0,0,0,
        20,251,1,0,0,0,22,264,1,0,0,0,24,269,1,0,0,0,26,275,1,0,0,0,28,283,
        1,0,0,0,30,299,1,0,0,0,32,307,1,0,0,0,34,313,1,0,0,0,36,316,1,0,
        0,0,38,322,1,0,0,0,40,324,1,0,0,0,42,328,1,0,0,0,44,339,1,0,0,0,
        46,341,1,0,0,0,48,343,1,0,0,0,50,347,1,0,0,0,52,353,1,0,0,0,54,355,
        1,0,0,0,56,366,1,0,0,0,58,374,1,0,0,0,60,382,1,0,0,0,62,389,1,0,
        0,0,64,391,1,0,0,0,66,394,1,0,0,0,68,397,1,0,0,0,70,405,1,0,0,0,
        72,420,1,0,0,0,74,424,1,0,0,0,76,426,1,0,0,0,78,434,1,0,0,0,80,441,
        1,0,0,0,82,447,1,0,0,0,84,449,1,0,0,0,86,451,1,0,0,0,88,453,1,0,
        0,0,90,92,3,38,19,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,
        94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,0,0,1,97,1,1,0,0,
        0,98,99,7,0,0,0,99,3,1,0,0,0,100,101,5,4,0,0,101,5,1,0,0,0,102,103,
        3,2,1,0,103,7,1,0,0,0,104,111,5,132,0,0,105,106,5,132,0,0,106,107,
        5,85,0,0,107,108,3,10,5,0,108,109,5,86,0,0,109,111,1,0,0,0,110,104,
        1,0,0,0,110,105,1,0,0,0,111,9,1,0,0,0,112,113,6,5,-1,0,113,142,3,
        12,6,0,114,142,3,2,1,0,115,142,5,132,0,0,116,117,5,83,0,0,117,118,
        3,10,5,0,118,119,5,84,0,0,119,142,1,0,0,0,120,121,5,98,0,0,121,142,
        3,10,5,25,122,123,5,90,0,0,123,142,3,10,5,24,124,125,5,95,0,0,125,
        142,3,8,4,0,126,127,5,132,0,0,127,128,5,85,0,0,128,129,3,10,5,0,
        129,130,5,86,0,0,130,142,1,0,0,0,131,132,3,8,4,0,132,133,5,99,0,
        0,133,134,3,10,5,3,134,142,1,0,0,0,135,136,3,8,4,0,136,137,5,120,
        0,0,137,142,1,0,0,0,138,139,3,8,4,0,139,140,5,121,0,0,140,142,1,
        0,0,0,141,112,1,0,0,0,141,114,1,0,0,0,141,115,1,0,0,0,141,116,1,
        0,0,0,141,120,1,0,0,0,141,122,1,0,0,0,141,124,1,0,0,0,141,126,1,
        0,0,0,141,131,1,0,0,0,141,135,1,0,0,0,141,138,1,0,0,0,142,199,1,
        0,0,0,143,144,10,22,0,0,144,145,5,91,0,0,145,198,3,10,5,23,146,147,
        10,21,0,0,147,148,5,92,0,0,148,198,3,10,5,22,149,150,10,20,0,0,150,
        151,5,93,0,0,151,198,3,10,5,21,152,153,10,19,0,0,153,154,5,89,0,
        0,154,198,3,10,5,20,155,156,10,18,0,0,156,157,5,90,0,0,157,198,3,
        10,5,19,158,159,10,17,0,0,159,160,5,100,0,0,160,198,3,10,5,18,161,
        162,10,16,0,0,162,163,5,101,0,0,163,198,3,10,5,17,164,165,10,15,
        0,0,165,166,5,116,0,0,166,198,3,10,5,16,167,168,10,14,0,0,168,169,
        5,117,0,0,169,198,3,10,5,15,170,171,10,13,0,0,171,172,5,114,0,0,
        172,198,3,10,5,14,173,174,10,12,0,0,174,175,5,115,0,0,175,198,3,
        10,5,13,176,177,10,11,0,0,177,178,5,96,0,0,178,198,3,10,5,12,179,
        180,10,10,0,0,180,181,5,95,0,0,181,198,3,10,5,11,182,183,10,9,0,
        0,183,184,5,94,0,0,184,198,3,10,5,10,185,186,10,8,0,0,186,187,5,
        119,0,0,187,198,3,10,5,9,188,189,10,7,0,0,189,190,5,118,0,0,190,
        198,3,10,5,8,191,192,10,6,0,0,192,193,5,110,0,0,193,198,3,10,5,7,
        194,195,10,5,0,0,195,196,5,112,0,0,196,198,3,10,5,6,197,143,1,0,
        0,0,197,146,1,0,0,0,197,149,1,0,0,0,197,152,1,0,0,0,197,155,1,0,
        0,0,197,158,1,0,0,0,197,161,1,0,0,0,197,164,1,0,0,0,197,167,1,0,
        0,0,197,170,1,0,0,0,197,173,1,0,0,0,197,176,1,0,0,0,197,179,1,0,
        0,0,197,182,1,0,0,0,197,185,1,0,0,0,197,188,1,0,0,0,197,191,1,0,
        0,0,197,194,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,
        0,0,200,11,1,0,0,0,201,199,1,0,0,0,202,203,5,132,0,0,203,212,5,83,
        0,0,204,209,3,10,5,0,205,206,5,122,0,0,206,208,3,10,5,0,207,205,
        1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,213,
        1,0,0,0,211,209,1,0,0,0,212,204,1,0,0,0,212,213,1,0,0,0,213,214,
        1,0,0,0,214,215,5,84,0,0,215,13,1,0,0,0,216,218,3,10,5,0,217,216,
        1,0,0,0,217,218,1,0,0,0,218,219,1,0,0,0,219,232,5,128,0,0,220,232,
        3,16,8,0,221,232,3,18,9,0,222,232,3,20,10,0,223,232,3,24,12,0,224,
        232,3,26,13,0,225,232,3,28,14,0,226,232,3,32,16,0,227,232,3,34,17,
        0,228,232,3,36,18,0,229,232,3,40,20,0,230,232,3,52,26,0,231,217,
        1,0,0,0,231,220,1,0,0,0,231,221,1,0,0,0,231,222,1,0,0,0,231,223,
        1,0,0,0,231,224,1,0,0,0,231,225,1,0,0,0,231,226,1,0,0,0,231,227,
        1,0,0,0,231,228,1,0,0,0,231,229,1,0,0,0,231,230,1,0,0,0,232,15,1,
        0,0,0,233,237,5,87,0,0,234,236,3,14,7,0,235,234,1,0,0,0,236,239,
        1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,237,
        1,0,0,0,240,241,5,88,0,0,241,17,1,0,0,0,242,243,5,41,0,0,243,244,
        5,83,0,0,244,245,3,10,5,0,245,246,5,84,0,0,246,249,3,14,7,0,247,
        248,5,30,0,0,248,250,3,14,7,0,249,247,1,0,0,0,249,250,1,0,0,0,250,
        19,1,0,0,0,251,252,5,65,0,0,252,253,5,83,0,0,253,254,3,10,5,0,254,
        255,5,84,0,0,255,259,5,87,0,0,256,258,3,22,11,0,257,256,1,0,0,0,
        258,261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,262,1,0,0,0,
        261,259,1,0,0,0,262,263,5,88,0,0,263,21,1,0,0,0,264,265,5,14,0,0,
        265,266,3,6,3,0,266,267,5,126,0,0,267,268,3,14,7,0,268,23,1,0,0,
        0,269,270,5,82,0,0,270,271,5,83,0,0,271,272,3,10,5,0,272,273,5,84,
        0,0,273,274,3,14,7,0,274,25,1,0,0,0,275,276,5,27,0,0,276,277,3,14,
        7,0,277,278,5,82,0,0,278,279,5,83,0,0,279,280,3,10,5,0,280,281,5,
        84,0,0,281,282,5,128,0,0,282,27,1,0,0,0,283,284,5,38,0,0,284,286,
        5,83,0,0,285,287,3,30,15,0,286,285,1,0,0,0,286,287,1,0,0,0,287,288,
        1,0,0,0,288,290,5,128,0,0,289,291,3,10,5,0,290,289,1,0,0,0,290,291,
        1,0,0,0,291,292,1,0,0,0,292,294,5,128,0,0,293,295,3,30,15,0,294,
        293,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,297,5,84,0,0,297,
        298,3,14,7,0,298,29,1,0,0,0,299,304,3,10,5,0,300,301,5,122,0,0,301,
        303,3,10,5,0,302,300,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,
        305,1,0,0,0,305,31,1,0,0,0,306,304,1,0,0,0,307,309,5,57,0,0,308,
        310,3,10,5,0,309,308,1,0,0,0,309,310,1,0,0,0,310,311,1,0,0,0,311,
        312,5,128,0,0,312,33,1,0,0,0,313,314,5,13,0,0,314,315,5,128,0,0,
        315,35,1,0,0,0,316,317,5,23,0,0,317,318,5,128,0,0,318,37,1,0,0,0,
        319,323,3,40,20,0,320,323,3,52,26,0,321,323,3,62,31,0,322,319,1,
        0,0,0,322,320,1,0,0,0,322,321,1,0,0,0,323,39,1,0,0,0,324,325,3,74,
        37,0,325,326,3,42,21,0,326,327,5,128,0,0,327,41,1,0,0,0,328,333,
        3,44,22,0,329,330,5,122,0,0,330,332,3,44,22,0,331,329,1,0,0,0,332,
        335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,43,1,0,0,0,335,333,
        1,0,0,0,336,340,3,46,23,0,337,340,3,48,24,0,338,340,3,50,25,0,339,
        336,1,0,0,0,339,337,1,0,0,0,339,338,1,0,0,0,340,45,1,0,0,0,341,342,
        5,132,0,0,342,47,1,0,0,0,343,344,5,132,0,0,344,345,5,99,0,0,345,
        346,3,6,3,0,346,49,1,0,0,0,347,348,5,132,0,0,348,349,5,99,0,0,349,
        350,3,10,5,0,350,51,1,0,0,0,351,354,3,54,27,0,352,354,3,58,29,0,
        353,351,1,0,0,0,353,352,1,0,0,0,354,53,1,0,0,0,355,356,3,78,39,0,
        356,362,3,60,30,0,357,358,5,99,0,0,358,359,5,87,0,0,359,360,3,56,
        28,0,360,361,5,88,0,0,361,363,1,0,0,0,362,357,1,0,0,0,362,363,1,
        0,0,0,363,364,1,0,0,0,364,365,5,128,0,0,365,55,1,0,0,0,366,371,3,
        10,5,0,367,368,5,122,0,0,368,370,3,10,5,0,369,367,1,0,0,0,370,373,
        1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,57,1,0,0,0,373,371,1,
        0,0,0,374,375,3,86,43,0,375,378,3,60,30,0,376,377,5,99,0,0,377,379,
        3,4,2,0,378,376,1,0,0,0,378,379,1,0,0,0,379,380,1,0,0,0,380,381,
        5,128,0,0,381,59,1,0,0,0,382,383,5,132,0,0,383,384,5,85,0,0,384,
        385,5,1,0,0,385,386,5,86,0,0,386,61,1,0,0,0,387,390,3,64,32,0,388,
        390,3,66,33,0,389,387,1,0,0,0,389,388,1,0,0,0,390,63,1,0,0,0,391,
        392,3,68,34,0,392,393,5,128,0,0,393,65,1,0,0,0,394,395,3,68,34,0,
        395,396,3,16,8,0,396,67,1,0,0,0,397,398,3,74,37,0,398,399,5,132,
        0,0,399,401,5,83,0,0,400,402,3,70,35,0,401,400,1,0,0,0,401,402,1,
        0,0,0,402,403,1,0,0,0,403,404,5,84,0,0,404,69,1,0,0,0,405,410,3,
        72,36,0,406,407,5,122,0,0,407,409,3,72,36,0,408,406,1,0,0,0,409,
        412,1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,71,1,0,0,0,412,410,
        1,0,0,0,413,414,3,76,38,0,414,415,5,132,0,0,415,421,1,0,0,0,416,
        417,3,78,39,0,417,418,5,132,0,0,418,421,1,0,0,0,419,421,5,131,0,
        0,420,413,1,0,0,0,420,416,1,0,0,0,420,419,1,0,0,0,421,73,1,0,0,0,
        422,425,3,76,38,0,423,425,3,78,39,0,424,422,1,0,0,0,424,423,1,0,
        0,0,425,75,1,0,0,0,426,427,3,78,39,0,427,428,5,91,0,0,428,77,1,0,
        0,0,429,435,3,80,40,0,430,435,3,82,41,0,431,435,3,84,42,0,432,435,
        3,86,43,0,433,435,3,88,44,0,434,429,1,0,0,0,434,430,1,0,0,0,434,
        431,1,0,0,0,434,432,1,0,0,0,434,433,1,0,0,0,435,79,1,0,0,0,436,442,
        5,43,0,0,437,442,5,44,0,0,438,442,5,58,0,0,439,440,5,44,0,0,440,
        442,5,44,0,0,441,436,1,0,0,0,441,437,1,0,0,0,441,438,1,0,0,0,441,
        439,1,0,0,0,442,81,1,0,0,0,443,448,5,37,0,0,444,448,5,28,0,0,445,
        446,5,44,0,0,446,448,5,28,0,0,447,443,1,0,0,0,447,444,1,0,0,0,447,
        445,1,0,0,0,448,83,1,0,0,0,449,450,5,12,0,0,450,85,1,0,0,0,451,452,
        5,16,0,0,452,87,1,0,0,0,453,454,5,79,0,0,454,89,1,0,0,0,32,93,110,
        141,197,199,209,212,217,231,237,249,259,286,290,294,304,309,322,
        333,339,353,362,371,378,389,401,410,420,424,434,441,447
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
    RULE_ifStatement = 9
    RULE_switchStatement = 10
    RULE_caseStatement = 11
    RULE_whileStatement = 12
    RULE_doWhileStatement = 13
    RULE_forStatement = 14
    RULE_forExprSet = 15
    RULE_returnStatement = 16
    RULE_breakStatement = 17
    RULE_continueStatement = 18
    RULE_declaration = 19
    RULE_variableDeclarator = 20
    RULE_variableDeclarationList = 21
    RULE_variableDeclaration = 22
    RULE_varDeclWithoutInit = 23
    RULE_varDeclWithConstInit = 24
    RULE_varDeclWithNormalInit = 25
    RULE_arrayDeclarator = 26
    RULE_normalArrayDeclaration = 27
    RULE_arrayAssginExpressionList = 28
    RULE_stringDeclaration = 29
    RULE_arrayName = 30
    RULE_functionDeclarator = 31
    RULE_functionDeclaration = 32
    RULE_functionDefinition = 33
    RULE_functionHead = 34
    RULE_functionParameterList = 35
    RULE_functionParameter = 36
    RULE_typeModifier = 37
    RULE_pointerTypeModifier = 38
    RULE_normalTypeModifier = 39
    RULE_integerTypeModifier = 40
    RULE_realTypeModifier = 41
    RULE_boolTypeModifier = 42
    RULE_charTypeModifier = 43
    RULE_voidTypeModifier = 44

    ruleNames =  [ "translationUnit", "literal", "stringLiteral", "constExpression", 
                   "leftExpression", "expression", "functionCall", "statement", 
                   "compoundStatement", "ifStatement", "switchStatement", 
                   "caseStatement", "whileStatement", "doWhileStatement", 
                   "forStatement", "forExprSet", "returnStatement", "breakStatement", 
                   "continueStatement", "declaration", "variableDeclarator", 
                   "variableDeclarationList", "variableDeclaration", "varDeclWithoutInit", 
                   "varDeclWithConstInit", "varDeclWithNormalInit", "arrayDeclarator", 
                   "normalArrayDeclaration", "arrayAssginExpressionList", 
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslationUnit" ):
                return visitor.visitTranslationUnit(self)
            else:
                return visitor.visitChildren(self)




    def translationUnit(self):

        localctx = cpp2llvmParser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79:
                self.state = 90
                self.declaration()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = cpp2llvmParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteral(self):

        localctx = cpp2llvmParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstExpression" ):
                return visitor.visitConstExpression(self)
            else:
                return visitor.visitChildren(self)




    def constExpression(self):

        localctx = cpp2llvmParser.ConstExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftExpression" ):
                return visitor.visitLeftExpression(self)
            else:
                return visitor.visitChildren(self)




    def leftExpression(self):

        localctx = cpp2llvmParser.LeftExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_leftExpression)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(cpp2llvmParser.Identifier)

                self.state = 106
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 107
                self.expression(0)
                self.state = 108
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cpp2llvmParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 113
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 114
                self.literal()
                pass

            elif la_ == 3:
                self.state = 115
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 4:
                self.state = 116
                self.match(cpp2llvmParser.LeftParen)
                self.state = 117
                self.expression(0)
                self.state = 118
                self.match(cpp2llvmParser.RightParen)
                pass

            elif la_ == 5:
                self.state = 120
                self.match(cpp2llvmParser.Not)
                self.state = 121
                self.expression(25)
                pass

            elif la_ == 6:
                self.state = 122
                self.match(cpp2llvmParser.Minus)
                self.state = 123
                self.expression(24)
                pass

            elif la_ == 7:
                self.state = 124
                self.match(cpp2llvmParser.And)
                self.state = 125
                self.leftExpression()
                pass

            elif la_ == 8:
                self.state = 126
                self.match(cpp2llvmParser.Identifier)
                self.state = 127
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 128
                self.expression(0)
                self.state = 129
                self.match(cpp2llvmParser.RightBracket)
                pass

            elif la_ == 9:
                self.state = 131
                self.leftExpression()
                self.state = 132
                self.match(cpp2llvmParser.Assign)
                self.state = 133
                self.expression(3)
                pass

            elif la_ == 10:
                self.state = 135
                self.leftExpression()
                self.state = 136
                self.match(cpp2llvmParser.PlusPlus)
                pass

            elif la_ == 11:
                self.state = 138
                self.leftExpression()
                self.state = 139
                self.match(cpp2llvmParser.MinusMinus)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 197
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 143
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 144
                        self.match(cpp2llvmParser.Star)
                        self.state = 145
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 146
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 147
                        self.match(cpp2llvmParser.Div)
                        self.state = 148
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 149
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 150
                        self.match(cpp2llvmParser.Mod)
                        self.state = 151
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 152
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 153
                        self.match(cpp2llvmParser.Plus)
                        self.state = 154
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 155
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 156
                        self.match(cpp2llvmParser.Minus)
                        self.state = 157
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 159
                        self.match(cpp2llvmParser.Less)
                        self.state = 160
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 162
                        self.match(cpp2llvmParser.Greater)
                        self.state = 163
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 165
                        self.match(cpp2llvmParser.LessEqual)
                        self.state = 166
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 168
                        self.match(cpp2llvmParser.GreaterEqual)
                        self.state = 169
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 171
                        self.match(cpp2llvmParser.Equal)
                        self.state = 172
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 174
                        self.match(cpp2llvmParser.NotEqual)
                        self.state = 175
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 177
                        self.match(cpp2llvmParser.Or)
                        self.state = 178
                        self.expression(12)
                        pass

                    elif la_ == 13:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 180
                        self.match(cpp2llvmParser.And)
                        self.state = 181
                        self.expression(11)
                        pass

                    elif la_ == 14:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 182
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 183
                        self.match(cpp2llvmParser.Caret)
                        self.state = 184
                        self.expression(10)
                        pass

                    elif la_ == 15:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 186
                        self.match(cpp2llvmParser.OrOr)
                        self.state = 187
                        self.expression(9)
                        pass

                    elif la_ == 16:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 188
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 189
                        self.match(cpp2llvmParser.AndAnd)
                        self.state = 190
                        self.expression(8)
                        pass

                    elif la_ == 17:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 192
                        self.match(cpp2llvmParser.LeftShift)
                        self.state = 193
                        self.expression(7)
                        pass

                    elif la_ == 18:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 195
                        self.match(cpp2llvmParser.RightShift)
                        self.state = 196
                        self.expression(6)
                        pass

             
                self.state = 201
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = cpp2llvmParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(cpp2llvmParser.Identifier)
            self.state = 203
            self.match(cpp2llvmParser.LeftParen)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 204
                self.expression(0)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==122:
                    self.state = 205
                    self.match(cpp2llvmParser.Comma)
                    self.state = 206
                    self.expression(0)
                    self.state = 211
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 214
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

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = cpp2llvmParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                    self.state = 216
                    self.expression(0)


                self.state = 219
                self.match(cpp2llvmParser.Semi)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.switchStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.doWhileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 225
                self.forStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 226
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 227
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 228
                self.continueStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 229
                self.variableDeclarator()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 230
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = cpp2llvmParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 432374564257869950) != 0 or (((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & -9223372027152941055) != 0 or _la==132:
                self.state = 234
                self.statement()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(cpp2llvmParser.RightBrace)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = cpp2llvmParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(cpp2llvmParser.If)
            self.state = 243
            self.match(cpp2llvmParser.LeftParen)
            self.state = 244
            self.expression(0)
            self.state = 245
            self.match(cpp2llvmParser.RightParen)
            self.state = 246
            self.statement()
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 247
                self.match(cpp2llvmParser.Else)
                self.state = 248
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = cpp2llvmParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(cpp2llvmParser.Switch)
            self.state = 252
            self.match(cpp2llvmParser.LeftParen)
            self.state = 253
            self.expression(0)
            self.state = 254
            self.match(cpp2llvmParser.RightParen)
            self.state = 255
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 256
                self.caseStatement()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 262
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStatement" ):
                return visitor.visitCaseStatement(self)
            else:
                return visitor.visitChildren(self)




    def caseStatement(self):

        localctx = cpp2llvmParser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(cpp2llvmParser.Case)
            self.state = 265
            self.constExpression()
            self.state = 266
            self.match(cpp2llvmParser.Colon)
            self.state = 267
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = cpp2llvmParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(cpp2llvmParser.While)
            self.state = 270
            self.match(cpp2llvmParser.LeftParen)
            self.state = 271
            self.expression(0)
            self.state = 272
            self.match(cpp2llvmParser.RightParen)
            self.state = 273
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def doWhileStatement(self):

        localctx = cpp2llvmParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(cpp2llvmParser.Do)
            self.state = 276
            self.statement()
            self.state = 277
            self.match(cpp2llvmParser.While)
            self.state = 278
            self.match(cpp2llvmParser.LeftParen)
            self.state = 279
            self.expression(0)
            self.state = 280
            self.match(cpp2llvmParser.RightParen)
            self.state = 281
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = cpp2llvmParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(cpp2llvmParser.For)
            self.state = 284
            self.match(cpp2llvmParser.LeftParen)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 285
                self.forExprSet()


            self.state = 288
            self.match(cpp2llvmParser.Semi)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 289
                self.expression(0)


            self.state = 292
            self.match(cpp2llvmParser.Semi)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 293
                self.forExprSet()


            self.state = 296
            self.match(cpp2llvmParser.RightParen)
            self.state = 297
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExprSet" ):
                return visitor.visitForExprSet(self)
            else:
                return visitor.visitChildren(self)




    def forExprSet(self):

        localctx = cpp2llvmParser.ForExprSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forExprSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.expression(0)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 300
                self.match(cpp2llvmParser.Comma)
                self.state = 301
                self.expression(0)
                self.state = 306
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = cpp2llvmParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(cpp2llvmParser.Return)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 308
                self.expression(0)


            self.state = 311
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = cpp2llvmParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(cpp2llvmParser.Break)
            self.state = 314
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = cpp2llvmParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(cpp2llvmParser.Continue)
            self.state = 317
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = cpp2llvmParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_declaration)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.variableDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.arrayDeclarator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = cpp2llvmParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_variableDeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.typeModifier()
            self.state = 325
            self.variableDeclarationList()
            self.state = 326
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarationList" ):
                return visitor.visitVariableDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarationList(self):

        localctx = cpp2llvmParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.variableDeclaration()
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 329
                self.match(cpp2llvmParser.Comma)
                self.state = 330
                self.variableDeclaration()
                self.state = 335
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = cpp2llvmParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableDeclaration)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.varDeclWithoutInit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.varDeclWithConstInit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithoutInit" ):
                return visitor.visitVarDeclWithoutInit(self)
            else:
                return visitor.visitChildren(self)




    def varDeclWithoutInit(self):

        localctx = cpp2llvmParser.VarDeclWithoutInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_varDeclWithoutInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithConstInit" ):
                return visitor.visitVarDeclWithConstInit(self)
            else:
                return visitor.visitChildren(self)




    def varDeclWithConstInit(self):

        localctx = cpp2llvmParser.VarDeclWithConstInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_varDeclWithConstInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(cpp2llvmParser.Identifier)
            self.state = 344
            self.match(cpp2llvmParser.Assign)
            self.state = 345
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithNormalInit" ):
                return visitor.visitVarDeclWithNormalInit(self)
            else:
                return visitor.visitChildren(self)




    def varDeclWithNormalInit(self):

        localctx = cpp2llvmParser.VarDeclWithNormalInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_varDeclWithNormalInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(cpp2llvmParser.Identifier)
            self.state = 348
            self.match(cpp2llvmParser.Assign)
            self.state = 349
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclarator" ):
                return visitor.visitArrayDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclarator(self):

        localctx = cpp2llvmParser.ArrayDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arrayDeclarator)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.normalArrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalArrayDeclaration" ):
                return visitor.visitNormalArrayDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def normalArrayDeclaration(self):

        localctx = cpp2llvmParser.NormalArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_normalArrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.normalTypeModifier()
            self.state = 356
            self.arrayName()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 357
                self.match(cpp2llvmParser.Assign)
                self.state = 358
                self.match(cpp2llvmParser.LeftBrace)
                self.state = 359
                self.arrayAssginExpressionList()
                self.state = 360
                self.match(cpp2llvmParser.RightBrace)


            self.state = 364
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssginExpressionList" ):
                return visitor.visitArrayAssginExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssginExpressionList(self):

        localctx = cpp2llvmParser.ArrayAssginExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayAssginExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.expression(0)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 367
                self.match(cpp2llvmParser.Comma)
                self.state = 368
                self.expression(0)
                self.state = 373
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringDeclaration" ):
                return visitor.visitStringDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def stringDeclaration(self):

        localctx = cpp2llvmParser.StringDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stringDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.charTypeModifier()
            self.state = 375
            self.arrayName()
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 376
                self.match(cpp2llvmParser.Assign)
                self.state = 377
                self.stringLiteral()


            self.state = 380
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayName" ):
                return visitor.visitArrayName(self)
            else:
                return visitor.visitChildren(self)




    def arrayName(self):

        localctx = cpp2llvmParser.ArrayNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(cpp2llvmParser.Identifier)
            self.state = 383
            self.match(cpp2llvmParser.LeftBracket)
            self.state = 384
            self.match(cpp2llvmParser.IntegerLiteral)
            self.state = 385
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclarator" ):
                return visitor.visitFunctionDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclarator(self):

        localctx = cpp2llvmParser.FunctionDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionDeclarator)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = cpp2llvmParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.functionHead()
            self.state = 392
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = cpp2llvmParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.functionHead()
            self.state = 395
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionHead" ):
                return visitor.visitFunctionHead(self)
            else:
                return visitor.visitChildren(self)




    def functionHead(self):

        localctx = cpp2llvmParser.FunctionHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_functionHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.typeModifier()
            self.state = 398
            self.match(cpp2llvmParser.Identifier)
            self.state = 399
            self.match(cpp2llvmParser.LeftParen)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79 or _la==131:
                self.state = 400
                self.functionParameterList()


            self.state = 403
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParameterList" ):
                return visitor.visitFunctionParameterList(self)
            else:
                return visitor.visitChildren(self)




    def functionParameterList(self):

        localctx = cpp2llvmParser.FunctionParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_functionParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.functionParameter()
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 406
                self.match(cpp2llvmParser.Comma)
                self.state = 407
                self.functionParameter()
                self.state = 412
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParameter" ):
                return visitor.visitFunctionParameter(self)
            else:
                return visitor.visitChildren(self)




    def functionParameter(self):

        localctx = cpp2llvmParser.FunctionParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_functionParameter)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.pointerTypeModifier()
                self.state = 414
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.normalTypeModifier()
                self.state = 417
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 419
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeModifier" ):
                return visitor.visitTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def typeModifier(self):

        localctx = cpp2llvmParser.TypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_typeModifier)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.pointerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerTypeModifier" ):
                return visitor.visitPointerTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def pointerTypeModifier(self):

        localctx = cpp2llvmParser.PointerTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_pointerTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.normalTypeModifier()
            self.state = 427
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalTypeModifier" ):
                return visitor.visitNormalTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def normalTypeModifier(self):

        localctx = cpp2llvmParser.NormalTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_normalTypeModifier)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.integerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.realTypeModifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.boolTypeModifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
                self.charTypeModifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 433
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerTypeModifier" ):
                return visitor.visitIntegerTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def integerTypeModifier(self):

        localctx = cpp2llvmParser.IntegerTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_integerTypeModifier)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(cpp2llvmParser.Int)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(cpp2llvmParser.Long)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(cpp2llvmParser.Short)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
                self.match(cpp2llvmParser.Long)
                self.state = 440
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealTypeModifier" ):
                return visitor.visitRealTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def realTypeModifier(self):

        localctx = cpp2llvmParser.RealTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_realTypeModifier)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(cpp2llvmParser.Float)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(cpp2llvmParser.Double)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.match(cpp2llvmParser.Long)
                self.state = 446
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolTypeModifier" ):
                return visitor.visitBoolTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def boolTypeModifier(self):

        localctx = cpp2llvmParser.BoolTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_boolTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharTypeModifier" ):
                return visitor.visitCharTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def charTypeModifier(self):

        localctx = cpp2llvmParser.CharTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_charTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidTypeModifier" ):
                return visitor.visitVoidTypeModifier(self)
            else:
                return visitor.visitChildren(self)




    def voidTypeModifier(self):

        localctx = cpp2llvmParser.VoidTypeModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_voidTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
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
         




