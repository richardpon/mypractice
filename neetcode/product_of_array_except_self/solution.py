class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = []

        # product of all preceding numbers before ith (not including self)
        prefix_products: List[int] = []
        # product of all numbers after ith (not including self)

        suffix_products: List[int] = []

        product_so_far = 1
        for i in range(len(nums)):
            if i > 0:
                product_so_far *= nums [i-1]
            
            prefix_products.append(product_so_far)


        suffix_product_so_far = 1

        for i in range(len(nums) -1, -1, -1):
            print(f"{i=}")
            if i < len(nums) - 1:
                suffix_product_so_far *= nums[i+1]

            suffix_products = [suffix_product_so_far] + suffix_products

    
        output = []
        for i in range(len(nums)):
            ith = prefix_products[i] * suffix_products[i]
            output.append(ith)
        return output
           



"""
1,2,4,6

prefix=[1,1,2,8]
suffix=[28,24,6,1]


"""
