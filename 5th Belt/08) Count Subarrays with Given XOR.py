# Count Subarrays with Given XOR
# Given an array of integers arr[] and a number m,
# count the number of subarrays having XOR of their
# elements equal to m.
#
# Input:
# First line contains an integer n, the size of the array.
# Second line contains n space-separated integers.
# Third line contains an integer m.
#
# Output:
# Return a single integer, the count of subarrays
# having XOR equal to m.

def subarray_xor(arr, n, m):
    count = 0
    xor = 0

    # Frequency map for prefix XOR values
    freq = {0: 1}

    for num in arr:
        xor ^= num

        if xor ^ m in freq:
            count += freq[xor ^ m]

        freq[xor] = freq.get(xor, 0) + 1

    return count


# Reading input
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# Compute and print the result
print(subarray_xor(arr, n, m))