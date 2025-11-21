def isValid(s: str) -> bool:
    pairs = {"(":")", "{":"}", "[":"]"}
    stack = []
    
    for x in s:
        if x in pairs:
            stack.append(pairs[x])
        else:
            if stack and x == stack[-1]:
                stack.pop()
            elif not stack or x != stack[-1]:
                return False
                
    return True if len(stack) == 0 else False

print(isValid(s = "()[]{}"))