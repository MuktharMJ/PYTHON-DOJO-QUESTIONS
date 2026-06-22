# Sum of Subarray Minimums
# Given an array of integers arr, find the sum of the minimum value
# of every contiguous subarray.
#
# Since the answer can be very large, return it modulo 10^9 + 7.

class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        ans = 0

        for i in range(n):
            mn = arr[i]

            for j in range(i, n):
                mn = min(mn, arr[j])
                ans = (ans + mn) % MOD

        return ans


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    solution = Solution()
    result = solution.sumSubarrayMins(arr)

    print(result)