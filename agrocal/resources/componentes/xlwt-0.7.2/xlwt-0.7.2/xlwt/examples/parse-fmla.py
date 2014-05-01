<<<<<<< HEAD
from xlwt import ExcelFormulaParser, ExcelFormula
import sys

f = ExcelFormula.Formula(
""" -((1.80 + 2.898 * 1)/(1.80 + 2.898))*
AVERAGE((1.80 + 2.898 * 1)/(1.80 + 2.898); 
        (1.80 + 2.898 * 1)/(1.80 + 2.898); 
        (1.80 + 2.898 * 1)/(1.80 + 2.898)) + 
SIN(PI()/4)""")

#for t in f.rpn():
#    print "%15s %15s" % (ExcelFormulaParser.PtgNames[t[0]], t[1])
=======
from xlwt import ExcelFormulaParser, ExcelFormula
import sys

f = ExcelFormula.Formula(
""" -((1.80 + 2.898 * 1)/(1.80 + 2.898))*
AVERAGE((1.80 + 2.898 * 1)/(1.80 + 2.898); 
        (1.80 + 2.898 * 1)/(1.80 + 2.898); 
        (1.80 + 2.898 * 1)/(1.80 + 2.898)) + 
SIN(PI()/4)""")

#for t in f.rpn():
#    print "%15s %15s" % (ExcelFormulaParser.PtgNames[t[0]], t[1])
>>>>>>> 7c6f7ebb9828b38cdb02b715888e268a54ec46f6
