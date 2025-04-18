'''
You are given an array time[] representing the start times of a set of tasks. Each task takes 6 units of time to complete once it starts. You are also given an integer C representing the number of CPUs available. Each CPU can only handle one task at a time.

Your goal is to schedule all the tasks such that the total time to complete all tasks is minimized.

Return the minimum time at which all tasks will be completed.

Example :-
Input: time = [1, 3, 6], C = 2
Output: 13
'''


def min_completion_time(times, cpu):

    import heapq

    times.sort()

    cpu_queue = []

    for start_time in times:

        if len(cpu_queue) < cpu:
            heapq.heappush(cpu_queue, start_time + 6)
        else:
            task_finish_time = heapq.heappop(cpu_queue)
            next_start_time = max(task_finish_time, start_time)
            heapq.heappush(cpu_queue, next_start_time + 6)

    return max(cpu_queue)


print(min_completion_time([1, 6, 7, 13], 4))
