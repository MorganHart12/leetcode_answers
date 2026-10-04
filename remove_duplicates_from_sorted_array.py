class Solution(object):
    def removeDuplicates(self, nums):
        count = 1
        for x in range(1, len(nums)):
            if nums[x] != nums[x - 1]:
                nums[count] = nums[x]
                count += 1

        return count