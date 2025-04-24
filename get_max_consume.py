import heapq


def get_max_consume(tasks):
    '''
    time complexity: O(nlogn)
    space complexity: O(n)
    '''

    tasks.sort(key=lambda x: x[0])

    min_heap = []
    curr_consume = max_consume = 0

    for start, end, consume in tasks:

        while min_heap and min_heap[0][0] <= start:
            _, ended_task_value = heapq.heappop(min_heap)
            curr_consume -= ended_task_value

        curr_consume += consume

        heapq.heappush(min_heap, (end, consume))

        max_consume = max(curr_consume, max_consume)

    return max_consume

    # new_task = []

    # for start_time, end_time, consume in tasks:
    #     new_task.append([start_time, consume])
    #     new_task.append([end_time, -consume])

    # new_task.sort(key=lambda x: (x[0], x[1]))
    # max_consume = curr_consume = 0

    # for task in new_tasks:
    #     _, consume = task

    #     curr_consume += consume
    #     max_consume = max(max_consume, curr_consume)

    # return max_consume


print(get_max_consume([[1, 5, 3], [2, 4, 5], [6, 8, 2], [3, 7, 4]]))
print(get_max_consume([[1, 5, 3], [6, 8, 4]]))
print(get_max_consume([[1, 10, 2], [2, 4, 3], [5, 7, 4]]))
print(get_max_consume([[1, 3, 2], [3, 5, 4]]))
