#Leetcode # 20
#My solution: 4/6/2023
#Problem Difficulty Level: Medium

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashM = {"}":"{",
                 ")":"(",
                 "]":"["}
                 
        for char in s:
            if char not in hashM:
                stack.append(char)
            else:
                if stack and stack[-1] == hashM[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False