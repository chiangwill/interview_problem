def longest_same_element_subarray(arr, allow_diff):

    from collections import defaultdict

    n = len(arr)

    left = res = max_count = 0

    char_count = defaultdict(int)

    for right in range(n):
        char_count[arr[right]] = char_count.get(arr[right], 0) + 1
        max_count = max(max_count, char_count[arr[right]])

        while (right - left + 1) - max_count > allow_diff:
            char_count[arr[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


print(longest_same_element_subarray([1, 1, 1, 3, 1, -1, 2, 1, 1, 1], 1))
