s = "[{}()]"
# Initialize an empty stack
stack = []
for char in s:
    # Character is an opening bracket, push it onto the stack
    if char in "({[":
        stack.append(char)
    # If the character is a closing bracket
    elif char in ")}]":
        # Check if the stack is empty or the top of the stack does not match the current closing bracket
        if not stack or {')': '(', '}': '{', ']': '['}[char] != stack.pop():
            print(False)  # if there's a mismatch
            break
else:
    # If we didn't break, check if the stack is empty
    print(not stack)
