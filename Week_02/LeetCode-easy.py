# 242. 有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False
        se = set(s)
        if se == set(t):
            for i in se:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False
			
# 1. 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for x in range(len(nums)):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]] = x

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if d.get(target-num) is not None:
                return i,d.get(target-num)
            d[num] = i

# 589. N叉树的前序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, out = [root, ],[]
        while stack:
            root = stack.pop()
            out.append(root.val)
            stack.extend(root.children[::-1])
        return out