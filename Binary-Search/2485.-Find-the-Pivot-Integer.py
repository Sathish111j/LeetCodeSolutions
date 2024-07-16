class Solution:
    def pivotInteger(self, n: int) -> int:

        #  Math solution
        # total_sum = n * (n + 1) // 2
        
        # # Calculate the square root of the sum
        # x = int((total_sum) ** 0.5)
        
        # # Check if x is a perfect square 
        # return x if x * x == total_sum else -1

        # if n == 1:
        #     return 1

        
        # Binary Search
        left, right = 1, n
        total_sum = n * (n + 1) // 2

        while left <= right:
            mid = (left + right) // 2
            left_sum = mid * (mid + 1) // 2
            right_sum = total_sum - left_sum + mid

            if left_sum == right_sum:
                return mid
            elif left_sum < right_sum:
                left = mid + 1
            else:
                right = mid - 1

        return -1

