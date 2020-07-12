# 191. 位1的个数
# bin函数转为二进制，count计算字符串出现的次数
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count("1")

        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count
		
# 231. 2的幂
# 位运算，移位
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        while n > 1:
            n = n/2
        return n == 1
        """
        return n > 0 and n & (n - 1) == 0