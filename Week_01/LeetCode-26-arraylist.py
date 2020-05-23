class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(1, len(nums)) :
            if i >= len(nums) :
                break
            while i < len(nums) and nums[i] == nums[i-1] :
                nums.remove(nums[i])
        
        return len(nums)
