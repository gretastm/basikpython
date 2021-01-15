class Fraction():
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __add__(self, other):
        a=self.denominator*other.denominator
        b=(a/self.denominator)*self.numerator
        c=(a/other.denominator)*other.numerator
        d=(b+c)/a
        return d
    def __sub__(self, other):
        a = self.denominator * other.denominator
        b = (a / self.denominator) * self.numerator
        c = (a / other.denominator) * other.numerator
        d = (b - c) / a
        return d
    def __mul__(self, other):
        a=self.numerator*other.numerator,self.denominator*other.denominator
        b=other.numerator,other.denominator=other.denominator,other.numerator
        c=self.numerator*other.numerator,self.denominator*other.denominator
        return a,c
    def __eq__(self, other):
        if self.numerator==other.numerator and self.denominator==other.denominator:
            return True
    def __ne__(self, other):
        if self.numerator!=other.numerator and self.numerator!=other.denominator:
            return True
    def __gt__(self, other):
        a=self.numerator/self.denominator
        b=other.numerator/other.denominator
        if a>b:
            return True
        return False