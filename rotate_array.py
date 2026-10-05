class Solution(object):
    def rotate(self, nums, k):
        for i in range(0, k):
            for x in nums:
                if nums[x] == len(nums):
                    nums[0] = x
                else:
                    nums.insert(nums[x + 1], nums.pop(nums[x])
        return nums