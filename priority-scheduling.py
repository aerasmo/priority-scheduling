import random

jobs = []
gantt = []

# ranomized jobs
random.seed(17)
# no. of jobs
n = random.randint(3,6)

# initialize jobs
for i in range(n):
    process_name = "p{}".format((i + 1))
    priority = random.randint(1, 4)
    arrival_time = random.randint(0, 10)
    burst_time = random.randint(1, 10)
    jobs.append([process_name, priority, arrival_time, burst_time, None, None, 0, burst_time])

# jobs = [
#     ['p1', 2, 0, 11],
#     ['p2', 2, 5, 28],
#     ['p3', 3, 12, 2],
#     ['p4', 3, 2, 10],
#     ['p5', 4, 9, 16],
# ]
# n = len(jobs)
# new_jobs = []
# for job in jobs:
#     new_jobs.append([] + job + [None, None, 0, job[-1], None])

# jobs = new_jobs

def non_preemptive(jobs):
    # work the jobs
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
        # current + burst
        if arrived[0][4] == None:
            arrived[0][4] = current_time

        finish = current_time + arrived[0][7]
        current_time = finish
        arrived[0][7] = 0
        arrived[0][5] = current_time
        finished_jobs += 1

        if arrived:
            gantt.append([arrived[0][0], start, finish])

        if next_time > finish:
            current_time = next_time

        finished.append(arrived.pop(0))

        # arrived = [job for job in arrived if job[2] <= current_time] +\
        arrived += [job for job in remaining if job[2] <= current_time]
        remaining = [job for job in jobs if job[2] > current_time]

        arrived.sort(key=lambda job: job[1])

    finished.sort(key=lambda job: job[0])
    return finished

def preemptive(jobs):
    # work the jobs
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
        # current + burst
        if arrived[0][4] == None:
            arrived[0][4] = current_time
        finish = current_time + arrived[0][7]
        # burst time 
        if next_time < finish:
            processed_time = next_time - current_time
            arrived[0][7] -= processed_time
            current_time = next_time
        else: # next_time >= finish
            current_time = finish
            arrived[0][7] = 0
            finished_jobs += 1

        # arrived = [job for job in arrived if job[2] <= current_time] +\
        if arrived:
            gantt.append([arrived[0][0], start, current_time])

        if arrived[0][7] == 0:
            arrived[0][5] = current_time
            finished.append(arrived.pop(0))

        arrived += [job for job in remaining if job[2] <= current_time]
        remaining = [job for job in jobs if job[2] > current_time]

        if not arrived:
            arrived += [job for job in remaining if job[2] <= next_time]
            remaining = [job for job in jobs if job[2] > next_time]

        arrived.sort(key=lambda job: job[1])
        
    # get waiting time 
    finished.sort(key=lambda job: job[0])
    return finished


def print_table(jobs):
    print("{}{}{}{}{}{}".format(
        "Job".ljust(7), 
        "Priority".ljust(10), 
        "Arrival Time".ljust(15),
        "Burst Time".ljust(15),
        "Start Time".ljust(15),
        "Finish Time".ljust(15),
    ))
    for job in jobs:
        print("{}{}{}{}{}{}".format(
            job[0].ljust(7), # name
            str(job[1]).ljust(10), # priority
            str(job[2]).ljust(15), # at
            str(job[3]).ljust(15), # bt
            str(job[4]).ljust(15), # start
            str(job[5]).ljust(15), # finish
        ))

if __name__ == "__main__":
    jobs = non_preemptive(jobs)
    # jobs = preemptive(jobs)

    print("RESULT")
    print_table(jobs)
    print("GANTT CHART")
    print(gantt)
