# Description
# The GoCJ dataset is comprised of different files. Each file contains the sizes of a specified number of jobs in terms 
# of Million Instructions (MI) derived from the workload behaviors witnessed in google cluster traces (surveys published). 
# The name of the file determines the number of jobs within the file i.e.; GoCJ_Dataset_100 has the sizes of 100 jobs. The 
# GoCJ dataset is accepted for publication in MDPI Data journal, the citation of the article will be provied very soon. Moreover, 
# the GoCJ dataset (i..e named as Google-like realistic dataset) is used in the following research work of the author.
# https://data.mendeley.com/datasets/b7bp6xhrcd/1

from mpi4py import MPI

def mct_parallel(jobs, rank, size):
    # Calculate the number of jobs to be processed by each MPI process
    chunk_size = len(jobs) // size  # 100//8 = 12, 
    start_index = rank * chunk_size # 0 * 12 = 0, 1*12 = 12,... 84
    end_index = start_index + chunk_size if rank < size - 1 else len(jobs) # 0 + 12 if 0 < 8-1=7 else 100, 24, ... 100

    # Initialize metrics
    start_times = {}
    completion_times = {}
    turnaround_times = {}
    waiting_times = {}
    makespan = 0

    # Assign each job to the processor with the earliest completion time
    current_time = 0
    for job_index, job_size in jobs[start_index:end_index]:
        # Calculate start time
        start_times[job_index] = current_time
        
        # Update completion time and makespan
        completion_times[job_index] = current_time + job_size
        current_time += job_size
        makespan = max(makespan, completion_times[job_index])

    # Calculate turnaround time and waiting time
    total_turnaround_time = 0
    total_waiting_time = 0
    for job_index in start_times:
        turnaround_times[job_index] = completion_times[job_index] - start_times[job_index]
        waiting_times[job_index] = start_times[job_index]
        total_turnaround_time += turnaround_times[job_index]
        total_waiting_time += waiting_times[job_index]
    
    # Gather results from all MPI processes
    all_start_times = comm.gather(start_times, root=0)
    all_completion_times = comm.gather(completion_times, root=0)
    all_turnaround_times = comm.gather(turnaround_times, root=0)
    all_waiting_times = comm.gather(waiting_times, root=0)
    all_makespans = comm.gather(makespan, root=0)
    
    # Combine results at the root process
    if rank == 0:
        combined_start_times = {k: v for d in all_start_times for k, v in d.items()}
        combined_completion_times = {k: v for d in all_completion_times for k, v in d.items()}
        combined_turnaround_times = {k: v for d in all_turnaround_times for k, v in d.items()}
        combined_waiting_times = {k: v for d in all_waiting_times for k, v in d.items()}
        combined_makespan = max(all_makespans)

        # Calculate average turnaround time and average waiting time
        total_jobs = len(combined_start_times)
        avg_turnaround_time = sum(combined_turnaround_times.values()) / total_jobs
        avg_waiting_time = sum(combined_waiting_times.values()) / total_jobs
    
        return combined_start_times, combined_completion_times, combined_turnaround_times, combined_waiting_times, combined_makespan, avg_turnaround_time, avg_waiting_time
    else:
        return None, None, None, None, None, None, None

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Read the dataset from the provided text file
with open("GoCJ_Dataset_800.txt", "r") as file:
    dataset = [int(job) for job in file.read().split("\n")]

# Create list of jobs
jobs = [(i, size) for i, size in enumerate(dataset, start=1)]

# Run MCT scheduling algorithm in parallel
start_times, completion_times, turnaround_times, waiting_times, makespan, avg_turnaround_time, avg_waiting_time = mct_parallel(jobs, rank, size)
# Print the results at each process

# Print the results at the root process
if rank == 0:
    for job_index in sorted(start_times.keys(), key=lambda x: start_times[x]):
        print(f"Job {job_index}: Start Time: {start_times[job_index]}, Completion Time: {completion_times[job_index]}, Turnaround Time: {turnaround_times[job_index]}, Waiting Time: {waiting_times[job_index]}")

    print(f"Makespan: {makespan}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")