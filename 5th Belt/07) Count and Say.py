# Count and Say
# The count-and-say sequence is defined recursively:
#
# countAndSay(1) = "1"
# countAndSay(n) is obtained by reading off the digits
# of countAndSay(n - 1).
#
# Example:
# "1" -> "11"
# "11" -> "21"
# "21" -> "1211"

def countAndSay(n):
    if n == 1:
        return "1"

    result = "1"

    for _ in range(2, n + 1):
        current = ""
        count = 1

        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1
            else:
                current += str(count) + result[i - 1]
                count = 1

        current += str(count) + result[-1]
        result = current

    return result


n = int(input())
print(countAndSay(n))