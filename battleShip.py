class Solution:
    def battleShip(self, matrix: list) -> list:

        count = 0
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 'X':
                    if (i == 0 or matrix[i-1][j] == '.') and (j == 0 or matrix[i][j-1] == '.'):
                        count += 1

        return count


if __name__ == "__main__":
    obj = Solution()
    ans = obj.battleShip([["."]])

    print(ans)
