'''
You have a very very big number 2123470299109372 and a given integer k [let's say k=6]
you need to find largest k digit number which is a subsequence of the original number. ans=999372
'''


def find_largest_number(number, k):
    stack = []
    n = len(number)
    remain = n - k

    for digit in number:
        while stack and remain > 0 and digit > stack[-1]:
            stack.pop()
            remain -= 1

        stack.append(digit)

    return ''.join(stack)


print(find_largest_number('2123470299109372', 6))
print(find_largest_number('225457', 3))
