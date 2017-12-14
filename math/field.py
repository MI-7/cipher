class polynomial:
    # n = [1, 10, 0, 0, 3]
    # => x**4 + 10*x**3 + 0 + 0 + 3
    def __init__(self, coeffs):
        self.coeffs = coeffs
    
    # 0 -> 3
    def coeff(self, i):
        return self.coeffs[len(self.coeffs) - i - 1]

    def sub(p1, p2):
        return p1 + p2 * polynomial([-1])

    def add(p1, p2):
        l1 = len(p1.coeffs)
        l2 = len(p2.coeffs)
        
        new_coeffs = []
        if l1 >= l2:
            p2_coeffs = [0] * (l1 - l2) + p2.coeffs
            new_coeffs = [p1.coeffs[i] + p2_coeffs[i] for i in range(0, len(p2_coeffs))]
        else:
            p1_coeffs = [0] * (l2 - l1) + p1.coeffs
            new_coeffs = [p1_coeffs[i] + p2.coeffs[i] for i in range(0, len(p1_coeffs))]
        
        return polynomial(new_coeffs)
    
    def __add__(p1, p2):
        return polynomial.add(p1, p2)
    
    def __sub__(p1, p2):
        return polynomial.sub(p1, p2)
    
    def scalarMult(self, s):
        # Returns: a new polynomial with all coefficients of self, multiplied by s
        return polynomial([self.coeffs[i] * s for i in range(0, len(self.coeffs))])
    
    def mul(p1, p2):
        p3 = polynomial([0])
        for i in range(0, len(p1.coeffs)):
            a = p1.coeffs[i]
            p4 = polynomial.shift(p2, (len(p1.coeffs) - 1 - i))
            p3 = polynomial.add(p3, p4.scalarMult(a))
        
        return p3   
     
    def shift(p, a):
        # Returns: a new polynomial, multiplied by x**a.
        return polynomial(p.coeffs + [0] * a)
    
    def __mul__(p1, p2):
        return polynomial.mul(p1, p2)

    def __str__(self, var='z'):
        result = ''
        for i in range(0, len(self.coeffs)):
            result = result + str(self.coeffs[i]) + var + '**' + str(len(self.coeffs) - 1 - i) + ', '
        return result
    
#__repr__(self, var='z')    
     
    def val(self, x):
        # Returns: the value of the polynomial with the variable assigned to x.
        return sum([self.coeffs[i] * (x ** (len(self.coeffs) - 1 - i)) for i in range(0, len(self.coeffs))])


# Galois Field
# Prime Fields: n = 1
# Extension Fields: n > 1
class gf:
    def __init__(self, p, n):
        self.p = p  # p=a prime
        self.n = n  # n=an integer
    
    def __str__(self):
        return "GF(" + str(self.p) + "," + str(self.n) + ")"
 
    def add(self, a, b):
        return (a + b) % self.p

    def sub(self, a, b):
        return (a - b) % self.p
    
    def mul(self, a, b):
        return (a * b) % self.p
    
    def inverse(self, a):
        pass


if __name__ == "__main__":
    g = gf(2, 8)