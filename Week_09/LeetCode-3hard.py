# 32. 最长有效括号
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = ' '+s
        dp = [0 for _ in range(len(s))] 
        maxs = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                if i-1 >= 0  and  s[i-1] == '(':
                    if i-1 == 0:
                        dp[i] = 2
                        maxs = max(maxs,dp[i])
                    else:
                        dp[i] = dp[i-2]+2
                        maxs = max(maxs,dp[i])
                elif i-1 >= 0 and s[i-1] == ')':
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                        maxs = max(maxs,dp[i])
        return  maxs