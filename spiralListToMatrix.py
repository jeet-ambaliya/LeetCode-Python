class Solution:
    def spiralListtoMatrix(self, inputList: list, m, n) -> list:
        print([i for i in range(1,n+1)])
        if not inputList:
            return []
        inputVal = [[0 for _ in range(n)] for _ in range(m) ]

        row = m
        col = n

        t = 0
        b = row - 1
        l = 0
        r = col - 1

        while inputList:
            for x in range(l, r + 1):
                inputVal[l][x] = inputList.pop(0)
            t += 1

            for x in range(t, b + 1):
                inputVal[x][r] = inputList.pop(0)
            r -= 1
            if t <= b:
                for x in range(r, l - 1, -1):
                    inputVal[b][x] = inputList.pop(0)
                b -= 1

            if l <= r:
                for x in range(b, t - 1, -1):
                    inputVal[x][l] = inputList.pop(0)
                l += 1
        return inputVal


if __name__ == "__main__":
    obj = Solution()
    ans = obj.spiralListtoMatrix([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)

    print(ans)
