#Modify this file so that your imports are correct.
from debt_repayment.GUI import DebtAPP
from debt_repayment.amortization_table.table import AmortizationTable
import pandas as pd

if __name__=="__main__":
    DebtAPP(AmortizationTable)