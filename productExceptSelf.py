class Solution:
    def productExceptSelf(self, inputList: list) -> list:
        if not inputList:
            return []

        left = [1] * len(inputList)
        right = [1] * len(inputList)

        for x in range(1, len(left)):
            left[x] = left[x - 1] * inputList[x - 1]

        for x in range(len(right) - 2, -1, -1):
            right[x] = right[x + 1] * inputList[x + 1]

        for x in range(len(inputList)):
            inputList[x] = left[x] * right[x]

        return inputList

    def productExceptSelfOptimal(self, inputList: list) -> list:
        if not inputList:
            return []

        out = [1] * len(inputList)

        for x in range(1, len(out)):
            out[x] = out[x - 1] * inputList[x - 1]

        suff = 1
        for x in range(len(out) - 2, -1, -1):
            suff *= inputList[x + 1]
            out[x] = out[x] * suff

        return out


if __name__ == "__main__":
    obj = Solution()
    ans = obj.productExceptSelf([-1, 1, 0, -3, 3])

    print(ans)
