import pdb

class CompoundInterest:

    @staticmethod
    def calculate(starting_amount, interest_rate, years):
        P = starting_amount
        r = interest_rate/100.00
        t = years
        n = 12.00
        A = P * ( 1.00 + r/n )**( n * t )
        return round(A, 2)
