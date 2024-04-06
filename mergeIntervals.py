class Solution:
    def mergeIntervals(self, inputList: list) -> list:
        if not inputList:
            return []
        inputList.sort()
        output = [inputList[0]]

        for x in inputList:
            if output[-1][1] >= x[0]:
                output[-1][1] = max(x[1], output[-1][1])
            else:
                output.append(x)

        return output


if __name__ == "__main__":
    obj = Solution()
    ans = obj.mergeIntervals([[1,4],[2,3]])

    print(ans)
