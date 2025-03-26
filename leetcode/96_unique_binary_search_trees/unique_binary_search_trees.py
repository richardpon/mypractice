class Solution:

    """
    Recursive solution where numTrees can be called with various N's on left and right

    n=3
    2,0 -> 2
    1,1 -> 1
    0,2 -> 2

    n=4
    3,0 -> 5
    2,1 -> 2
    1,2 -> 2
    0,3 -> 5
    
    n=5
    4,0 -> 14
    3,1 -> 5
    2,2 -> 4
    1,3 -> 5
    0,4 -> 14
    (42)


    n=6
    5,0 -> 42
    4,1 -> 14
    3,2 -> 10
    2,3 -> 10
    1,4 -> 14
    0,5 -> 42

    """
    
    
    cached_num = {
        0: 1,
        1: 1,
        2: 2,
    }

    def numTrees(self, n: int) -> int:
        
        if n in self.cached_num:
            return self.cached_num[n]

        sum = 0
        for i in range(n):
            left_num = n-1-i
            right_num = i
            
            left_sum = self.numTrees(left_num)
            right_sum = self.numTrees(right_num)

            print(f"{left_num=}->{left_sum=} || {right_num=}->{right_sum=}")


            sum += left_sum * right_sum
            
        if n not in self.cached_num:
            self.cached_num[n] = sum

        return sum
        

