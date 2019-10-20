from math import factorial

# basemath contains some basic math classes

# class natnumber get some characteristics of a natural number
# the constructor is natnumber(n) where n is a natural number
# the methods are:
#		n            - returns the n number used in constructor
#		factorial    - returns the factorial number of n
#		factor       - returns the list of prime factors of n
#		isprime      - returns true if n is a prime number otherwise false
#		istriangular - returns true if n is a triangular number
 
class natnumber(object):

        def __init__(self, x):
                self.__n = x
                self.__factor = []
                self.__testn()

        def __testn(self):
                assert (isinstance(self.n, int) and (self.n >= 0)), 'Invalid natural number!'
                
        def __calcfactors(self):
                den = 2
                num = self.n
                while (num/den != 1):
                    if (num % den == 0):
                        self.__factor.append(den)
                        num /= den
                    else:
                        den += 1
                        break
                while (num/den != 1):
                    if (num % den == 0):
                        self.__factor.append(den)
                        num /= den
                    else:
                        den += 2
                self.__factor.append(den)

        @property
        def n(self):
                return self.__n

        @property
        def factorial(self):
                return factorial(self.n)

        @property
        def factor(self):
                self.__factor.clear()
                if (self.n <= 1):
                        self.__factor.append(self.n)
                else:
                        self.__calcfactors()
                return self.__factor

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
