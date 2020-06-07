# 70. 爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 3): return n
        v1, v2, v3 = 1, 2, 3
        for i in range(4, n+1):
            v1, v2 = v2, v3
            v3 = v1 + v2
        return v3