from typing import List

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
        
        raw = self.divideRecursive(
            abs(dividend), 
            abs(divisor), 
            0, 
            [1], 
            [abs(divisor)], 
            0
            )
        
        if signness == 1 and raw > 2**31-1:
            raw = 2**31-1;
        
        return raw * signness

    
    """
    Handle only positive values
    """
    def divideRecursive(
        self, 
        total: int, 
        divisor: int, 
        dividedBy: int,
        num_divisors: List[int], 
        factors: List[int], 
        index_to_try: int
        ) -> int:

        if total == 0: # 0 / 5 = 0
            return dividedBy
        elif total < factors[index_to_try] and index_to_try == 0:
            return dividedBy    
        elif total < factors[index_to_try] and index_to_try > 0:
            #go lower index if it can
            return self.divideRecursive(
                    total,
                    divisor,
                    dividedBy,
                    num_divisors,
                    factors,
                    index_to_try - 1
                )
        elif total >= factors[index_to_try]:
            # Can subtract current power
            new_total = total - factors[index_to_try]
            dividedBy += num_divisors[index_to_try]

            #can go to higher power?
            if len(num_divisors) == index_to_try + 1:
                # Can try a higher divisor
                num_divisors.append(num_divisors[-1] + num_divisors[-1])
                factors.append(factors[-1] + factors[-1])

                return self.divideRecursive(
                    new_total,
                    divisor,
                    dividedBy,
                    num_divisors,
                    factors,
                    index_to_try + 1
                )
            else:
                # Try lower power (higher power failed, so current power a second time will fail)
                new_index = index_to_try - 1 if index_to_try > 0 else index_to_try
                return self.divideRecursive(
                    new_total,
                    divisor,
                    dividedBy,
                    num_divisors,
                    factors,
                    new_index
                )
        


         
    """
    100, 2, 0, [1], [2], 0
    98, 2, 1, [1,2], [2,4], 1
    94, 2, 3, [1,2,4], [2,4,8], 2
    86, 2, 7, [1,2,4,8], [2,4,8,16], 3
    70, 2, 15,[1,2,4,8,16], [2,4,8,16,32], 4
    38, 2, 31,[1,2,4,8,16,32], [2,4,8,16,32,64], 5 #go lower, recurse with 32
    38, 2, 31,[1,2,4,8,16,32], [2,4,8,16,32,64], 4 # go lower since len>index+1 
    6,  2  47,[1,2,4,8,16,32], [2,4,8,16,32,64], 3 # go lower, can't subtract
    6,  2  47,[1,2,4,8,16,32], [2,4,8,16,32,64], 2 # go lower, can't subtract
    6,  2  47,[1,2,4,8,16,32], [2,4,8,16,32,64], 1 # go lower, since len>index+1
    2,  2  49,[1,2,4,8,16,32], [2,4,8,16,32,64], 0 # go lower, since len>index+1
    0,  2  50,[1,2,4,8,16,32], [2,4,8,16,32,64], 0 # go lower, since len>index+1

    100, 3, 0, [1], [3], 0
    97, 3, 1, [1,2], [3,6], 1
    91, 3, 3, [1,2,4], [3,6,12], 2
    79, 3, 7, [1,2,4,8], [3,6,12,24], 3
    55, 3, 15, [1,2,4,8,16], [3,6,12,24,48], 4
    7, 3, 31, [1,2,4,8,16,32], [3,6,12,24,48,96], 5
    7, 3, 31, [1,2,4,8,16,32], [3,6,12,24,48,96], 4
    7, 3, 31, [1,2,4,8,16,32], [3,6,12,24,48,96], 3
    7, 3, 31, [1,2,4,8,16,32], [3,6,12,24,48,96], 2
    7, 3, 31, [1,2,4,8,16,32], [3,6,12,24,48,96], 1
    1, 3, 33, [1,2,4,8,16,32], [3,6,12,24,48,96], 0
    """

    def isPositive(self, num: int) -> bool:
        return num == abs(num)

    def signness(self, a: int, b: int) -> int:
        isSame = ((self.isPositive(a) and self.isPositive(b)) or
        (not self.isPositive(a) and not self.isPositive(b)))

        if isSame:
            return 1
        else:
            return -1
