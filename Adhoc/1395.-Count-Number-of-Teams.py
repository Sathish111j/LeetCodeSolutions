class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # many diff solution are there 

        # this works but tle

        # n = len(rating)
        # memo = {}
        
        # def backtrack(index, count, prev, increasing):
        #     if count == 3:
        #         return 1
        #     if index == n:
        #         return 0
            
        #     key = (index, count, prev, increasing)
        #     if key in memo:
        #         return memo[key]
            
        #     total = backtrack(index + 1, count, prev, increasing)
            
        #     if count == 0 or (increasing and rating[index] > prev) or (not increasing and rating[index] < prev):
        #         total += backtrack(index + 1, count + 1, rating[index], increasing)
            
        #     memo[key] = total
        #     return total
        
        # return backtrack(0, 0, -1, True) + backtrack(0, 0, float('inf'), False)

        n = len(rating)
        less = [0] * n
        greater = [0] * n
        
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    less[i] += 1
                elif rating[j] > rating[i]:
                    greater[i] += 1
        
        total = 0
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    total += less[j]
                elif rating[j] > rating[i]:
                    total += greater[j]
        
        return total