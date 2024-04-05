from collections import deque


class Solution:
    def checkParenthesis(self, inputVal) -> bool:
        values = deque()
        for i in inputVal:
            if i == '(':
                values.append(')')
            else:
                if values:
                    values.pop()
                else:
                    return False

        return len(values) == 0

    def checkParenthesisOptimal(self, inputVal) -> bool:

        counter = 0

        for i in inputVal:
            if i == '(':
                counter += 1
            else:
                counter -= 1
                if counter < 0:
                    return False

        return counter == 0


if __name__ == "__main__":
    obj = Solution()
    ans = obj.checkParenthesis(")")
    ans1 = obj.checkParenthesisOptimal(")")
    print(ans)
    print(ans1)
