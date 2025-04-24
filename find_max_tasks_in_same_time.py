def find_max_tasks_in_same_time(events):

    if not events:
        return 0

    max_task = curr_task = 0
    events.sort(key=lambda x: (x[0], 0 if x[2] == "START" else 1))

    for event in events:
        _, task, action = event

        if action == 'START':
            curr_task += 1
            max_task = max(max_task, curr_task)
        elif action == 'END':
            curr_task -= 1

    return max_task


print(find_max_tasks_in_same_time([(1, "taskA", "START"), (6, "taskA", "END"), (3, "taskB", "START"), (7, "taskC", "START"), (8, "taskB", "END"), (10, "taskC", "END")]))
