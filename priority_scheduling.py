import random
from preemptive import preemptive
from non_preemptive import non_preemptive

def generate_jobs(seed, nmin, nmax):
    """
        generate jobs matrix to be used 
    """
    jobs = []
    gantt = []
    random.seed(seed)
    n = random.randint(nmin,nmax)
    for i in range(n):
        process_name = "p{}".format((i + 1))
        priority = random.randint(1, 4)
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        jobs.append([process_name, priority, arrival_time, burst_time, None, None, 0, burst_time])
    return jobs

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

def test(n):
    """
        test for errors
    """
    for i in range(n):
        jobs = generate_jobs(i, 3, 6)
        solve(jobs, "p")
        solve(jobs, "np")

def solve(jobs, strategy):
    job_table, job_gantt = [], []
    if strategy.lower() == "p":
        strat = "preemptive"
        job_table, job_gantt = preemptive(jobs)
    elif strategy.lower() == "np":
        strat = "non-preemptive"
        job_table, job_gantt = non_preemptive(jobs)
    else:
        print("Invalid op")

    if job_table and job_gantt:
        print("RESULT ({})".format(strat))
        print_table(job_table)
        print("GANTT CHART")
        print(job_gantt)

def main():
    jobs = generate_jobs(17, 3, 6)
    strategy = input("Select process (p-preemptive, np-nonpreemptive): ")
    solve(jobs, strategy)

if __name__ == "__main__":
    # main()
    test(30)
