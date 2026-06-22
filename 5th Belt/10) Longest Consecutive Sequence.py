# Longest Consecutive Sequence
# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
#
# The algorithm must run in O(n) time.

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start a sequence only if num is the first element
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# Input reading
n = int(input())

if n == 0:
    print(0)
else:
    nums = list(map(int, input().split()))
    print(longestConsecutive(nums))