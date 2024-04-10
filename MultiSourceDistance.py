from collections import deque


class Solution:
    def rottingOrranges(self, inputList: list[list]) -> int:

        locQueue = deque()
        total = 0

        for i, row in enumerate(inputList):
            for j, cell in enumerate(row):
                if cell == 'X':
                    locQueue.append((i, j))
                    total += 1

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while len(locQueue) > 0:
            count = 1
            row, col = locQueue.popleft()
            queue = deque()
            queue.append((row,col))
            visited = []

            while len(queue) > 0:

                x,y = queue.popleft()

                for dr, dc in direction:
                    r = dr + x
                    c = dc + y

                    if 0 <= r < len(inputList) and 0 <= c < len(inputList[0]) and inputList[r][c] != "X" and (r,c) not in visited:

                        if inputList[r][c] == '':
                            val = "{}".format(count)
                            inputList[r][c] = val
                            visited.append((r, c))
                        else:

                            val1 = int(inputList[r][c])
                            inputList[r][c] = "{}".format(min(count, val1))

                        queue.insert(0,(r, c))
                        visited.append((r,c))
                count += 1
        return inputList


if __name__ == "__main__":
    obj = Solution()
    ans = obj.rottingOrranges([['X','','','','', 'X'], ['X','','','','', 'X']])

    print(ans)
