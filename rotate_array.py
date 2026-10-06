class Solution1(object):
    #my orginal solution: i found a solution that only worked when
    # len nums was even so i attempted to bypass this by writing more 
    #lines of code when i shoudlve been tryinbg to better understand
    # what the issue was in the first place
    def rotate(self, nums, k):
        length = len(nums)
        if length % 2 == 0:
            back = nums[-k:] 
            front = nums[:k] 
            nums[-k:] = front
            nums[:k] = back
        else:
            back = nums[-k:] 
            front = nums[:k] 

            middle_index = int(length / 2) + 1


            nums[-k:] = front
            nums[middle_index] = nums[-1]
            nums[:k] = back
            nums = nums.pop()
 
 
        return nums
    
# by using :-k you avoid cutting off elements in the middle
#by using nums[:] it allows you to directly modify the orignal nums without looping
#because [:] means "slice from very beginning to very end"
class Solution2(object):
    def rotate(self, nums, k):
        #this line stops the list rotating endlessly if k is to large
        k = k % len(nums)

        back = nums[-k:] 
        front = nums[:-k] 
        nums[:] = back + front

        return nums
