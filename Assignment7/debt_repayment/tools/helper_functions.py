#Put useful stuff here
#Make good choices :)

def calculate_payments(loan_amount: float, annual_interest_rate:float, num_months: int):
    """
    calculates the monthly payment for a loan using the formula for fixed-rate loans

    Args:
        loan_amount(float): the total amount of the loan
        annual_interest_rate(float): the annual interest rate as a percentage
        num_months(int): the number of months for the loan term

    Returns:
        float: the monthly payment
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    if monthly_interest_rate == 0:
        return round(loan_amount / num_months, 2)

    m = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_months) / \
        ((1 + monthly_interest_rate) ** num_months -1)
    return round(m, 2)

def calculate_total_paid(monthly_payment: float, annual_interest_rate: float, num_months: int):
    """
    calculates the total amount paid over the life of the loan

    Args:
        monthly_payment(float): the monthly payment amount
        num_months(int): the number of months for the loan term

    Returns:
        float: the total amount paid

    """
    loan_amount = calculate_payments(monthly_payment, annual_interest_rate, num_months)

    return round(loan_amount * num_months, 2)


def calculate_total_interest(loan_amount: float, annual_interest_rate: float, num_months: int):
    """
    calculates the total interest paid over the life of the loan

    Args:
        loan_amount(float): the total amount paid over the loan term
        num_months(int): the initial loan amount

    Returns:
        float: the total interest paid
    """
    total_paid = calculate_total_paid(loan_amount, annual_interest_rate, num_months)
    return round(total_paid - loan_amount, 2)

def main():
    loan_amount = 10000
    annual_interest_rate = 5
    num_months = 36

    monthly_payment = calculate_payments(loan_amount, annual_interest_rate ,num_months)
    print(f'Monthly Payment: ${monthly_payment}')

    total_paid = calculate_total_paid(monthly_payment, annual_interest_rate, num_months)
    print(f'Total Amount Paid: ${total_paid}')

    total_interest = calculate_total_interest(loan_amount, annual_interest_rate, num_months)
    print(f'Total Interest Paid: ${total_interest}')

if __name__ == '__main__':
    main()