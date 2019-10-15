from math import factorial

class natnumber(object):

        def __init__(self, x):
                self.__n = x
                self.__factor = []
                self.__testn()

        def __testn(self):
                assert (isinstance(self.n, int) and (self.n >= 0)), 'Invalid natural number!'

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
                        den = 2
                        num = self.n
                        while (num/den != 1):
                                if (num % den == 0):
                                        self.__factor.append(den)
                                        num = num/den
                                else:
                                        den += 1
                        self.__factor.append(den)
                return self.__factor

        @property
        def isprime(self):
                if (self.n <= 1):
                        return False
                else:
                        return len(self.factor) == 1
