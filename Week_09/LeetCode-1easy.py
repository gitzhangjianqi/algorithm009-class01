# 387. 字符串中的第一个唯一字符
# 两次循环，暴力解法
import math
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        if len(s) == 1: return 0
        for i in range(len(s)):
            if s[i] in s[i+1:] or s[i] in s[:i]:
                continue
            else:
                return i
        return -1

		
# 541. 反转字符串 II
# 以k为单位，反转字符串，间隔为flag，为true反转，否则不用
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, flag = "", True
        for i in range(0, len(s), k):
            res += s[i:i + k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res 