def simplify_expressions(expressions: str) -> str:

    # dict to record char appear times
    char_count = {}

    # get length of s
    n = len(expressions)

    # sign stack 1 mean '+' and -1 mean '-'
    sign_stack = [1]

    sign = 1

    for char in expressions:  # time complexity O(n) n is length of expression

        if char in '+-':
            sign = 1 if char == '+' else -1
        elif char == '(':
            sign_stack.append(sign * sign_stack[-1])
            sign = 1
        elif char == ')':
            sign_stack.pop()
        elif char.isalpha():
            val = sign * sign_stack[-1] if sign_stack else sign
            char_count[char] = char_count.get(char, 0) + val

    res = []
    for char, count in char_count.items():  # time complexity is O(k) k in numbers of char

        if count == 0:
            continue

        if count == 1:
            exp = f'+{char}' if res else f'{char}'
        elif count == -1:
            exp = f'-{char}'
        else:
            exp = f'+{count}{char}' if res and count > 0 else f'{count}{char}'

        res.append(exp)

    return ''.join(res)


print(simplify_expressions('a+b+c-b-b-b+(d+(a-b))'))
# print(simplify_expressions('a+b+c-b-b-b+(d+(a-b))'))
