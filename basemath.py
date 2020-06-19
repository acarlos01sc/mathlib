from math import factorial

# basemath contains some basic math classes

# class natnumber get some characteristics of a natural number
# the constructor is natnumber(n) where n is a natural number
# the methods are:
#		n            - returns the n number used in constructor
#		factorial    - returns the factorial number of n
#               phi          - returns Euler's totient function of n
#		factor       - returns the list of prime factors of n
#		iseven       - returns true if n is even
#		isprime      - returns true if n is a prime number otherwise false
#		istriangular - returns true if n is a triangular number
 
class natnumber(object):

        def __init__(self, x):
                self.__n = x
                self.__factor = []
                self.__factor_defined = False
                self.__testn()

        def __testn(self):
                assert (isinstance(self.n, int) and (self.n >= 0)), 'Invalid natural number!'
                
        def __calcfactors_odd(self, numerator, denominator = 3):
        	den = denominator
        	num = numerator
        	while (num/den != 1):
                    if (num % den == 0):
                        self.__factor.append(den)
                        num /= den
                    else:
                        den += 2
        	self.__factor.append(den)

        def __calcfactors_even(self, numerator, denominator = 2):
                den = denominator
                num = numerator
                while (num/den != 1):
                    if (num % den == 0):
                        self.__factor.append(den)
                        num /= den
                    else:
                        den += 1
                        break
                if (num/den != 1):
                    self.__calcfactors_odd(num)
                else:
                    self.__factor.append(den)

        def __calc_phi(self):
                self.factor
                phi = self.__n
                ref = 1
                for i in self.__factor:
                        if (ref != i):
                                ref = i
                                phi *= (ref-1)/ref
                return phi

        @property
        def n(self):
                return self.__n

        @property
        def factorial(self):
                return factorial(self.n)

        @property
        def factor(self):
                if not(self.__factor_defined):
                        self.__factor.clear()
                        if (self.n <= 1):
                                self.__factor.append(self.n)
                        elif self.iseven:
                                self.__calcfactors_even(self.n)
                        else:
                                self.__calcfactors_odd(self.n)
                        self.__factor_defined = True
                return self.__factor

        @property
        def iseven(self):
            return ((self.n % 10) in [0,2,4,6,8])

        @property
        def isprime(self):
                if (self.n <= 1):
                        return False
                else:
                        return len(self.factor) == 1

        @property
        def istriangular(self):
            i = 1
            while (((i*(i+1))/2) < self.n):
                i += 1
            if (((i*(i+1))/2) == self.n):
                return True
            else:
                return False

        @property
        def phi(self):
                return self.__calc_phi()
