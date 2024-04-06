from collections import deque, Counter


class Solution:
    def spiralMatrix(self, inputVal: list[list]) -> list:
        if not inputVal:
            return []
        output = []

        row = len(inputVal)
        col = len(inputVal[0])

        t = 0
        b = row - 1
        l = 0
        r = col - 1

        while len(output) < row * col:
            for x in range(l, r + 1):
                output.append(inputVal[l][x])
            t += 1

            for x in range(t, b + 1):
                output.append(inputVal[x][r])
            r -= 1
            if t <= b:
                for x in range(r, l - 1, -1):
                    output.append(inputVal[b][x])
                b -= 1

            if l <= r:
                for x in range(b, t - 1, -1):
                    output.append(inputVal[x][l])
                l += 1
        return output


if __name__ == "__main__":
    obj = Solution()
    ans = obj.spiralMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(ans)
