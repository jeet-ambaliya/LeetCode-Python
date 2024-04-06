class Solution:
    def mergeTwoSortedArray(self, inputList1: list, inputList2: list) -> list:
        if not inputList1:
            return inputList2

        i = 0
        while len(inputList2) > 0:
            val = inputList2[0]
            if i >= len(inputList1):
                break
            if inputList1[i] >= val:
                inputList1.insert(i, val)
                inputList2.pop(0)
                i+=1

            i += 1

        if len(inputList2) != 0:
            return inputList1 + inputList2
        return inputList1


if __name__ == "__main__":
    obj = Solution()
    ans = obj.mergeTwoSortedArray([1, 2, 3], [1,2,7, 8, 9])

    print(ans)
