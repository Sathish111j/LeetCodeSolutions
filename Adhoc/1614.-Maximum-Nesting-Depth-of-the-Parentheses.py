class Solution:
    def maxDepth(self, s: str) -> int:
        m_depth = 0
        c_depth = 0
        
        for c in s:
            if c == '(':
                c_depth += 1
                if c_depth > m_depth:
                    m_depth = c_depth
            elif c == ')':
                c_depth -= 1
        
        return m_depth
            
