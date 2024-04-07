from collections import deque


class Solution:
    def rottingOrranges(self, inputList: list[list]) -> int:

        rottenQueue = deque()
        time = 0
        fresh = 0

        for i, row in enumerate(inputList):
            for j, cell in enumerate(row):
                if cell == 2:
                    rottenQueue.append((i, j))
                if cell == 1:
                    fresh += 1

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while fresh and len(rottenQueue) > 0:

            for i in range(len(rottenQueue)):
                row, col = rottenQueue.popleft()

                for dr, dc in direction:
                    r, c = dr + row, dc + col

                    if r < 0 or r == len(inputList) or c < 0 or c == len(inputList[0]) or inputList[r][c] != 1:
                        continue

                    inputList[r][c] = 2
                    rottenQueue.append((r, c))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1


if __name__ == "__main__":
    obj = Solution()
    ans = obj.rottingOrranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]])

    print(ans)
