def canChange(start, target):

    if start.replace('_', '') != target.replace('_', ''):
        return False

    start_L = [idx for idx, char in enumerate(start) if char == 'L']
    start_R = [idx for idx, char in enumerate(start) if char == 'R']
    target_L = [idx for idx, char in enumerate(target) if char == 'L']
    target_R = [idx for idx, char in enumerate(target) if char == 'R']

    for s, t in zip(start_L, target_L):
        if s < t:
            return False

    for s, t in zip(start_R, target_R):
        if s > t:
            return False

    return True


print(canChange("_L__R__R_", "L______RR"))
print(canChange("R_L_", "__LR"))
print(canChange("_R", "L_"))
