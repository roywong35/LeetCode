def countBinarySubstrings(s: str) -> int:
    count = []
    total = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            total += 1
        else:
            count.append(total)
            total = 1
    count.append(total)

    res = 0
    for i in range(len(count) - 1):
        res += min(count[i], count[i + 1])
    return res

print(countBinarySubstrings("00111000011"))

def countBinarySubstrings(s: str) -> int:
    count = 0
    prev = 0
    curr = 1
    n = len(s)

    for i in range(1, n):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            prev = curr
            curr = 1

        if prev >= curr:
            count += 1
    return count

print(countBinarySubstrings("00111000011"))