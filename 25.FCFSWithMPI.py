from mpi4py import MPI

def fcfs_parallel(jobs, rank, size):
    # Calculate the number of jobs to be processed by each MPI process
    chunk_size = len(jobs) // size
    start_index = rank * chunk_size
    end_index = start_index + chunk_size if rank < size - 1 else len(jobs)

    # Initialize metrics
    start_times = {}
    completion_times = {}
    turnaround_times = {}
    waiting_times = {}
    makespan = 0

    # Assign each job to the processor sequentially
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

# Run FCFS scheduling algorithm in parallel
start_times, completion_times, turnaround_times, waiting_times, makespan, avg_turnaround_time, avg_waiting_time = fcfs_parallel(jobs, rank, size)

# Print the results at the root process
if rank == 0:
    for job_index in sorted(start_times.keys(), key=lambda x: start_times[x]):
        print(f"Job {job_index}: Start Time: {start_times[job_index]}, Completion Time: {completion_times[job_index]}, Turnaround Time: {turnaround_times[job_index]}, Waiting Time: {waiting_times[job_index]}")

    print(f"Makespan: {makespan}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
