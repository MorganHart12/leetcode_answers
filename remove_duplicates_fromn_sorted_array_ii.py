class Solution(object):
    def removeDuplicates(self, nums):
        count = 2
        for x in range(1, len(nums)):
                if nums[x] != nums[count- 2]:
                    nums[count] = nums[x]
                    count += 1

                    
            
        return count