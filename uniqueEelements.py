from collections import deque, Counter


class Solution:
    def uniqueEelemets(self, inputVal: list) -> int:
        return len(Counter(inputVal))

    def uniqueEelemetsSet(self, inputVal: list) -> int:
        return len(set(inputVal))

    def uniqueElementsListofLists(self, inputVal) -> int:
        # List of Lists needs to be converted to tuple because lists are mutable and set cannot accept mutable data
        values = [tuple(val) for val in inputVal]
        return len(set(values))

if __name__ == "__main__":
    obj = Solution()
    ans = obj.uniqueEelemets([1,1,1,2,1,3,4])
    ans1 = obj.uniqueEelemetsSet([1,1,1,2,1,3,4])
    ans2 = obj.uniqueElementsListofLists([[1, 2], [1, 2], [3, 4], [3, 4]])

    print(ans)
    print(ans1)
    print(ans2)

