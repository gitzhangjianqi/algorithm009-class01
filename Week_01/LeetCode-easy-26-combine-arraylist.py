"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(1, len(nums)) :
            if i >= len(nums) :
                break
            while i < len(nums) and nums[i] == nums[i-1] :
                nums.remove(nums[i])
        
        return len(nums)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)) :
            if nums[i] > nums[index] :
                index += 1
                nums[index] = nums[i]
        nums = nums[0:index+1]
        return len(nums)
