class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Initialize the result as x
        res = x
        i_x = 1  # Bitwise mask starting from the least significant bit
        i_n = 1  # Keeps track of powers of 2 to apply bitwise shifts

        # Iterate to find the minimum ending number in the array
        while i_n <= n - 1:
            # If the current bit in x is 0, try to set it in res if possible
            if i_x & x == 0:
                # Ensure that i_n has bits in common with n-1
                if i_n & (n - 1):
                    res = res | i_x  # Set the bit in res
                i_n = i_n << 1  # Move to the next bit position
            i_x = i_x << 1  # Move to the next bit position in i_x

        return res
