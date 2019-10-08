"""
Question:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Solution:
    unsorted - sort first
    repetition - skip repetition
    a + b = - c, so given any a and b pair, find -c
    set flag = -a, then from (a, rightmost], use j=[a] and k=[rightmost] to find the tuple
"""


class Solution:
    def threeSum(self, nums):
        if len(nums) <= 2:
            return []

        res = []
        nums.sort()

        for i in range(len(nums)-2):
            # skip repetition
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # set -a
            flag = -nums[i]

            j, k = i+1, len(nums)-1
            # searching
            while j < k:
                if nums[j] + nums[k] == flag:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j] + nums[k] > flag:
                    k -= 1
                else:
                    j += 1

        return res


test = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(test.threeSum(nums))
