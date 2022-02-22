def preemptive(jobs):
    """
        use preemptive approach
    """
    n = len(jobs)
    gantt = []
    jobs.sort(key=lambda job: (job[2], job[1]))
    current_time = jobs[0][2]
    arrived = [job for job in jobs if job[2] <= current_time]
    remaining = [job for job in jobs if job[2] > current_time]
    finished = []

    finished_jobs = 0
    while finished_jobs < n:
        if remaining:
            next_time = remaining[0][2]
        else:
            if arrived:
                next_time = current_time + arrived[0][7]
            else: break
        
        start = current_time
        if arrived[0][4] == None:
            arrived[0][4] = current_time
        finish = current_time + arrived[0][7]

        if next_time < finish:
            processed_time = next_time - current_time
            arrived[0][7] -= processed_time
            current_time = next_time
        else:
            arrived[0][7] = 0
            finished_jobs += 1
            current_time = next_time

        if arrived:
            gantt.append([arrived[0][0], start, finish])

        if arrived[0][7] == 0:
            arrived[0][5] = current_time
            finished.append(arrived.pop(0))

        arrived += [job for job in remaining if job[2] <= current_time]
        remaining = [job for job in jobs if job[2] > current_time]

        arrived.sort(key=lambda job: job[1])
        
    finished.sort(key=lambda job: job[0])
    return finished, gantt