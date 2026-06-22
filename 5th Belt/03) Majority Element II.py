# Majority Element II
# Given an integer array nums of size n, find all elements that
# appear more than ⌊n/3⌋ times.
#
# Return all such elements in any order.

def majorityElement(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    result = []

    for num in count:
        if count[num] > len(nums) // 3:
            result.append(num)

    return result


# Input format handling
n = int(input())  # Size of the array
nums = list(map(int, input().split()))  # Elements of the array

# Get the majority elements
result = majorityElement(nums)

# Print the output based on the length of the result
if len(result) == 1:
    print(result[0])  # Single majority element
else:
    print(" ".join(map(str, result)))  # Multiple majority elements if applicable