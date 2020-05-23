class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        k %= lenth

        nums[:] = nums[lenth-k:] + nums[:lenth-k]

        # for _ in range(k) :
        #     nums.insert(0, nums.pop())
