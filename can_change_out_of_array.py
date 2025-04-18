def canChange(start, target):

    from collections import defaultdict, deque

    char_count = defaultdict(deque)

    for idx, char in enumerate(start):
        if char not in char_count:
            char_count[char] = deque()

        char_count[char].append(idx)

    print(char_count)


# print(canChange("_L__R__R_", "L______RR"))
# print(canChange("R_L_", "__LR"))
# print(canChange("_R", "L_"))
print(canChange("_L_LRL_R_", "____"))
