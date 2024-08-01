class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            res.append((bin(i)[2:]).count("1"))
        
        return res

        # ans = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     ans[i] = ans[i >> 1] + (i & 1)
        # return ans