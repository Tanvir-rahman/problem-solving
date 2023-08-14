def is_valid_parentheses(s):
    mapping = {"(": ")", "[": "]", "{": "}"}

    stack = []

    for c in s:
        if c in mapping:
            stack.append(mapping[c])
        elif not stack or c != stack.pop():
            return False

    return len(stack) == 0


# Example usage:
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("([)]"))  # False
print(is_valid_parentheses("{[]}"))  # True
