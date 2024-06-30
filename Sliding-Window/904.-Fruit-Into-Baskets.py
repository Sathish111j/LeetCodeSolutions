class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        distinct_fruits = {}
        max_length = 0
        left = 0

        for right in range(len(fruits)):

            if fruits[right] in distinct_fruits:
                distinct_fruits[fruits[right]] += 1
            else:
                distinct_fruits[fruits[right]] = 1
                
            if len(distinct_fruits) > 2:
                distinct_fruits[fruits[left]] -= 1
                if distinct_fruits[fruits[left]] == 0:
                    del distinct_fruits[fruits[left]]
                    
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length