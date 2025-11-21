def isPalindrome(s: str) -> bool:
    filtered = "".join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

print(isPalindrome(s = "A man, a plan, a canal: Panama"))