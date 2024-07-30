class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack=[]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        indicesToRemove = set(stack)

        result = []
        for i in range(len(s)):
            if i not in indicesToRemove:
                result.append(s[i])
        
        return "".join(result)


