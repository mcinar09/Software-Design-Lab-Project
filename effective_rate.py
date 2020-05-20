def effectiverate(r, n):  # r is yearly interest rate in decimal form, n is number of times per year the interest is compounded
    """The effective annual interest rate is the real return on a savings account or any interest-paying
    investment when the effects of compounding over time are taken into account. It also reveals the real 
    percentage rate owed in interest on a loan, a credit card, or any other debt. """
    divided_rate = r/n
    compounded_float = 1 + divided_rate
    exponent_float = ((compounded_float ** n) - 1)
    rounded_exponent_float = round(exponent_float, 4)*100
    return rounded_exponent_float


effectiverate(.062, 365)

effectiverate(.0625, 2)

#  Comparing two Investment accounts


def comparing_annual_yield(account_1_r, account_1_n, account_2_r, account_2_n):
    """ Which savings account is a better investment? """

    account_1 = (effectiverate(account_1_r, account_1_n))
    account_2 = (effectiverate(account_2_r, account_2_n))
    if account_1 > account_2:
        choice_1 = print("First investment account is better with an annual yield of " +
                         str(account_1) + "%.")
        return choice_1
    elif account_1 < account_2:
        choice_2 = print("Second investment account is better with an annual yield of " +
                         str(account_2) + "%.")
        return choice_2
    else:
        return "There's no difference between two investments"


comparing_annual_yield(0.062, 365, .0625, 2)
comparing_annual_yield(0.03, 12, 0.0325, 2)

# Annuities


# reg_payment is the regular periodic payment, t is the term of the annuity in years
def future_value_of_annuity(reg_payment, r, n, t):
    """ An annuity is a savings investment plan in which the investor makes a regular, fixed payment into a compound - interest account\n
    where the interest rate doesn't change during the term of the investment. """
    divided_rate = r/n
    compounded_float = 1 + divided_rate
    exponent_float = ((compounded_float**(n*t)) - 1)

    product = (reg_payment*exponent_float)
    future_amount = round(product/divided_rate, 2)
    return print("In " + str(t) + " years, you will receive $" + str(future_amount))


future_value_of_annuity(500, 0.06, 1, 3)
future_value_of_annuity(800, 0.05, 2, 4)


# Finding the Monthly Payment for an Annuity
def monthly_payment_for_an_annuity(future_amount, r, n, t):
    """Compute the periodic payment to meet an investment goal. """
    divided_rate = r/n
    compounded_float = 1 + divided_rate
    exponent_float = ((compounded_float**(n*t)) - 1)
    product_of_f_d = future_amount * divided_rate
    monthly_payment = round(product_of_f_d/exponent_float, 2)
    return print("Your monthly fixed payment to receive $" + str(future_amount) + " in " + str(t) + " years is $" + str(monthly_payment))


monthly_payment_for_an_annuity(35000, 0.075, 52, 5)
monthly_payment_for_an_annuity(6000, 0.055, 12, 2)
