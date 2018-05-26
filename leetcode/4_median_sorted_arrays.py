import math
'''
possibly different lengths
couple caes
1) partially overlapping ranges [1,2,3,8] and [4,5,6,7,10,11]
2) non-overlapping [1,2,3] and [6,7,8,9,10,11,50]
    -concatenate them and find the middle or middle 2 elements


NOTE: can be very different in length
[1,2,3,4,5,6,7,8,9,10] and [4]

ex [1,3] and [2]


how to cut each input array in half?

idea: find median of each individual list (easy)

h = number of items higher than higher median
l = number of ieams lower than lower median
n = min(l, h)
remove n items higher than higher median, and lower than lower median


[1,2,3,4,5,6,7,8,9,10] and [-10, -9, -8, 0, 101, 102, 103, 104, 105]

[1,2,3,4,5,6,7,8,9,10] and [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
median = 5.5 and 16
remove 4 items below and above?


BASE: middle of nums1 == middle nums2
or length

once one of the lists gets to a single element, just insert it into

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # one is empty
        if len(nums1) == 0:
            return self.get_median_single_sorted_list(nums2)
        elif len(nums2) == 0:
            return self.get_median_single_sorted_list(nums1)

        # if either has 2 or fewer elements, insert into other list and find median
        if len(nums1) <= 2 or len(nums2) <= 2:
            if len(nums1) <= 2:
                source = nums1
                l = nums2
            elif len(nums2) <= 2:
                source = nums2
                l = nums1

            while len(source) > 0:
                s = source.pop()
                l = self.insert_element_into_sorted_list(s, l)

            return self.get_median_single_sorted_list(l)

        num_to_remove = min(
            self.calc_num_to_remove(nums1),
            self.calc_num_to_remove(nums2)
        )

        median1 = self.get_median_single_sorted_list(nums1)
        median2 = self.get_median_single_sorted_list(nums2)

        if median1 > median2:
            nums1 = nums1[:len(nums1) - num_to_remove]
            nums2 = nums2[num_to_remove:]
        else:
            nums1 = nums1[num_to_remove:]
            nums2 = nums2[:len(nums2) - num_to_remove]

        return self.findMedianSortedArrays(nums1, nums2)

    def calc_num_to_remove(self, nums):

        l = len(nums)

        if l % 2 == 0:
            half = l / 2 - 1
        else:
            half = math.floor(l / 2)

        return int(half)

    def get_median_single_sorted_list(self, nums):
        if len(nums) == 1:
            median = nums[0]
        elif len(nums) % 2 == 0:
            i_high = int(len(nums) / 2)
            i_low = i_high - 1
            median = (nums[i_high] + nums[i_low]) / 2
        else:
            i = math.floor(len(nums) / 2)
            median = nums[i]

        return float(median)

    def insert_element_into_sorted_list(self, e, l):
        if len(l) == 0:
            return [e]

        i = math.floor(len(l) / 2)

        if e > l[i]:
            return l[:i + 1] + self.insert_element_into_sorted_list(e, l[i + 1:])
        else:
            return self.insert_element_into_sorted_list(e, l[:i]) + l[i:]



nums1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
# nums1 = [1,3]
nums2 = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,101,102,103,104,105,106]
# nums2 = [2]



nums1 = [1,2,6,7]
nums2 = [3,4,5,8]
s = Solution()

m = s.findMedianSortedArrays(nums1, nums2)
print(m)

# l = s.insert_element_into_sorted_list(4, nums2)
# print(l)
