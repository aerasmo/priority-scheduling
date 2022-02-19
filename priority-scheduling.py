import random

# non preemptive 
random.seed(16)
jobs = []
gantt = []
# no. of jobs
n = random.randint(3,6)
# initialize jobs
for i in range(n):
    process_name = "p{}".format((i + 1))
    priority = random.randint(1, 4)
    arrival_time = random.randint(0, 10)
    burst_time = random.randint(1, 10)
    jobs.append([process_name, priority, arrival_time, burst_time, None, None, None, 0])


# work the jobs
jobs.sort(key=lambda job: (job[2], job[1]))
current_time = jobs[0][2]

# process
# if job is available and not finish
finished_jobs = 0

while finished_jobs < n:
    # sort by priority
    for job in jobs:
        if job[2] <= current_time and job[5] == None:
            # start time
            start_time = current_time
            if job[4] == None:
                job[4] = start_time

            # finish time 
            job[7] += job[3]
            finish_time = start_time + job[3] 

            if job[7] == job[3]:
                job[5] = finish_time
                job[6] = job[4] - job[2]
                finished_jobs += 1
                
            current_time = finish_time


            gantt.append([job[0], start_time, finish_time])
    jobs.sort(key=lambda job: (job[2], job[1]))

def print_table():
    print("{}{}{}{}{}{}{}".format(
        "Job".ljust(7), 
        "Priority".ljust(10), 
        "Arrival Time".ljust(15),
        "Burst Time".ljust(15),
        "Start Time".ljust(15),
        "Finish Time".ljust(15),
        "Waiting Time".ljust(15),
    ))
    for job in jobs:
        print("{}{}{}{}{}{}{}".format(
            job[0].ljust(7), # name
            str(job[1]).ljust(10), # priority
            str(job[2]).ljust(15), # at
            str(job[3]).ljust(15), #  bt
            str(job[4]).ljust(15), # start
            str(job[5]).ljust(15), # finish
            str(job[6]).ljust(15), # wait time
        ))

print_table()
print(gantt)
