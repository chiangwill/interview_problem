from collections import Counter, defaultdict


def find_longest_subarray_in_k_item(logs, k):

    if not logs or len(Counter(logs)) < k:
        return 0

    log_count = defaultdict(int)
    n = len(logs)
    left = res = 0

    for right in range(n):
        log_count[logs[right]] += 1

        while len(log_count) > k:
            log_count[logs[left]] -= 1
            if log_count[logs[left]] == 0:
                del log_count[logs[left]]

            left += 1

        res = max(res, (right - left + 1))

    return res


print(find_longest_subarray_in_k_item([1, 2, 1, 3, 1, 2, 4], 2))
