import collections
from collections import deque


class Solution:
    def noOfIslandIterative(self, inputList: list[list]) -> int:

        if len(inputList) == 0:
            return 0

        islands = 0
        visit = set()

        def dfs(r, c, size):
            size += 1
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if r in range(len(inputList)) and c in range(len(inputList[0])) and inputList[r][c] == "1" and (
                    r, c) not in visit:
                        size += 1
                        q.append((r, c))
                        visit.add((r, c))

            return size

        maxSize = 0
        islandSize = []
        size = 0
        for i, line in enumerate(inputList):
            for j, cell in enumerate(line):
                if cell == "1" and (i, j) not in visit:
                    size = dfs(i, j, 0)
                    islands += 1
                    maxSize = max(maxSize, size)

        return islands, maxSize

    def noOfIslandRecursive(self, inputList: list[list]) -> int:

        if len(inputList) == 0:
            return 0

        islands = 0

        def dfs(grid, r, c, size):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return 0

            size += 1
            grid[r][c] = '0'

            size += dfs(grid, r, c - 1, 0)
            size += dfs(grid, r - 1, c, 0)
            size += dfs(grid, r, c + 1, 0)
            size += dfs(grid, r + 1, c, 0)

            return size

        maxSize = 0
        for i, line in enumerate(inputList):
            for j, cell in enumerate(line):
                if cell == "1":
                    islands += 1
                    island_size = dfs(inputList, i, j, 0)
                    maxSize = max(maxSize, island_size)  # Update maxIsland if needed

        return islands, maxSize


if __name__ == "__main__":
    obj = Solution()
    ans, maxSize = obj.noOfIslandRecursive([["1", "1", "1", "1", "0"],
                                   ["1", "1", "0", "1", "0"],
                                   ["1", "1", "0", "0", "0"],
                                   ["0", "0", "0", "0", "1"]
                                   ])

    print(ans)
    print(maxSize)
