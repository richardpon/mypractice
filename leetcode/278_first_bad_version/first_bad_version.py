# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
"""
G G|G B B  lower is all good, so bad must be in upper
l   m   u
mid = 2 lower=[0:2], upper=[2:5]

G G G|B B lower is all good, so first bad in upper
    l m u
mid = 1

G G G B|B lowest is bad, so return it's index
      lmu
lower = mid


G G|B B B  lower is all good, bad must be in upper
l   m   u

G G B|B B lowest is bad so return its index
    l m u

G G B    
"""
class Solution:
    def firstBadVersion(self, n):
        return self.first_bad_recursive(1, n)
    
    # call only on range containing first BAD
    def first_bad_recursive(self, lower, upper):
        #base cases
        if lower == upper:
            # range contains BAD, so this must be first bad
            return lower

        elif upper - lower == 1:
            #only two elements
            if isBadVersion(lower):
                return lower
            else:
                return upper
        
        # 3 or more elements
        mid = (upper + lower) // 2

        if isBadVersion(lower):
            # since this range includes the first bad, then lower must be the first bad
            return lower
        elif isBadVersion(mid):
            # bad version is in lower half
            return self.first_bad_recursive(lower, mid)
        else:
            # first bad in upper 
            # don't include mid as it was checked above
            return self.first_bad_recursive(mid + 1, upper)
