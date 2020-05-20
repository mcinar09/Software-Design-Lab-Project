# Calculating the Effective Rate, and Annuities

For my project, I defined some functions that will provide some necessary information for an investor or for a loan borrower using Python. I used some built-in Python functions like `print()`, `round()` and control flow functions (i. e., `if`, `elif`, and `else`) to compare values and return the desired one.

## Effective Rate
 The first function I defined  is `effective_rate` that calculates the annual interest yield of an investment account. 

The effective annual interest rate is the real return on a savings account or any interest-paying investment when the effects of compounding over time are taken into account. It also reveals the real percentage rate owed in interest on a loan, a credit card, or any other debt.
 
The function, `effective_rate` takes two parameters:
- `r` = interest rate per year (i. e., stated rate)
- `n` = number of periods per year the interest is calculated

Then, it provides you the real annual yield (real interest rate per year rather than the stated one).

## Comparing Two Investment Accounts

Next, I defined a function, `comparing_annual_yield` that compares two investment accounts and tells you the best option. 

The function, `comparing_annual_yield` takes four parameters:

- `account_1_r` = interest rate of account one

- `account_1_n` = number of periods per year the interest is calculated for account one

- `account_2_r` = interest rate of account two

- `account_2_n` = number of periods per year the interest is calculated for account two

## Annuities

The third function, `future_value_of_annuity` computes the the future amount for an investor who plans to save money for some particular expenses.

An annuity is a savings investment plan in which the investor makes a regular, fixed payment into a compound - interest account where the interest rate doesn't change during the term of the investment.  This differs from a regular compound - interest account in that you don't invest an entire amount at the beginning of the investment period, but rather the investment up into smaller payments.For example, you might pay \\$500  annually for 3 years into an account that yields 6\% interest compounded annually. The total amount accumulated (payments plus interest) is called the future value of the annuity.

Annuities are often used by individuals or families to save money to pay things like college expenses, vacations, or retirements.

The function, `future_value_of_annuity` takes four parameters:

- `reg_payment` is the regular periodic payment
- `r` is the annual interest rate
- `n` is the number of payments made per year
- `t` is the term of the annuity in years

##  Finding the Monthly Payment for an Annuity

The fourth function, `monthly_payment_for_an_annuity` computes the regular periodic payment to meet an investment goal.

One way that annuities are commonly used is to save money for some specific future expenses. In that case, you'd more than likely know what future value you're shooting for, and you'd be interested in finding the regular payment necessary to reach that goal. 

The function, `monthly_payment_for_an_annuity` takes four parameters:

- `future_amount` is the desired savings

- `r` is the annual interest rate
- `n` is the number of payments made per year
- `t` is the term of the annuity in years


#### References:
- *Sobecki, Dave, Bluman*, *Allan, "MATH in Our World"*, Third Edition, McGraw-Hill Education, 2015.

- https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python

- https://www.youtube.com/watch?v=yXY3f9jw7fg




