class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        c_num = 0
        c_str = ""
        
        for char in s:
            if char.isdigit():
                c_num = c_num * 10 + int(char) 
            elif char == '[':
                stack.append((c_str, c_num))
                c_str = ""
                c_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                c_str = last_str + c_str * num
            else:
                c_str += char
        
        return c_str
