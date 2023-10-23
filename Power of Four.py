class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Check if n is a positive integer
        if n <= 0:
            return False
        
        # Check if n is a power of two
        if (n & (n - 1)) != 0:
            return False
        
        # Check if the binary representation of n has an odd number of zeros between the 1s
        binary_n = bin(n)[2:]  # Convert n to binary and remove the '0b' prefix
        count_zeros = binary_n.count('0')
        return count_zeros % 2 == 0

# Example usage:
solution = Solution()
print(solution.isPowerOfFour(16))  # Output: True
print(solution.isPowerOfFour(5))   # Output: False
print(solution.isPowerOfFour(1))   # Output: True
