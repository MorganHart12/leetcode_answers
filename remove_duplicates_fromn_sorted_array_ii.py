class Solution(object):
    def removeDuplicates(self, nums):
        count = 1
        temp = 0
        for x in range(1, len(nums)):
            for y in range(2, len(nums)):
                if nums[y] == nums[x] == nums[x - 1]:
                    nums[count] = nums[x]
                    count += 1

   
                    
            
        return count
              