# 64. 最小路径和
# 从第一行开始逐个遍历，找到从[0][0]到该位子的最小路径，直到[-1][-1]返回
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if row == 0 and column == 0: continue
                if row == 0 and column > 0:
                    grid[0][column] += grid[0][column-1]
                else:
                    if column == 0:
                        grid[row][column] += grid[row-1][column]
                    else:
                        grid[row][column] += min(grid[row-1][column], grid[row][column-1])
        
        return grid[-1][-1]