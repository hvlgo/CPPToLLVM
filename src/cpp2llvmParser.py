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
        39,2,40,7,40,1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,1,0,1,1,1,1,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,101,8,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,132,8,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,188,8,4,10,4,12,4,191,9,4,1,5,1,5,1,5,1,5,1,5,5,5,198,8,5,10,
        5,12,5,201,9,5,3,5,203,8,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,216,8,7,1,8,3,8,219,8,8,1,8,1,8,1,9,1,9,5,9,225,8,9,10,
        9,12,9,228,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,244,8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,
        11,252,8,11,10,11,12,11,255,9,11,1,11,1,11,3,11,259,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,280,8,12,10,12,12,12,283,9,12,3,12,285,
        8,12,1,12,1,12,3,12,289,8,12,1,12,1,12,1,12,1,12,5,12,295,8,12,10,
        12,12,12,298,9,12,3,12,300,8,12,1,12,1,12,3,12,304,8,12,1,13,1,13,
        1,13,1,13,3,13,310,8,13,1,13,1,13,3,13,314,8,13,1,13,1,13,1,14,1,
        14,1,14,3,14,321,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,330,
        8,16,10,16,12,16,333,9,16,1,17,1,17,1,17,3,17,338,8,17,1,18,1,18,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,3,21,352,8,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,361,8,22,1,22,1,22,1,23,
        1,23,1,23,5,23,368,8,23,10,23,12,23,371,9,23,1,24,1,24,1,24,1,24,
        3,24,377,8,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,3,26,
        388,8,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,
        400,8,29,1,29,1,29,1,30,1,30,1,30,5,30,407,8,30,10,30,12,30,410,
        9,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,419,8,31,1,32,1,32,
        3,32,423,8,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,3,34,433,8,
        34,1,35,1,35,1,35,1,35,1,35,3,35,440,8,35,1,36,1,36,1,36,1,36,3,
        36,446,8,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,40,0,1,8,41,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,0,1,1,0,1,
        6,492,0,85,1,0,0,0,2,90,1,0,0,0,4,92,1,0,0,0,6,100,1,0,0,0,8,131,
        1,0,0,0,10,192,1,0,0,0,12,206,1,0,0,0,14,215,1,0,0,0,16,218,1,0,
        0,0,18,222,1,0,0,0,20,231,1,0,0,0,22,258,1,0,0,0,24,303,1,0,0,0,
        26,313,1,0,0,0,28,320,1,0,0,0,30,322,1,0,0,0,32,326,1,0,0,0,34,337,
        1,0,0,0,36,339,1,0,0,0,38,341,1,0,0,0,40,345,1,0,0,0,42,351,1,0,
        0,0,44,353,1,0,0,0,46,364,1,0,0,0,48,372,1,0,0,0,50,380,1,0,0,0,
        52,387,1,0,0,0,54,389,1,0,0,0,56,392,1,0,0,0,58,395,1,0,0,0,60,403,
        1,0,0,0,62,418,1,0,0,0,64,422,1,0,0,0,66,424,1,0,0,0,68,432,1,0,
        0,0,70,439,1,0,0,0,72,445,1,0,0,0,74,447,1,0,0,0,76,449,1,0,0,0,
        78,451,1,0,0,0,80,453,1,0,0,0,82,84,3,28,14,0,83,82,1,0,0,0,84,87,
        1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,
        88,89,5,0,0,1,89,1,1,0,0,0,90,91,5,4,0,0,91,3,1,0,0,0,92,93,3,80,
        40,0,93,5,1,0,0,0,94,101,5,132,0,0,95,96,5,132,0,0,96,97,5,85,0,
        0,97,98,3,8,4,0,98,99,5,86,0,0,99,101,1,0,0,0,100,94,1,0,0,0,100,
        95,1,0,0,0,101,7,1,0,0,0,102,103,6,4,-1,0,103,132,3,10,5,0,104,132,
        3,80,40,0,105,132,5,132,0,0,106,107,5,83,0,0,107,108,3,8,4,0,108,
        109,5,84,0,0,109,132,1,0,0,0,110,111,5,98,0,0,111,132,3,8,4,25,112,
        113,5,90,0,0,113,132,3,8,4,24,114,115,5,95,0,0,115,132,3,6,3,0,116,
        117,5,132,0,0,117,118,5,85,0,0,118,119,3,8,4,0,119,120,5,86,0,0,
        120,132,1,0,0,0,121,122,3,6,3,0,122,123,5,99,0,0,123,124,3,8,4,3,
        124,132,1,0,0,0,125,126,3,6,3,0,126,127,5,120,0,0,127,132,1,0,0,
        0,128,129,3,6,3,0,129,130,5,121,0,0,130,132,1,0,0,0,131,102,1,0,
        0,0,131,104,1,0,0,0,131,105,1,0,0,0,131,106,1,0,0,0,131,110,1,0,
        0,0,131,112,1,0,0,0,131,114,1,0,0,0,131,116,1,0,0,0,131,121,1,0,
        0,0,131,125,1,0,0,0,131,128,1,0,0,0,132,189,1,0,0,0,133,134,10,22,
        0,0,134,135,5,91,0,0,135,188,3,8,4,23,136,137,10,21,0,0,137,138,
        5,92,0,0,138,188,3,8,4,22,139,140,10,20,0,0,140,141,5,93,0,0,141,
        188,3,8,4,21,142,143,10,19,0,0,143,144,5,89,0,0,144,188,3,8,4,20,
        145,146,10,18,0,0,146,147,5,90,0,0,147,188,3,8,4,19,148,149,10,17,
        0,0,149,150,5,100,0,0,150,188,3,8,4,18,151,152,10,16,0,0,152,153,
        5,101,0,0,153,188,3,8,4,17,154,155,10,15,0,0,155,156,5,116,0,0,156,
        188,3,8,4,16,157,158,10,14,0,0,158,159,5,117,0,0,159,188,3,8,4,15,
        160,161,10,13,0,0,161,162,5,114,0,0,162,188,3,8,4,14,163,164,10,
        12,0,0,164,165,5,115,0,0,165,188,3,8,4,13,166,167,10,11,0,0,167,
        168,5,96,0,0,168,188,3,8,4,12,169,170,10,10,0,0,170,171,5,95,0,0,
        171,188,3,8,4,11,172,173,10,9,0,0,173,174,5,94,0,0,174,188,3,8,4,
        10,175,176,10,8,0,0,176,177,5,119,0,0,177,188,3,8,4,9,178,179,10,
        7,0,0,179,180,5,118,0,0,180,188,3,8,4,8,181,182,10,6,0,0,182,183,
        5,110,0,0,183,188,3,8,4,7,184,185,10,5,0,0,185,186,5,112,0,0,186,
        188,3,8,4,6,187,133,1,0,0,0,187,136,1,0,0,0,187,139,1,0,0,0,187,
        142,1,0,0,0,187,145,1,0,0,0,187,148,1,0,0,0,187,151,1,0,0,0,187,
        154,1,0,0,0,187,157,1,0,0,0,187,160,1,0,0,0,187,163,1,0,0,0,187,
        166,1,0,0,0,187,169,1,0,0,0,187,172,1,0,0,0,187,175,1,0,0,0,187,
        178,1,0,0,0,187,181,1,0,0,0,187,184,1,0,0,0,188,191,1,0,0,0,189,
        187,1,0,0,0,189,190,1,0,0,0,190,9,1,0,0,0,191,189,1,0,0,0,192,193,
        5,132,0,0,193,202,5,83,0,0,194,199,3,8,4,0,195,196,5,122,0,0,196,
        198,3,8,4,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,
        200,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,202,194,1,0,0,0,202,
        203,1,0,0,0,203,204,1,0,0,0,204,205,5,84,0,0,205,11,1,0,0,0,206,
        207,3,8,4,0,207,13,1,0,0,0,208,216,3,16,8,0,209,216,3,18,9,0,210,
        216,3,22,11,0,211,216,3,24,12,0,212,216,3,26,13,0,213,216,3,30,15,
        0,214,216,3,42,21,0,215,208,1,0,0,0,215,209,1,0,0,0,215,210,1,0,
        0,0,215,211,1,0,0,0,215,212,1,0,0,0,215,213,1,0,0,0,215,214,1,0,
        0,0,216,15,1,0,0,0,217,219,3,8,4,0,218,217,1,0,0,0,218,219,1,0,0,
        0,219,220,1,0,0,0,220,221,5,128,0,0,221,17,1,0,0,0,222,226,5,87,
        0,0,223,225,3,14,7,0,224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,
        0,0,226,227,1,0,0,0,227,229,1,0,0,0,228,226,1,0,0,0,229,230,5,88,
        0,0,230,19,1,0,0,0,231,232,5,14,0,0,232,233,3,4,2,0,233,234,5,126,
        0,0,234,235,3,14,7,0,235,21,1,0,0,0,236,237,5,41,0,0,237,238,5,83,
        0,0,238,239,3,12,6,0,239,240,5,84,0,0,240,243,3,14,7,0,241,242,5,
        30,0,0,242,244,3,14,7,0,243,241,1,0,0,0,243,244,1,0,0,0,244,259,
        1,0,0,0,245,246,5,65,0,0,246,247,5,83,0,0,247,248,3,12,6,0,248,249,
        5,84,0,0,249,253,5,87,0,0,250,252,3,20,10,0,251,250,1,0,0,0,252,
        255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,
        253,1,0,0,0,256,257,5,88,0,0,257,259,1,0,0,0,258,236,1,0,0,0,258,
        245,1,0,0,0,259,23,1,0,0,0,260,261,5,82,0,0,261,262,5,83,0,0,262,
        263,3,12,6,0,263,264,5,84,0,0,264,265,3,14,7,0,265,304,1,0,0,0,266,
        267,5,27,0,0,267,268,3,14,7,0,268,269,5,82,0,0,269,270,5,83,0,0,
        270,271,3,8,4,0,271,272,5,84,0,0,272,273,5,128,0,0,273,304,1,0,0,
        0,274,275,5,38,0,0,275,284,5,83,0,0,276,281,3,8,4,0,277,278,5,122,
        0,0,278,280,3,8,4,0,279,277,1,0,0,0,280,283,1,0,0,0,281,279,1,0,
        0,0,281,282,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,284,276,1,0,
        0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,288,5,128,0,0,287,289,3,
        8,4,0,288,287,1,0,0,0,288,289,1,0,0,0,289,290,1,0,0,0,290,299,5,
        128,0,0,291,296,3,8,4,0,292,293,5,122,0,0,293,295,3,8,4,0,294,292,
        1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,300,
        1,0,0,0,298,296,1,0,0,0,299,291,1,0,0,0,299,300,1,0,0,0,300,301,
        1,0,0,0,301,302,5,84,0,0,302,304,3,14,7,0,303,260,1,0,0,0,303,266,
        1,0,0,0,303,274,1,0,0,0,304,25,1,0,0,0,305,314,5,13,0,0,306,314,
        5,23,0,0,307,309,5,57,0,0,308,310,3,8,4,0,309,308,1,0,0,0,309,310,
        1,0,0,0,310,314,1,0,0,0,311,312,5,40,0,0,312,314,5,132,0,0,313,305,
        1,0,0,0,313,306,1,0,0,0,313,307,1,0,0,0,313,311,1,0,0,0,314,315,
        1,0,0,0,315,316,5,128,0,0,316,27,1,0,0,0,317,321,3,30,15,0,318,321,
        3,42,21,0,319,321,3,52,26,0,320,317,1,0,0,0,320,318,1,0,0,0,320,
        319,1,0,0,0,321,29,1,0,0,0,322,323,3,64,32,0,323,324,3,32,16,0,324,
        325,5,128,0,0,325,31,1,0,0,0,326,331,3,34,17,0,327,328,5,122,0,0,
        328,330,3,34,17,0,329,327,1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,
        0,331,332,1,0,0,0,332,33,1,0,0,0,333,331,1,0,0,0,334,338,3,36,18,
        0,335,338,3,38,19,0,336,338,3,40,20,0,337,334,1,0,0,0,337,335,1,
        0,0,0,337,336,1,0,0,0,338,35,1,0,0,0,339,340,5,132,0,0,340,37,1,
        0,0,0,341,342,5,132,0,0,342,343,5,99,0,0,343,344,3,4,2,0,344,39,
        1,0,0,0,345,346,5,132,0,0,346,347,5,99,0,0,347,348,3,8,4,0,348,41,
        1,0,0,0,349,352,3,44,22,0,350,352,3,48,24,0,351,349,1,0,0,0,351,
        350,1,0,0,0,352,43,1,0,0,0,353,354,3,68,34,0,354,360,3,50,25,0,355,
        356,5,99,0,0,356,357,5,87,0,0,357,358,3,46,23,0,358,359,5,88,0,0,
        359,361,1,0,0,0,360,355,1,0,0,0,360,361,1,0,0,0,361,362,1,0,0,0,
        362,363,5,128,0,0,363,45,1,0,0,0,364,369,3,8,4,0,365,366,5,122,0,
        0,366,368,3,8,4,0,367,365,1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,
        0,369,370,1,0,0,0,370,47,1,0,0,0,371,369,1,0,0,0,372,373,3,76,38,
        0,373,376,3,50,25,0,374,375,5,99,0,0,375,377,3,2,1,0,376,374,1,0,
        0,0,376,377,1,0,0,0,377,378,1,0,0,0,378,379,5,128,0,0,379,49,1,0,
        0,0,380,381,5,132,0,0,381,382,5,85,0,0,382,383,5,133,0,0,383,384,
        5,86,0,0,384,51,1,0,0,0,385,388,3,54,27,0,386,388,3,56,28,0,387,
        385,1,0,0,0,387,386,1,0,0,0,388,53,1,0,0,0,389,390,3,58,29,0,390,
        391,5,128,0,0,391,55,1,0,0,0,392,393,3,58,29,0,393,394,3,18,9,0,
        394,57,1,0,0,0,395,396,3,64,32,0,396,397,5,132,0,0,397,399,5,83,
        0,0,398,400,3,60,30,0,399,398,1,0,0,0,399,400,1,0,0,0,400,401,1,
        0,0,0,401,402,5,84,0,0,402,59,1,0,0,0,403,408,3,62,31,0,404,405,
        5,122,0,0,405,407,3,62,31,0,406,404,1,0,0,0,407,410,1,0,0,0,408,
        406,1,0,0,0,408,409,1,0,0,0,409,61,1,0,0,0,410,408,1,0,0,0,411,412,
        3,66,33,0,412,413,5,132,0,0,413,419,1,0,0,0,414,415,3,68,34,0,415,
        416,5,132,0,0,416,419,1,0,0,0,417,419,5,131,0,0,418,411,1,0,0,0,
        418,414,1,0,0,0,418,417,1,0,0,0,419,63,1,0,0,0,420,423,3,66,33,0,
        421,423,3,68,34,0,422,420,1,0,0,0,422,421,1,0,0,0,423,65,1,0,0,0,
        424,425,3,68,34,0,425,426,5,91,0,0,426,67,1,0,0,0,427,433,3,70,35,
        0,428,433,3,72,36,0,429,433,3,74,37,0,430,433,3,76,38,0,431,433,
        3,78,39,0,432,427,1,0,0,0,432,428,1,0,0,0,432,429,1,0,0,0,432,430,
        1,0,0,0,432,431,1,0,0,0,433,69,1,0,0,0,434,440,5,43,0,0,435,440,
        5,44,0,0,436,440,5,58,0,0,437,438,5,44,0,0,438,440,5,44,0,0,439,
        434,1,0,0,0,439,435,1,0,0,0,439,436,1,0,0,0,439,437,1,0,0,0,440,
        71,1,0,0,0,441,446,5,37,0,0,442,446,5,28,0,0,443,444,5,44,0,0,444,
        446,5,28,0,0,445,441,1,0,0,0,445,442,1,0,0,0,445,443,1,0,0,0,446,
        73,1,0,0,0,447,448,5,12,0,0,448,75,1,0,0,0,449,450,5,16,0,0,450,
        77,1,0,0,0,451,452,5,79,0,0,452,79,1,0,0,0,453,454,7,0,0,0,454,81,
        1,0,0,0,36,85,100,131,187,189,199,202,215,218,226,243,253,258,281,
        284,288,296,299,303,309,313,320,331,337,351,360,369,376,387,399,
        408,418,422,432,439,445
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
    RULE_stringLiteral = 1
    RULE_constExpression = 2
    RULE_leftExpression = 3
    RULE_expression = 4
    RULE_functionCall = 5
    RULE_condition = 6
    RULE_statement = 7
    RULE_expressionStatement = 8
    RULE_compoundStatement = 9
    RULE_caseStatement = 10
    RULE_selectionStatement = 11
    RULE_iterationStatement = 12
    RULE_jumpStatement = 13
    RULE_declaration = 14
    RULE_variableDeclarator = 15
    RULE_variableDeclarationList = 16
    RULE_variableDeclaration = 17
    RULE_varDeclWithoutInit = 18
    RULE_varDeclWithConstInit = 19
    RULE_varDeclWithNormalInit = 20
    RULE_arrayDeclarator = 21
    RULE_normalArrayDeclaration = 22
    RULE_arrayAssginExpressionList = 23
    RULE_stringDeclaration = 24
    RULE_arrayName = 25
    RULE_functionDeclarator = 26
    RULE_functionDeclaration = 27
    RULE_functionDefinition = 28
    RULE_functionHead = 29
    RULE_functionParameterList = 30
    RULE_functionParameter = 31
    RULE_typeModifier = 32
    RULE_pointerTypeModifier = 33
    RULE_normalTypeModifier = 34
    RULE_integerTypeModifier = 35
    RULE_realTypeModifier = 36
    RULE_boolTypeModifier = 37
    RULE_charTypeModifier = 38
    RULE_voidTypeModifier = 39
    RULE_literal = 40

    ruleNames =  [ "translationUnit", "stringLiteral", "constExpression", 
                   "leftExpression", "expression", "functionCall", "condition", 
                   "statement", "expressionStatement", "compoundStatement", 
                   "caseStatement", "selectionStatement", "iterationStatement", 
                   "jumpStatement", "declaration", "variableDeclarator", 
                   "variableDeclarationList", "variableDeclaration", "varDeclWithoutInit", 
                   "varDeclWithConstInit", "varDeclWithNormalInit", "arrayDeclarator", 
                   "normalArrayDeclaration", "arrayAssginExpressionList", 
                   "stringDeclaration", "arrayName", "functionDeclarator", 
                   "functionDeclaration", "functionDefinition", "functionHead", 
                   "functionParameterList", "functionParameter", "typeModifier", 
                   "pointerTypeModifier", "normalTypeModifier", "integerTypeModifier", 
                   "realTypeModifier", "boolTypeModifier", "charTypeModifier", 
                   "voidTypeModifier", "literal" ]

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
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79:
                self.state = 82
                self.declaration()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(cpp2llvmParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
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
        self.enterRule(localctx, 4, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
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
        self.enterRule(localctx, 6, self.RULE_leftExpression)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(cpp2llvmParser.Identifier)

                self.state = 96
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 97
                self.expression(0)
                self.state = 98
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 103
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 104
                self.literal()
                pass

            elif la_ == 3:
                self.state = 105
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 4:
                self.state = 106
                self.match(cpp2llvmParser.LeftParen)
                self.state = 107
                self.expression(0)
                self.state = 108
                self.match(cpp2llvmParser.RightParen)
                pass

            elif la_ == 5:
                self.state = 110
                self.match(cpp2llvmParser.Not)
                self.state = 111
                self.expression(25)
                pass

            elif la_ == 6:
                self.state = 112
                self.match(cpp2llvmParser.Minus)
                self.state = 113
                self.expression(24)
                pass

            elif la_ == 7:
                self.state = 114
                self.match(cpp2llvmParser.And)
                self.state = 115
                self.leftExpression()
                pass

            elif la_ == 8:
                self.state = 116
                self.match(cpp2llvmParser.Identifier)
                self.state = 117
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 118
                self.expression(0)
                self.state = 119
                self.match(cpp2llvmParser.RightBracket)
                pass

            elif la_ == 9:
                self.state = 121
                self.leftExpression()
                self.state = 122
                self.match(cpp2llvmParser.Assign)
                self.state = 123
                self.expression(3)
                pass

            elif la_ == 10:
                self.state = 125
                self.leftExpression()
                self.state = 126
                self.match(cpp2llvmParser.PlusPlus)
                pass

            elif la_ == 11:
                self.state = 128
                self.leftExpression()
                self.state = 129
                self.match(cpp2llvmParser.MinusMinus)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 187
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 133
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 134
                        self.match(cpp2llvmParser.Star)
                        self.state = 135
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 136
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 137
                        self.match(cpp2llvmParser.Div)
                        self.state = 138
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 140
                        self.match(cpp2llvmParser.Mod)
                        self.state = 141
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 143
                        self.match(cpp2llvmParser.Plus)
                        self.state = 144
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 146
                        self.match(cpp2llvmParser.Minus)
                        self.state = 147
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 149
                        self.match(cpp2llvmParser.Less)
                        self.state = 150
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 152
                        self.match(cpp2llvmParser.Greater)
                        self.state = 153
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 155
                        self.match(cpp2llvmParser.LessEqual)
                        self.state = 156
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 158
                        self.match(cpp2llvmParser.GreaterEqual)
                        self.state = 159
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 161
                        self.match(cpp2llvmParser.Equal)
                        self.state = 162
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 164
                        self.match(cpp2llvmParser.NotEqual)
                        self.state = 165
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 167
                        self.match(cpp2llvmParser.Or)
                        self.state = 168
                        self.expression(12)
                        pass

                    elif la_ == 13:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 170
                        self.match(cpp2llvmParser.And)
                        self.state = 171
                        self.expression(11)
                        pass

                    elif la_ == 14:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 173
                        self.match(cpp2llvmParser.Caret)
                        self.state = 174
                        self.expression(10)
                        pass

                    elif la_ == 15:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 176
                        self.match(cpp2llvmParser.OrOr)
                        self.state = 177
                        self.expression(9)
                        pass

                    elif la_ == 16:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 178
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 179
                        self.match(cpp2llvmParser.AndAnd)
                        self.state = 180
                        self.expression(8)
                        pass

                    elif la_ == 17:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 182
                        self.match(cpp2llvmParser.LeftShift)
                        self.state = 183
                        self.expression(7)
                        pass

                    elif la_ == 18:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 185
                        self.match(cpp2llvmParser.RightShift)
                        self.state = 186
                        self.expression(6)
                        pass

             
                self.state = 191
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
        self.enterRule(localctx, 10, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(cpp2llvmParser.Identifier)
            self.state = 193
            self.match(cpp2llvmParser.LeftParen)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 194
                self.expression(0)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==122:
                    self.state = 195
                    self.match(cpp2llvmParser.Comma)
                    self.state = 196
                    self.expression(0)
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 204
            self.match(cpp2llvmParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = cpp2llvmParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expression(0)
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


        def selectionStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.SelectionStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.IterationStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(cpp2llvmParser.JumpStatementContext,0)


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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.selectionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.iterationStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.jumpStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.variableDeclarator()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.arrayDeclarator()
                pass


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
        self.enterRule(localctx, 16, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 217
                self.expression(0)


            self.state = 220
            self.match(cpp2llvmParser.Semi)
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
        self.enterRule(localctx, 18, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 432375663769497726) != 0 or (((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & -9223372027152941055) != 0 or _la==132:
                self.state = 223
                self.statement()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
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
        self.enterRule(localctx, 20, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(cpp2llvmParser.Case)
            self.state = 232
            self.constExpression()
            self.state = 233
            self.match(cpp2llvmParser.Colon)
            self.state = 234
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(cpp2llvmParser.If, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def condition(self):
            return self.getTypedRuleContext(cpp2llvmParser.ConditionContext,0)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.StatementContext,i)


        def Else(self):
            return self.getToken(cpp2llvmParser.Else, 0)

        def Switch(self):
            return self.getToken(cpp2llvmParser.Switch, 0)

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
            return cpp2llvmParser.RULE_selectionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionStatement" ):
                listener.enterSelectionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionStatement" ):
                listener.exitSelectionStatement(self)




    def selectionStatement(self):

        localctx = cpp2llvmParser.SelectionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_selectionStatement)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(cpp2llvmParser.If)
                self.state = 237
                self.match(cpp2llvmParser.LeftParen)
                self.state = 238
                self.condition()
                self.state = 239
                self.match(cpp2llvmParser.RightParen)
                self.state = 240
                self.statement()
                self.state = 243
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 241
                    self.match(cpp2llvmParser.Else)
                    self.state = 242
                    self.statement()


                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(cpp2llvmParser.Switch)
                self.state = 246
                self.match(cpp2llvmParser.LeftParen)
                self.state = 247
                self.condition()
                self.state = 248
                self.match(cpp2llvmParser.RightParen)
                self.state = 249
                self.match(cpp2llvmParser.LeftBrace)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 250
                    self.caseStatement()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
                self.match(cpp2llvmParser.RightBrace)
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


    class IterationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(cpp2llvmParser.While, 0)

        def LeftParen(self):
            return self.getToken(cpp2llvmParser.LeftParen, 0)

        def condition(self):
            return self.getTypedRuleContext(cpp2llvmParser.ConditionContext,0)


        def RightParen(self):
            return self.getToken(cpp2llvmParser.RightParen, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp2llvmParser.StatementContext,0)


        def Do(self):
            return self.getToken(cpp2llvmParser.Do, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp2llvmParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,i)


        def Semi(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Semi)
            else:
                return self.getToken(cpp2llvmParser.Semi, i)

        def For(self):
            return self.getToken(cpp2llvmParser.For, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(cpp2llvmParser.Comma)
            else:
                return self.getToken(cpp2llvmParser.Comma, i)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_iterationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterationStatement" ):
                listener.enterIterationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterationStatement" ):
                listener.exitIterationStatement(self)




    def iterationStatement(self):

        localctx = cpp2llvmParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [82]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(cpp2llvmParser.While)
                self.state = 261
                self.match(cpp2llvmParser.LeftParen)
                self.state = 262
                self.condition()
                self.state = 263
                self.match(cpp2llvmParser.RightParen)
                self.state = 264
                self.statement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(cpp2llvmParser.Do)
                self.state = 267
                self.statement()
                self.state = 268
                self.match(cpp2llvmParser.While)
                self.state = 269
                self.match(cpp2llvmParser.LeftParen)
                self.state = 270
                self.expression(0)
                self.state = 271
                self.match(cpp2llvmParser.RightParen)
                self.state = 272
                self.match(cpp2llvmParser.Semi)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.match(cpp2llvmParser.For)
                self.state = 275
                self.match(cpp2llvmParser.LeftParen)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                    self.state = 276
                    self.expression(0)
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==122:
                        self.state = 277
                        self.match(cpp2llvmParser.Comma)
                        self.state = 278
                        self.expression(0)
                        self.state = 283
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 286
                self.match(cpp2llvmParser.Semi)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                    self.state = 287
                    self.expression(0)


                self.state = 290
                self.match(cpp2llvmParser.Semi)
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                    self.state = 291
                    self.expression(0)
                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==122:
                        self.state = 292
                        self.match(cpp2llvmParser.Comma)
                        self.state = 293
                        self.expression(0)
                        self.state = 298
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 301
                self.match(cpp2llvmParser.RightParen)
                self.state = 302
                self.statement()
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


    class JumpStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(cpp2llvmParser.Semi, 0)

        def Break(self):
            return self.getToken(cpp2llvmParser.Break, 0)

        def Continue(self):
            return self.getToken(cpp2llvmParser.Continue, 0)

        def Return(self):
            return self.getToken(cpp2llvmParser.Return, 0)

        def Goto(self):
            return self.getToken(cpp2llvmParser.Goto, 0)

        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp2llvmParser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp2llvmParser.RULE_jumpStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpStatement" ):
                listener.enterJumpStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpStatement" ):
                listener.exitJumpStatement(self)




    def jumpStatement(self):

        localctx = cpp2llvmParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 305
                self.match(cpp2llvmParser.Break)
                pass
            elif token in [23]:
                self.state = 306
                self.match(cpp2llvmParser.Continue)
                pass
            elif token in [57]:
                self.state = 307
                self.match(cpp2llvmParser.Return)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                    self.state = 308
                    self.expression(0)


                pass
            elif token in [40]:
                self.state = 311
                self.match(cpp2llvmParser.Goto)
                self.state = 312
                self.match(cpp2llvmParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 315
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
        self.enterRule(localctx, 28, self.RULE_declaration)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.variableDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.arrayDeclarator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
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
        self.enterRule(localctx, 30, self.RULE_variableDeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.typeModifier()
            self.state = 323
            self.variableDeclarationList()
            self.state = 324
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
        self.enterRule(localctx, 32, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.variableDeclaration()
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 327
                self.match(cpp2llvmParser.Comma)
                self.state = 328
                self.variableDeclaration()
                self.state = 333
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
        self.enterRule(localctx, 34, self.RULE_variableDeclaration)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.varDeclWithoutInit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.varDeclWithConstInit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
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
        self.enterRule(localctx, 36, self.RULE_varDeclWithoutInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
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
        self.enterRule(localctx, 38, self.RULE_varDeclWithConstInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(cpp2llvmParser.Identifier)
            self.state = 342
            self.match(cpp2llvmParser.Assign)
            self.state = 343
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
        self.enterRule(localctx, 40, self.RULE_varDeclWithNormalInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(cpp2llvmParser.Identifier)
            self.state = 346
            self.match(cpp2llvmParser.Assign)
            self.state = 347
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
        self.enterRule(localctx, 42, self.RULE_arrayDeclarator)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.normalArrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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
        self.enterRule(localctx, 44, self.RULE_normalArrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.normalTypeModifier()
            self.state = 354
            self.arrayName()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 355
                self.match(cpp2llvmParser.Assign)
                self.state = 356
                self.match(cpp2llvmParser.LeftBrace)
                self.state = 357
                self.arrayAssginExpressionList()
                self.state = 358
                self.match(cpp2llvmParser.RightBrace)


            self.state = 362
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
        self.enterRule(localctx, 46, self.RULE_arrayAssginExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.expression(0)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 365
                self.match(cpp2llvmParser.Comma)
                self.state = 366
                self.expression(0)
                self.state = 371
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
        self.enterRule(localctx, 48, self.RULE_stringDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.charTypeModifier()
            self.state = 373
            self.arrayName()
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 374
                self.match(cpp2llvmParser.Assign)
                self.state = 375
                self.stringLiteral()


            self.state = 378
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

        def DecimalLiteral(self):
            return self.getToken(cpp2llvmParser.DecimalLiteral, 0)

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
        self.enterRule(localctx, 50, self.RULE_arrayName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(cpp2llvmParser.Identifier)
            self.state = 381
            self.match(cpp2llvmParser.LeftBracket)
            self.state = 382
            self.match(cpp2llvmParser.DecimalLiteral)
            self.state = 383
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
        self.enterRule(localctx, 52, self.RULE_functionDeclarator)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
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
        self.enterRule(localctx, 54, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.functionHead()
            self.state = 390
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
        self.enterRule(localctx, 56, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.functionHead()
            self.state = 393
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
        self.enterRule(localctx, 58, self.RULE_functionHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.typeModifier()
            self.state = 396
            self.match(cpp2llvmParser.Identifier)
            self.state = 397
            self.match(cpp2llvmParser.LeftParen)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79 or _la==131:
                self.state = 398
                self.functionParameterList()


            self.state = 401
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
        self.enterRule(localctx, 60, self.RULE_functionParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.functionParameter()
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 404
                self.match(cpp2llvmParser.Comma)
                self.state = 405
                self.functionParameter()
                self.state = 410
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
        self.enterRule(localctx, 62, self.RULE_functionParameter)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.pointerTypeModifier()
                self.state = 412
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.normalTypeModifier()
                self.state = 415
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
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
        self.enterRule(localctx, 64, self.RULE_typeModifier)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.pointerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
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
        self.enterRule(localctx, 66, self.RULE_pointerTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.normalTypeModifier()
            self.state = 425
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
        self.enterRule(localctx, 68, self.RULE_normalTypeModifier)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.integerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.realTypeModifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.boolTypeModifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.charTypeModifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
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
        self.enterRule(localctx, 70, self.RULE_integerTypeModifier)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(cpp2llvmParser.Int)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(cpp2llvmParser.Long)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.match(cpp2llvmParser.Short)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
                self.match(cpp2llvmParser.Long)
                self.state = 438
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
        self.enterRule(localctx, 72, self.RULE_realTypeModifier)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(cpp2llvmParser.Float)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.match(cpp2llvmParser.Double)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                self.match(cpp2llvmParser.Long)
                self.state = 444
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
        self.enterRule(localctx, 74, self.RULE_boolTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
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
        self.enterRule(localctx, 76, self.RULE_charTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
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
        self.enterRule(localctx, 78, self.RULE_voidTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(cpp2llvmParser.Void)
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
        self.enterRule(localctx, 80, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expression_sempred
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
         




