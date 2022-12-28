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
        4,1,141,469,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,1,0,5,0,98,8,0,10,0,12,0,101,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,109,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,127,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,3,8,158,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,214,
        8,8,10,8,12,8,217,9,8,1,9,1,9,1,9,1,9,1,9,5,9,224,8,9,10,9,12,9,
        227,9,9,3,9,229,8,9,1,9,1,9,1,10,3,10,234,8,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,248,8,10,1,11,1,
        11,5,11,252,8,11,10,11,12,11,255,9,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,266,8,12,1,13,1,13,1,13,1,13,1,13,1,13,5,
        13,274,8,13,10,13,12,13,277,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,
        14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,17,1,17,1,17,3,17,303,8,17,1,17,1,17,3,17,307,8,17,1,17,
        1,17,3,17,311,8,17,1,17,1,17,1,17,1,18,1,18,1,18,5,18,319,8,18,10,
        18,12,18,322,9,18,1,19,1,19,3,19,326,8,19,1,19,1,19,1,20,1,20,1,
        20,1,21,1,21,1,21,1,22,1,22,1,22,3,22,339,8,22,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,5,24,348,8,24,10,24,12,24,351,9,24,1,25,1,25,1,
        25,3,25,356,8,25,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,1,29,1,29,3,29,370,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,
        30,379,8,30,1,30,1,30,1,31,1,31,1,31,5,31,386,8,31,10,31,12,31,389,
        9,31,1,32,1,32,1,32,1,32,3,32,395,8,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,34,1,34,3,34,406,8,34,1,35,1,35,1,35,1,36,1,36,1,36,
        1,37,1,37,1,37,1,37,3,37,418,8,37,1,37,1,37,1,38,1,38,1,38,5,38,
        425,8,38,10,38,12,38,428,9,38,1,39,1,39,1,39,1,39,3,39,434,8,39,
        1,40,1,40,3,40,438,8,40,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,
        3,42,448,8,42,1,43,1,43,1,43,1,43,1,43,3,43,455,8,43,1,44,1,44,1,
        44,1,44,3,44,461,8,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,0,1,16,
        48,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,94,0,0,498,0,99,1,0,0,0,2,108,1,0,0,0,4,110,1,0,0,0,6,112,
        1,0,0,0,8,114,1,0,0,0,10,116,1,0,0,0,12,118,1,0,0,0,14,126,1,0,0,
        0,16,157,1,0,0,0,18,218,1,0,0,0,20,247,1,0,0,0,22,249,1,0,0,0,24,
        258,1,0,0,0,26,267,1,0,0,0,28,280,1,0,0,0,30,285,1,0,0,0,32,291,
        1,0,0,0,34,299,1,0,0,0,36,315,1,0,0,0,38,323,1,0,0,0,40,329,1,0,
        0,0,42,332,1,0,0,0,44,338,1,0,0,0,46,340,1,0,0,0,48,344,1,0,0,0,
        50,355,1,0,0,0,52,357,1,0,0,0,54,359,1,0,0,0,56,363,1,0,0,0,58,369,
        1,0,0,0,60,371,1,0,0,0,62,382,1,0,0,0,64,390,1,0,0,0,66,398,1,0,
        0,0,68,405,1,0,0,0,70,407,1,0,0,0,72,410,1,0,0,0,74,413,1,0,0,0,
        76,421,1,0,0,0,78,433,1,0,0,0,80,437,1,0,0,0,82,439,1,0,0,0,84,447,
        1,0,0,0,86,454,1,0,0,0,88,460,1,0,0,0,90,462,1,0,0,0,92,464,1,0,
        0,0,94,466,1,0,0,0,96,98,3,44,22,0,97,96,1,0,0,0,98,101,1,0,0,0,
        99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,
        103,5,0,0,1,103,1,1,0,0,0,104,109,3,4,2,0,105,109,3,6,3,0,106,109,
        3,8,4,0,107,109,3,10,5,0,108,104,1,0,0,0,108,105,1,0,0,0,108,106,
        1,0,0,0,108,107,1,0,0,0,109,3,1,0,0,0,110,111,5,1,0,0,111,5,1,0,
        0,0,112,113,5,2,0,0,113,7,1,0,0,0,114,115,5,3,0,0,115,9,1,0,0,0,
        116,117,5,4,0,0,117,11,1,0,0,0,118,119,3,2,1,0,119,13,1,0,0,0,120,
        127,5,132,0,0,121,122,5,132,0,0,122,123,5,85,0,0,123,124,3,16,8,
        0,124,125,5,86,0,0,125,127,1,0,0,0,126,120,1,0,0,0,126,121,1,0,0,
        0,127,15,1,0,0,0,128,129,6,8,-1,0,129,158,3,18,9,0,130,158,3,2,1,
        0,131,158,5,132,0,0,132,133,5,83,0,0,133,134,3,16,8,0,134,135,5,
        84,0,0,135,158,1,0,0,0,136,137,5,98,0,0,137,158,3,16,8,25,138,139,
        5,90,0,0,139,158,3,16,8,24,140,141,5,95,0,0,141,158,3,14,7,0,142,
        143,5,132,0,0,143,144,5,85,0,0,144,145,3,16,8,0,145,146,5,86,0,0,
        146,158,1,0,0,0,147,148,3,14,7,0,148,149,5,99,0,0,149,150,3,16,8,
        3,150,158,1,0,0,0,151,152,3,14,7,0,152,153,5,120,0,0,153,158,1,0,
        0,0,154,155,3,14,7,0,155,156,5,121,0,0,156,158,1,0,0,0,157,128,1,
        0,0,0,157,130,1,0,0,0,157,131,1,0,0,0,157,132,1,0,0,0,157,136,1,
        0,0,0,157,138,1,0,0,0,157,140,1,0,0,0,157,142,1,0,0,0,157,147,1,
        0,0,0,157,151,1,0,0,0,157,154,1,0,0,0,158,215,1,0,0,0,159,160,10,
        22,0,0,160,161,5,91,0,0,161,214,3,16,8,23,162,163,10,21,0,0,163,
        164,5,92,0,0,164,214,3,16,8,22,165,166,10,20,0,0,166,167,5,93,0,
        0,167,214,3,16,8,21,168,169,10,19,0,0,169,170,5,89,0,0,170,214,3,
        16,8,20,171,172,10,18,0,0,172,173,5,90,0,0,173,214,3,16,8,19,174,
        175,10,17,0,0,175,176,5,100,0,0,176,214,3,16,8,18,177,178,10,16,
        0,0,178,179,5,101,0,0,179,214,3,16,8,17,180,181,10,15,0,0,181,182,
        5,116,0,0,182,214,3,16,8,16,183,184,10,14,0,0,184,185,5,117,0,0,
        185,214,3,16,8,15,186,187,10,13,0,0,187,188,5,114,0,0,188,214,3,
        16,8,14,189,190,10,12,0,0,190,191,5,115,0,0,191,214,3,16,8,13,192,
        193,10,11,0,0,193,194,5,96,0,0,194,214,3,16,8,12,195,196,10,10,0,
        0,196,197,5,95,0,0,197,214,3,16,8,11,198,199,10,9,0,0,199,200,5,
        94,0,0,200,214,3,16,8,10,201,202,10,8,0,0,202,203,5,119,0,0,203,
        214,3,16,8,9,204,205,10,7,0,0,205,206,5,118,0,0,206,214,3,16,8,8,
        207,208,10,6,0,0,208,209,5,110,0,0,209,214,3,16,8,7,210,211,10,5,
        0,0,211,212,5,112,0,0,212,214,3,16,8,6,213,159,1,0,0,0,213,162,1,
        0,0,0,213,165,1,0,0,0,213,168,1,0,0,0,213,171,1,0,0,0,213,174,1,
        0,0,0,213,177,1,0,0,0,213,180,1,0,0,0,213,183,1,0,0,0,213,186,1,
        0,0,0,213,189,1,0,0,0,213,192,1,0,0,0,213,195,1,0,0,0,213,198,1,
        0,0,0,213,201,1,0,0,0,213,204,1,0,0,0,213,207,1,0,0,0,213,210,1,
        0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,17,1,0,
        0,0,217,215,1,0,0,0,218,219,5,132,0,0,219,228,5,83,0,0,220,225,3,
        16,8,0,221,222,5,122,0,0,222,224,3,16,8,0,223,221,1,0,0,0,224,227,
        1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,229,1,0,0,0,227,225,
        1,0,0,0,228,220,1,0,0,0,228,229,1,0,0,0,229,230,1,0,0,0,230,231,
        5,84,0,0,231,19,1,0,0,0,232,234,3,16,8,0,233,232,1,0,0,0,233,234,
        1,0,0,0,234,235,1,0,0,0,235,248,5,128,0,0,236,248,3,22,11,0,237,
        248,3,24,12,0,238,248,3,26,13,0,239,248,3,30,15,0,240,248,3,32,16,
        0,241,248,3,34,17,0,242,248,3,38,19,0,243,248,3,40,20,0,244,248,
        3,42,21,0,245,248,3,46,23,0,246,248,3,58,29,0,247,233,1,0,0,0,247,
        236,1,0,0,0,247,237,1,0,0,0,247,238,1,0,0,0,247,239,1,0,0,0,247,
        240,1,0,0,0,247,241,1,0,0,0,247,242,1,0,0,0,247,243,1,0,0,0,247,
        244,1,0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,21,1,0,0,0,249,253,
        5,87,0,0,250,252,3,20,10,0,251,250,1,0,0,0,252,255,1,0,0,0,253,251,
        1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,253,1,0,0,0,256,257,
        5,88,0,0,257,23,1,0,0,0,258,259,5,41,0,0,259,260,5,83,0,0,260,261,
        3,16,8,0,261,262,5,84,0,0,262,265,3,20,10,0,263,264,5,30,0,0,264,
        266,3,20,10,0,265,263,1,0,0,0,265,266,1,0,0,0,266,25,1,0,0,0,267,
        268,5,65,0,0,268,269,5,83,0,0,269,270,3,16,8,0,270,271,5,84,0,0,
        271,275,5,87,0,0,272,274,3,28,14,0,273,272,1,0,0,0,274,277,1,0,0,
        0,275,273,1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,0,277,275,1,0,0,
        0,278,279,5,88,0,0,279,27,1,0,0,0,280,281,5,14,0,0,281,282,3,12,
        6,0,282,283,5,126,0,0,283,284,3,20,10,0,284,29,1,0,0,0,285,286,5,
        82,0,0,286,287,5,83,0,0,287,288,3,16,8,0,288,289,5,84,0,0,289,290,
        3,20,10,0,290,31,1,0,0,0,291,292,5,27,0,0,292,293,3,20,10,0,293,
        294,5,82,0,0,294,295,5,83,0,0,295,296,3,16,8,0,296,297,5,84,0,0,
        297,298,5,128,0,0,298,33,1,0,0,0,299,300,5,38,0,0,300,302,5,83,0,
        0,301,303,3,36,18,0,302,301,1,0,0,0,302,303,1,0,0,0,303,304,1,0,
        0,0,304,306,5,128,0,0,305,307,3,16,8,0,306,305,1,0,0,0,306,307,1,
        0,0,0,307,308,1,0,0,0,308,310,5,128,0,0,309,311,3,36,18,0,310,309,
        1,0,0,0,310,311,1,0,0,0,311,312,1,0,0,0,312,313,5,84,0,0,313,314,
        3,20,10,0,314,35,1,0,0,0,315,320,3,16,8,0,316,317,5,122,0,0,317,
        319,3,16,8,0,318,316,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,320,
        321,1,0,0,0,321,37,1,0,0,0,322,320,1,0,0,0,323,325,5,57,0,0,324,
        326,3,16,8,0,325,324,1,0,0,0,325,326,1,0,0,0,326,327,1,0,0,0,327,
        328,5,128,0,0,328,39,1,0,0,0,329,330,5,13,0,0,330,331,5,128,0,0,
        331,41,1,0,0,0,332,333,5,23,0,0,333,334,5,128,0,0,334,43,1,0,0,0,
        335,339,3,46,23,0,336,339,3,58,29,0,337,339,3,68,34,0,338,335,1,
        0,0,0,338,336,1,0,0,0,338,337,1,0,0,0,339,45,1,0,0,0,340,341,3,80,
        40,0,341,342,3,48,24,0,342,343,5,128,0,0,343,47,1,0,0,0,344,349,
        3,50,25,0,345,346,5,122,0,0,346,348,3,50,25,0,347,345,1,0,0,0,348,
        351,1,0,0,0,349,347,1,0,0,0,349,350,1,0,0,0,350,49,1,0,0,0,351,349,
        1,0,0,0,352,356,3,52,26,0,353,356,3,54,27,0,354,356,3,56,28,0,355,
        352,1,0,0,0,355,353,1,0,0,0,355,354,1,0,0,0,356,51,1,0,0,0,357,358,
        5,132,0,0,358,53,1,0,0,0,359,360,5,132,0,0,360,361,5,99,0,0,361,
        362,3,12,6,0,362,55,1,0,0,0,363,364,5,132,0,0,364,365,5,99,0,0,365,
        366,3,16,8,0,366,57,1,0,0,0,367,370,3,60,30,0,368,370,3,64,32,0,
        369,367,1,0,0,0,369,368,1,0,0,0,370,59,1,0,0,0,371,372,3,84,42,0,
        372,378,3,66,33,0,373,374,5,99,0,0,374,375,5,87,0,0,375,376,3,62,
        31,0,376,377,5,88,0,0,377,379,1,0,0,0,378,373,1,0,0,0,378,379,1,
        0,0,0,379,380,1,0,0,0,380,381,5,128,0,0,381,61,1,0,0,0,382,387,3,
        16,8,0,383,384,5,122,0,0,384,386,3,16,8,0,385,383,1,0,0,0,386,389,
        1,0,0,0,387,385,1,0,0,0,387,388,1,0,0,0,388,63,1,0,0,0,389,387,1,
        0,0,0,390,391,3,92,46,0,391,394,3,66,33,0,392,393,5,99,0,0,393,395,
        3,10,5,0,394,392,1,0,0,0,394,395,1,0,0,0,395,396,1,0,0,0,396,397,
        5,128,0,0,397,65,1,0,0,0,398,399,5,132,0,0,399,400,5,85,0,0,400,
        401,5,1,0,0,401,402,5,86,0,0,402,67,1,0,0,0,403,406,3,70,35,0,404,
        406,3,72,36,0,405,403,1,0,0,0,405,404,1,0,0,0,406,69,1,0,0,0,407,
        408,3,74,37,0,408,409,5,128,0,0,409,71,1,0,0,0,410,411,3,74,37,0,
        411,412,3,22,11,0,412,73,1,0,0,0,413,414,3,80,40,0,414,415,5,132,
        0,0,415,417,5,83,0,0,416,418,3,76,38,0,417,416,1,0,0,0,417,418,1,
        0,0,0,418,419,1,0,0,0,419,420,5,84,0,0,420,75,1,0,0,0,421,426,3,
        78,39,0,422,423,5,122,0,0,423,425,3,78,39,0,424,422,1,0,0,0,425,
        428,1,0,0,0,426,424,1,0,0,0,426,427,1,0,0,0,427,77,1,0,0,0,428,426,
        1,0,0,0,429,430,3,80,40,0,430,431,5,132,0,0,431,434,1,0,0,0,432,
        434,5,131,0,0,433,429,1,0,0,0,433,432,1,0,0,0,434,79,1,0,0,0,435,
        438,3,82,41,0,436,438,3,84,42,0,437,435,1,0,0,0,437,436,1,0,0,0,
        438,81,1,0,0,0,439,440,3,84,42,0,440,441,5,91,0,0,441,83,1,0,0,0,
        442,448,3,86,43,0,443,448,3,88,44,0,444,448,3,90,45,0,445,448,3,
        92,46,0,446,448,3,94,47,0,447,442,1,0,0,0,447,443,1,0,0,0,447,444,
        1,0,0,0,447,445,1,0,0,0,447,446,1,0,0,0,448,85,1,0,0,0,449,455,5,
        43,0,0,450,455,5,44,0,0,451,455,5,58,0,0,452,453,5,44,0,0,453,455,
        5,44,0,0,454,449,1,0,0,0,454,450,1,0,0,0,454,451,1,0,0,0,454,452,
        1,0,0,0,455,87,1,0,0,0,456,461,5,37,0,0,457,461,5,28,0,0,458,459,
        5,44,0,0,459,461,5,28,0,0,460,456,1,0,0,0,460,457,1,0,0,0,460,458,
        1,0,0,0,461,89,1,0,0,0,462,463,5,12,0,0,463,91,1,0,0,0,464,465,5,
        16,0,0,465,93,1,0,0,0,466,467,5,79,0,0,467,95,1,0,0,0,33,99,108,
        126,157,213,215,225,228,233,247,253,265,275,302,306,310,320,325,
        338,349,355,369,378,387,394,405,417,426,433,437,447,454,460
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
    RULE_integerLiteral = 2
    RULE_characterLiteral = 3
    RULE_floatingLiteral = 4
    RULE_stringLiteral = 5
    RULE_constExpression = 6
    RULE_leftExpression = 7
    RULE_expression = 8
    RULE_functionCall = 9
    RULE_statement = 10
    RULE_compoundStatement = 11
    RULE_ifStatement = 12
    RULE_switchStatement = 13
    RULE_caseStatement = 14
    RULE_whileStatement = 15
    RULE_doWhileStatement = 16
    RULE_forStatement = 17
    RULE_forExprSet = 18
    RULE_returnStatement = 19
    RULE_breakStatement = 20
    RULE_continueStatement = 21
    RULE_declaration = 22
    RULE_variableDeclarator = 23
    RULE_variableDeclarationList = 24
    RULE_variableDeclaration = 25
    RULE_varDeclWithoutInit = 26
    RULE_varDeclWithConstInit = 27
    RULE_varDeclWithNormalInit = 28
    RULE_arrayDeclarator = 29
    RULE_normalArrayDeclaration = 30
    RULE_arrayAssginExpressionList = 31
    RULE_stringDeclaration = 32
    RULE_arrayName = 33
    RULE_functionDeclarator = 34
    RULE_functionDeclaration = 35
    RULE_functionDefinition = 36
    RULE_functionHead = 37
    RULE_functionParameterList = 38
    RULE_functionParameter = 39
    RULE_typeModifier = 40
    RULE_pointerTypeModifier = 41
    RULE_normalTypeModifier = 42
    RULE_integerTypeModifier = 43
    RULE_realTypeModifier = 44
    RULE_boolTypeModifier = 45
    RULE_charTypeModifier = 46
    RULE_voidTypeModifier = 47

    ruleNames =  [ "translationUnit", "literal", "integerLiteral", "characterLiteral", 
                   "floatingLiteral", "stringLiteral", "constExpression", 
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
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79:
                self.state = 96
                self.declaration()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
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

        def integerLiteral(self):
            return self.getTypedRuleContext(cpp2llvmParser.IntegerLiteralContext,0)


        def characterLiteral(self):
            return self.getTypedRuleContext(cpp2llvmParser.CharacterLiteralContext,0)


        def floatingLiteral(self):
            return self.getTypedRuleContext(cpp2llvmParser.FloatingLiteralContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(cpp2llvmParser.StringLiteralContext,0)


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
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.integerLiteral()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.characterLiteral()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.floatingLiteral()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.stringLiteral()
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


    class IntegerLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(cpp2llvmParser.IntegerLiteral, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_integerLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerLiteral" ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerLiteral" ):
                listener.exitIntegerLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLiteral" ):
                return visitor.visitIntegerLiteral(self)
            else:
                return visitor.visitChildren(self)




    def integerLiteral(self):

        localctx = cpp2llvmParser.IntegerLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_integerLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(cpp2llvmParser.IntegerLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CharacterLiteral(self):
            return self.getToken(cpp2llvmParser.CharacterLiteral, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_characterLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterLiteral" ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterLiteral" ):
                listener.exitCharacterLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacterLiteral" ):
                return visitor.visitCharacterLiteral(self)
            else:
                return visitor.visitChildren(self)




    def characterLiteral(self):

        localctx = cpp2llvmParser.CharacterLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_characterLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(cpp2llvmParser.CharacterLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatingLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FloatingLiteral(self):
            return self.getToken(cpp2llvmParser.FloatingLiteral, 0)

        def getRuleIndex(self):
            return cpp2llvmParser.RULE_floatingLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatingLiteral" ):
                listener.enterFloatingLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatingLiteral" ):
                listener.exitFloatingLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatingLiteral" ):
                return visitor.visitFloatingLiteral(self)
            else:
                return visitor.visitChildren(self)




    def floatingLiteral(self):

        localctx = cpp2llvmParser.FloatingLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_floatingLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(cpp2llvmParser.FloatingLiteral)
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
        self.enterRule(localctx, 10, self.RULE_stringLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
        self.enterRule(localctx, 12, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
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
        self.enterRule(localctx, 14, self.RULE_leftExpression)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(cpp2llvmParser.Identifier)

                self.state = 122
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 123
                self.expression(0)
                self.state = 124
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 129
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 130
                self.literal()
                pass

            elif la_ == 3:
                self.state = 131
                self.match(cpp2llvmParser.Identifier)
                pass

            elif la_ == 4:
                self.state = 132
                self.match(cpp2llvmParser.LeftParen)
                self.state = 133
                self.expression(0)
                self.state = 134
                self.match(cpp2llvmParser.RightParen)
                pass

            elif la_ == 5:
                self.state = 136
                self.match(cpp2llvmParser.Not)
                self.state = 137
                self.expression(25)
                pass

            elif la_ == 6:
                self.state = 138
                self.match(cpp2llvmParser.Minus)
                self.state = 139
                self.expression(24)
                pass

            elif la_ == 7:
                self.state = 140
                self.match(cpp2llvmParser.And)
                self.state = 141
                self.leftExpression()
                pass

            elif la_ == 8:
                self.state = 142
                self.match(cpp2llvmParser.Identifier)
                self.state = 143
                self.match(cpp2llvmParser.LeftBracket)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.match(cpp2llvmParser.RightBracket)
                pass

            elif la_ == 9:
                self.state = 147
                self.leftExpression()
                self.state = 148
                self.match(cpp2llvmParser.Assign)
                self.state = 149
                self.expression(3)
                pass

            elif la_ == 10:
                self.state = 151
                self.leftExpression()
                self.state = 152
                self.match(cpp2llvmParser.PlusPlus)
                pass

            elif la_ == 11:
                self.state = 154
                self.leftExpression()
                self.state = 155
                self.match(cpp2llvmParser.MinusMinus)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 213
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 159
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 160
                        self.match(cpp2llvmParser.Star)
                        self.state = 161
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 163
                        self.match(cpp2llvmParser.Div)
                        self.state = 164
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 166
                        self.match(cpp2llvmParser.Mod)
                        self.state = 167
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 169
                        self.match(cpp2llvmParser.Plus)
                        self.state = 170
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 172
                        self.match(cpp2llvmParser.Minus)
                        self.state = 173
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 175
                        self.match(cpp2llvmParser.Less)
                        self.state = 176
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 178
                        self.match(cpp2llvmParser.Greater)
                        self.state = 179
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 180
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 181
                        self.match(cpp2llvmParser.LessEqual)
                        self.state = 182
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 183
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 184
                        self.match(cpp2llvmParser.GreaterEqual)
                        self.state = 185
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 187
                        self.match(cpp2llvmParser.Equal)
                        self.state = 188
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 190
                        self.match(cpp2llvmParser.NotEqual)
                        self.state = 191
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 193
                        self.match(cpp2llvmParser.Or)
                        self.state = 194
                        self.expression(12)
                        pass

                    elif la_ == 13:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 196
                        self.match(cpp2llvmParser.And)
                        self.state = 197
                        self.expression(11)
                        pass

                    elif la_ == 14:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 199
                        self.match(cpp2llvmParser.Caret)
                        self.state = 200
                        self.expression(10)
                        pass

                    elif la_ == 15:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 202
                        self.match(cpp2llvmParser.OrOr)
                        self.state = 203
                        self.expression(9)
                        pass

                    elif la_ == 16:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 205
                        self.match(cpp2llvmParser.AndAnd)
                        self.state = 206
                        self.expression(8)
                        pass

                    elif la_ == 17:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 208
                        self.match(cpp2llvmParser.LeftShift)
                        self.state = 209
                        self.expression(7)
                        pass

                    elif la_ == 18:
                        localctx = cpp2llvmParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 211
                        self.match(cpp2llvmParser.RightShift)
                        self.state = 212
                        self.expression(6)
                        pass

             
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(cpp2llvmParser.Identifier)
            self.state = 219
            self.match(cpp2llvmParser.LeftParen)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 220
                self.expression(0)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==122:
                    self.state = 221
                    self.match(cpp2llvmParser.Comma)
                    self.state = 222
                    self.expression(0)
                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 230
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
        self.enterRule(localctx, 20, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                    self.state = 232
                    self.expression(0)


                self.state = 235
                self.match(cpp2llvmParser.Semi)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.switchStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
                self.doWhileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 241
                self.forStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 242
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 243
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 244
                self.continueStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 245
                self.variableDeclarator()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 246
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
        self.enterRule(localctx, 22, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 432374564257869854) != 0 or (((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & -9223372027152941055) != 0 or _la==132:
                self.state = 250
                self.statement()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
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
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(cpp2llvmParser.If)
            self.state = 259
            self.match(cpp2llvmParser.LeftParen)
            self.state = 260
            self.expression(0)
            self.state = 261
            self.match(cpp2llvmParser.RightParen)
            self.state = 262
            self.statement()
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(cpp2llvmParser.Else)
                self.state = 264
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
        self.enterRule(localctx, 26, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(cpp2llvmParser.Switch)
            self.state = 268
            self.match(cpp2llvmParser.LeftParen)
            self.state = 269
            self.expression(0)
            self.state = 270
            self.match(cpp2llvmParser.RightParen)
            self.state = 271
            self.match(cpp2llvmParser.LeftBrace)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 272
                self.caseStatement()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 278
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
        self.enterRule(localctx, 28, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(cpp2llvmParser.Case)
            self.state = 281
            self.constExpression()
            self.state = 282
            self.match(cpp2llvmParser.Colon)
            self.state = 283
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
        self.enterRule(localctx, 30, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(cpp2llvmParser.While)
            self.state = 286
            self.match(cpp2llvmParser.LeftParen)
            self.state = 287
            self.expression(0)
            self.state = 288
            self.match(cpp2llvmParser.RightParen)
            self.state = 289
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
        self.enterRule(localctx, 32, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(cpp2llvmParser.Do)
            self.state = 292
            self.statement()
            self.state = 293
            self.match(cpp2llvmParser.While)
            self.state = 294
            self.match(cpp2llvmParser.LeftParen)
            self.state = 295
            self.expression(0)
            self.state = 296
            self.match(cpp2llvmParser.RightParen)
            self.state = 297
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
        self.enterRule(localctx, 34, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(cpp2llvmParser.For)
            self.state = 300
            self.match(cpp2llvmParser.LeftParen)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 301
                self.forExprSet()


            self.state = 304
            self.match(cpp2llvmParser.Semi)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 305
                self.expression(0)


            self.state = 308
            self.match(cpp2llvmParser.Semi)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 309
                self.forExprSet()


            self.state = 312
            self.match(cpp2llvmParser.RightParen)
            self.state = 313
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
        self.enterRule(localctx, 36, self.RULE_forExprSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.expression(0)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 316
                self.match(cpp2llvmParser.Comma)
                self.state = 317
                self.expression(0)
                self.state = 322
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
        self.enterRule(localctx, 38, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(cpp2llvmParser.Return)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0 or (((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 562949953458305) != 0:
                self.state = 324
                self.expression(0)


            self.state = 327
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
        self.enterRule(localctx, 40, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(cpp2llvmParser.Break)
            self.state = 330
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
        self.enterRule(localctx, 42, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(cpp2llvmParser.Continue)
            self.state = 333
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
        self.enterRule(localctx, 44, self.RULE_declaration)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.variableDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.arrayDeclarator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
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
        self.enterRule(localctx, 46, self.RULE_variableDeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.typeModifier()
            self.state = 341
            self.variableDeclarationList()
            self.state = 342
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
        self.enterRule(localctx, 48, self.RULE_variableDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.variableDeclaration()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 345
                self.match(cpp2llvmParser.Comma)
                self.state = 346
                self.variableDeclaration()
                self.state = 351
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
        self.enterRule(localctx, 50, self.RULE_variableDeclaration)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.varDeclWithoutInit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.varDeclWithConstInit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
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
        self.enterRule(localctx, 52, self.RULE_varDeclWithoutInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
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
        self.enterRule(localctx, 54, self.RULE_varDeclWithConstInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(cpp2llvmParser.Identifier)
            self.state = 360
            self.match(cpp2llvmParser.Assign)
            self.state = 361
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
        self.enterRule(localctx, 56, self.RULE_varDeclWithNormalInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(cpp2llvmParser.Identifier)
            self.state = 364
            self.match(cpp2llvmParser.Assign)
            self.state = 365
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
        self.enterRule(localctx, 58, self.RULE_arrayDeclarator)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.normalArrayDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
        self.enterRule(localctx, 60, self.RULE_normalArrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.normalTypeModifier()
            self.state = 372
            self.arrayName()
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 373
                self.match(cpp2llvmParser.Assign)
                self.state = 374
                self.match(cpp2llvmParser.LeftBrace)
                self.state = 375
                self.arrayAssginExpressionList()
                self.state = 376
                self.match(cpp2llvmParser.RightBrace)


            self.state = 380
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
        self.enterRule(localctx, 62, self.RULE_arrayAssginExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.expression(0)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 383
                self.match(cpp2llvmParser.Comma)
                self.state = 384
                self.expression(0)
                self.state = 389
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
        self.enterRule(localctx, 64, self.RULE_stringDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.charTypeModifier()
            self.state = 391
            self.arrayName()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==99:
                self.state = 392
                self.match(cpp2llvmParser.Assign)
                self.state = 393
                self.stringLiteral()


            self.state = 396
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
        self.enterRule(localctx, 66, self.RULE_arrayName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(cpp2llvmParser.Identifier)
            self.state = 399
            self.match(cpp2llvmParser.LeftBracket)
            self.state = 400
            self.match(cpp2llvmParser.IntegerLiteral)
            self.state = 401
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
        self.enterRule(localctx, 68, self.RULE_functionDeclarator)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
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
        self.enterRule(localctx, 70, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.functionHead()
            self.state = 408
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
        self.enterRule(localctx, 72, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.functionHead()
            self.state = 411
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
        self.enterRule(localctx, 74, self.RULE_functionHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.typeModifier()
            self.state = 414
            self.match(cpp2llvmParser.Identifier)
            self.state = 415
            self.match(cpp2llvmParser.LeftParen)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 288256902138236928) != 0 or _la==79 or _la==131:
                self.state = 416
                self.functionParameterList()


            self.state = 419
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
        self.enterRule(localctx, 76, self.RULE_functionParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.functionParameter()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==122:
                self.state = 422
                self.match(cpp2llvmParser.Comma)
                self.state = 423
                self.functionParameter()
                self.state = 428
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

        def typeModifier(self):
            return self.getTypedRuleContext(cpp2llvmParser.TypeModifierContext,0)


        def Identifier(self):
            return self.getToken(cpp2llvmParser.Identifier, 0)

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
        self.enterRule(localctx, 78, self.RULE_functionParameter)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 16, 28, 37, 43, 44, 58, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.typeModifier()
                self.state = 430
                self.match(cpp2llvmParser.Identifier)
                pass
            elif token in [131]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(cpp2llvmParser.Ellipsis)
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
        self.enterRule(localctx, 80, self.RULE_typeModifier)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.pointerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
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
        self.enterRule(localctx, 82, self.RULE_pointerTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.normalTypeModifier()
            self.state = 440
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
        self.enterRule(localctx, 84, self.RULE_normalTypeModifier)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.integerTypeModifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.realTypeModifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.boolTypeModifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.charTypeModifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
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
        self.enterRule(localctx, 86, self.RULE_integerTypeModifier)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(cpp2llvmParser.Int)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.match(cpp2llvmParser.Long)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.match(cpp2llvmParser.Short)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 452
                self.match(cpp2llvmParser.Long)
                self.state = 453
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
        self.enterRule(localctx, 88, self.RULE_realTypeModifier)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(cpp2llvmParser.Float)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(cpp2llvmParser.Double)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 458
                self.match(cpp2llvmParser.Long)
                self.state = 459
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
        self.enterRule(localctx, 90, self.RULE_boolTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
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
        self.enterRule(localctx, 92, self.RULE_charTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
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
        self.enterRule(localctx, 94, self.RULE_voidTypeModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
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
        self._predicates[8] = self.expression_sempred
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
         




