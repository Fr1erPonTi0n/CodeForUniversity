def brackets(line):
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{", ">": "<"}
    opening_brackets = set(brackets_map.values())
    closing_brackets = set(brackets_map.keys())
    for char in line:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets_map[char] != stack.pop():
                return False
    return not stack
