# Beautiful Arrangement
# Given an integer n, count the number of beautiful arrangements
# that can be formed using numbers from 1 to n.
#
# A beautiful arrangement is an arrangement where:
# - perm[i] is divisible by i, or
# - i is divisible by perm[i]
#
# Return the total number of beautiful arrangements.

def countArrangement(n):

    # Track which numbers are already used
    used = [False] * (n + 1)

    # Try filling positions one by one
    def backtrack(pos):

        # Found a valid arrangement
        if pos > n:
            return 1

        count = 0

        # Try every unused number
        for num in range(1, n + 1):

            # Check arrangement condition
            if not used[num] and (num % pos == 0 or pos % num == 0):

                # Choose
                used[num] = True

                # Explore
                count += backtrack(pos + 1)

                # Backtrack
                used[num] = False

        return count

    return backtrack(1)


n = int(input())

print(countArrangement(n))