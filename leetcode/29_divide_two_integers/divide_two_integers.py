class Solution:
    """
    1) need to know if dividend and or divisor are positive or negative
    2) divisor can be >= dividend
    3) handle overflow

    4) is performance going to be an issue? Can't just linearly add divisor
       until >= dividend (including)
       
       multiplier * dividend >= divisor (return multiplier - 1)
       
       linear = could increment multplier by 1 (add dividend until >= divisor)
       binary search, double dividend until >=divisor, then add smaller chunks
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        # determine signness of return value (1/-1)
        signness = self.signness(dividend, divisor)
        multiplier = 0

        #only deal with abs below
        dividend = abs(dividend)
        divisor = abs(divisor)
        while (dividend >= divisor):
            dividend -= divisor
            multiplier += 1
        
        return signness * multiplier


        #return signness * self.divideRecursive(dividend, divisor, 0, 0)

    
    """
    Handle only positive values
    """
    #def divideRecursive(self, total: int, divisor, i: int, sum: int) -> int:
    def divideRecursive(self, total: int, divisor) -> int:
        if total == 0: # 0 / 5 = 0
            return 0
        elif total == divisor: # 4 /4 = 1
            return 1
        elif total < divisor: # 2 / 4 = 0 (remainder = 2)
            return 0
        else:
            return 
            # total > divisor
            # 10 / 2
            # 
    ###
    # 10 / 2
    # 8 / 2 i=1 sum=2
    # 6 / 2 i=2 sum=4
    # 2 / 2 i=4 sum=8  

    def isPositive(self, num: int) -> bool:
        return num == abs(num)

    def signness(self, a: int, b: int) -> int:
        isSame = ((self.isPositive(a) and self.isPositive(b)) or
        (not self.isPositive(a) and not self.isPositive(b)))

        if isSame:
            return 1
        else:
            return -1
