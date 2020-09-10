import pdb

class CompoundInterest:

    @staticmethod
    def calculate(
            starting_amount, interest_rate,
            years, monthly_contribution=0
    ):
        P = starting_amount
        r = interest_rate/100.00
        t = years
        n = 12.00
        PMT = monthly_contribution
        A = P * ( 1.00 + r/n )**( n * t )
        if PMT == 0:
            return round(A, 2)
        else:
            future_val = CompoundInterest.future_value(r, n, t, PMT)
            return round(A + future_val, 2)

    @staticmethod
    def future_value(r, n, t, PMT):
        x = 1.00 + r/n
        return PMT * ((x**(n*t) - 1.00) / (r/n)) * x
