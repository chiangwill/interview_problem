import math


def plan_exhibition(value, time_arr, max_time):
    """
    Calculates the maximum value achievable by visiting exhibits within max_time,
    with the constraint that viewing exhibit i prevents viewing exhibit i+1.

    Args:
        value: A list of non-negative integers representing the value of each exhibit.
        time_arr: A list of positive integers representing the time needed for each exhibit.
        max_time: The maximum total time allowed.

    Returns:
        The maximum achievable value.

    """

    n = len(value)

    if n == 0:
        return 0

    # dp_view[i][t]: max value considering exhibits 0 to i, VIEWING exhibit i, using exactly t time. Initialized to -1 (impossible).
    dp_view = [[-1] * (max_time + 1) for _ in range(n)]

    # dp_skip[i][t]: max value considering exhibits 0 to i, SKIPPING exhibit i, using exactly t time. Initialized to -1 (impossible).
    dp_skip = [[-1] * (max_time + 1) for _ in range(n)]

    # --- Base Case: Exhibit 0 ---
    # Option 1: Skip exhibit 0
    dp_skip[0][0] = 0  # Takes 0 time, yields 0 value

    # Option 2: View exhibit 0 (if time allows)
    time0 = time_arr[0]
    value0 = value[0]
    if time0 <= max_time:
        dp_view[0][time0] = value0  # Takes time0 time, yields value0 value

    # --- Fill DP tables for exhibits 1 to n-1 ---
    for i in range(1, n):
        time_i = time_arr[i]
        value_i = value[i]

        for t in range(max_time + 1):
            # --- Calculate dp_skip[i][t] ---
            # To skip exhibit i at time t, we must have reached exhibit i-1 also at time t.
            # We could have either viewed or skipped exhibit i-1. Take the max.
            prev_max_at_t = -1

            if dp_skip[i - 1][t] != -1:
                prev_max_at_t = max(prev_max_at_t, dp_skip[i - 1][t])
            if dp_view[i - 1][t] != -1:
                prev_max_at_t = max(prev_max_at_t, dp_view[i - 1][t])

            dp_skip[i][t] = prev_max_at_t

            # --- Calculate dp_view[i][t] ---
            # To view exhibit i at time t:
            # 1. We must have enough time: t >= time_i
            # 2. We must have SKIPPED exhibit i-1.
            # 3. The time before viewing exhibit i was: prev_time = t - time_i
            # 4. The value comes from dp_skip[i-1][prev_time] + value_i

            prev_time = t - time_i
            if prev_time >= 0 and dp_skip[i - 1][prev_time] != -1:

                # If it's possible to reach the required previous state
                current_view_value = dp_skip[i - 1][prev_time] + value_i
                dp_view[i][t] = current_view_value  # Assign the calculated value

    # --- Find the final maximum value ---
    # Look at the last exhibit (n-1). The max value is the highest value achieved
    # across all possible times t (<= max_time), whether we viewed or skipped the last one.
    max_total_value = 0  # Since values are non-negative, the minimum possible value is 0
    for t in range(max_time + 1):
        if dp_skip[n - 1][t] != -1:
            max_total_value = max(max_total_value, dp_skip[n - 1][t])
        if dp_view[n - 1][t] != -1:
            max_total_value = max(max_total_value, dp_view[n - 1][t])

    return max_total_value
