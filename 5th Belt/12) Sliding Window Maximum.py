# Sliding Window Maximum
# You are given an array of integers nums and a sliding window
# of size k that moves from the left of the array to the right.
# For each window, find the maximum element.
#
# Print the maximum value for each window.

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

result = maxSlidingWindow(arr, k)

print(" ".join(map(str, result)))