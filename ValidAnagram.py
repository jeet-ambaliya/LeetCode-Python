class Solution:
    def checkAnagram(self, input1, input2) -> bool:
        dict = {}
        for x in input1:
            dict.update({x: dict.get(x) + 1})

        for x in input2:
            dict.update({x: dict.get(x) - 1})

        for i in dict.keys():
            if dict.get(i) != 0:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()
    ans = obj.checkAnagram("abba", "baa")
    print(ans)
