class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        median = len(nums) // 2
        return nums[median]
