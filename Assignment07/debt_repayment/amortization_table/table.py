#Your official starting point :)
import os
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from debt_repayment.tools.helper_functions import calculate_payments
from debt_repayment.tools.my_logger import my_logger

class AmortizationTable:
    """
    a class to represent an amortization table for a loan.

    Attributes:
        loan_type(str): the type of the loan
        loan_balance(float): the total amount of the loan
        interest_rate(float): the annual interest rate in percentage
        num_months(int): the number of months for the loan term
        monthly_payment(float): the monthly payment amount
        amortization_df(pd.DataFrame): the DataFrame containing the amortization schedule

    Methods:
        create_table: creates an amortization table based on the provided loan details.
        save_table: saves the amortization table to a CSV file.
        more_principal: returns the payment number when more principal than interest is paid.
        halfway: returns the payment number when half of the loan balance is paid off.
        update_payments: updates the loan balance and/or monthly payment, then recreates the table.
    """


    def __init__(self, loan_type, loan_balance, interest_rate, num_months, monthly_payment):
        """
        initializes the AmortizationTable instance

        Attributes:
            loan_type(str): the type of loan
            loan_balance(float): the total loan balance
            interest_rate(float): the annual interest rate
            num_months(int): the number of months over which the loan is to be paid
            monthly_payment(float): the monthly payment amount
        """
        self.logger = my_logger()
        self.logger.info('Initializing Table Instance')
        self.loan_type = loan_type
        self.loan_balance = loan_balance
        self.interest_rate = interest_rate
        self.num_months = num_months
        self.monthly_payment = monthly_payment
        self.amortization_df = pd.DataFrame()
        self.logger.debug(f'Loan details: Type={loan_type}, Balance={loan_balance}, Interest Rate={interest_rate}, Term={num_months} months, Monthly Payment={monthly_payment}')
        self.create_table()


    def create_table(self):
        """
         creates the amortization table by calculating the principal and interest paid for each month.

         Returns:
             None
         """
        self.logger.info('Creating Table...')
        monthly_interest = self.interest_rate / 100 / 12

        rows = []
        current_balance = self.loan_balance
        due_date = (datetime.today().replace(day=1) + relativedelta(months=1))

        for payment_num in range(1, self.num_months + 1):
            interest_paid = current_balance * monthly_interest
            principal_paid = self.monthly_payment - interest_paid

            if current_balance < self.monthly_payment:
                principal_paid = current_balance
                self.monthly_payment = principal_paid + interest_paid
            remaining_balance = current_balance - principal_paid

            rows.append({
                'Payment #': payment_num,
                'Due date': due_date.strftime("%Y-%m-%d"),
                'Payment amount': round(self.monthly_payment, 2),
                'Principal paid': round(principal_paid, 2),
                'Interest paid': round(interest_paid, 2),
                'Remaining balance': round(remaining_balance, 2)
            })

            current_balance = remaining_balance
            due_date += relativedelta(months=1)

            if current_balance <= 0:
                break
        self.amortization_df = pd.DataFrame(rows)
        self.logger.info(f'Table created with {len(rows)}rows.')

    def save_table(self):
        """
        saves the amortization table to a CSV file

        Returns:
            None
        """
        self.logger.info('Saving table to CSV...')
        folder_path = os.path.join('debt_repayment', 'files', 'tables')
        os.makedirs(folder_path, exist_ok=True)

        filename = f'{self.loan_type}-{self.loan_balance}-{self.monthly_payment}.csv'
        file_path = os.path.join(folder_path, filename)

        self.amortization_df.to_csv(file_path, index=False)
        self.logger.info(f'Table Saved to {file_path}')

    def more_principal(self):
        """
        determines the payment number when the principal paid exceeds the interest paid

        Returns:
            int: the payment number when more principal is paid than interest
        """
        for idx, row in self.amortization_df.iterrows():
            if row['Principal paid'] > row['Interest paid']:
                return row['Payment #']

        return self.num_months

    def halfway(self):
        """
        determines the payment number when half of the loan balance is paid off

        Returns:
            int: the payment number at which the loan balance is halfway paid off
        """
        halfway_point = self.loan_balance / 2
        cumulative_principal = 0
        for idx, row in self.amortization_df.iterrows():
           cumulative_principal += row['Principal paid']
           if cumulative_principal >= halfway_point:
                return row['Payment #']
        return self.num_months


    def update_payments(self, lump_sum: 0.0, extra_payment: 0.0):
        """
        updates the loan balance and/or monthly payment, then recreates the amortization table

        Attributes:
            lump_sum(float): An additional lump sum payment to be applied to the loan balance. Default is 0.0
            extra_payment(float): An additional amount to be added to the monthly payment. Default is 0.0

        Returns:
            None
        """
        if lump_sum > 0:
            self.loan_balance -= lump_sum

        if extra_payment > 0:
            self.monthly_payment += extra_payment

        self.create_table()

def main():
    loan_balance = 20000
    annual_interest_rate = 6
    num_months = 36

    monthly_payment = calculate_payments(loan_balance, annual_interest_rate, num_months)

    instance = AmortizationTable(
        loan_type = 'Auto',
        loan_balance = loan_balance,
        interest_rate = annual_interest_rate,
        num_months = num_months,
        monthly_payment = monthly_payment
    )

    print(f'Monthly Payment: S{instance.monthly_payment:.2f}')
    print(f'More principal at payment {instance.more_principal()}')
    print(f'Halfway point at payment {instance.halfway()}')

    print('\n Amortization Table:')
    print(instance.amortization_df)

    instance.save_table()

    instance.update_payments(lump_sum = 100.0, extra_payment = 10)
    print(f'Updated monthly payment: ${instance.monthly_payment:.2f}')



if __name__ == '__main__':
    main()