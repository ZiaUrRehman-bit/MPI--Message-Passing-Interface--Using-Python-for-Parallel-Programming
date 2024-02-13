from mpi4py import MPI

def min_min_parallel(jobs, rank, size):
    # Calculate the number of jobs to be processed by each MPI process
    chunk_size = len(jobs) // size
    start_index = rank * chunk_size
    end_index = start_index + chunk_size if rank < size - 1 else len(jobs)

    # Initialize metrics
    start_times = {}
    completion_times = {}
    makespan = 0

    # Assign each job to the processor with the earliest minimum completion time
    for _ in range(len(jobs)):
        # Check if there are jobs remaining
        if jobs[start_index:end_index]:
            min_job_index, min_job_size = min(jobs[start_index:end_index], key=lambda x: x[1])
            min_job_global_index = min_job_index + start_index

            # Calculate start time
            start_times[min_job_global_index] = makespan

            # Update completion time and makespan
            completion_times[min_job_global_index] = makespan + min_job_size
            makespan = max(makespan, completion_times[min_job_global_index])

            # Remove the assigned job from the list
            jobs.remove((min_job_index, min_job_size))

    # Calculate turnaround time and waiting time
    total_turnaround_time = sum(completion_times.values()) - sum(start_times.values())
    total_waiting_time = sum(start_times.values())
    
    # Gather results from all MPI processes
    all_start_times = comm.gather(start_times, root=0)
    all_completion_times = comm.gather(completion_times, root=0)
    all_makespans = comm.gather(makespan, root=0)
    total_turnaround_times = comm.reduce(total_turnaround_time, op=MPI.SUM, root=0)
    total_waiting_times = comm.reduce(total_waiting_time, op=MPI.SUM, root=0)

    # Combine results at the root process
    if rank == 0:
        combined_start_times = {k: v for d in all_start_times for k, v in d.items()}
        combined_completion_times = {k: v for d in all_completion_times for k, v in d.items()}
        combined_makespan = max(all_makespans)

        # Calculate average turnaround time and average waiting time
        total_jobs = len(combined_start_times)
        avg_turnaround_time = total_turnaround_times / total_jobs
        avg_waiting_time = total_waiting_times / total_jobs
    
        return combined_start_times, combined_completion_times, combined_makespan, avg_turnaround_time, avg_waiting_time
    else:
        return None, None, None, None, None

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Read the dataset from the provided text file
with open("GoCJ_Dataset_800.txt", "r") as file:
    dataset = [int(job) for job in file.read().split("\n")]

# Create list of jobs
jobs = [(i, size) for i, size in enumerate(dataset, start=1)]

# Run Min-Min scheduling algorithm in parallel
start_times, completion_times, makespan, avg_turnaround_time, avg_waiting_time = min_min_parallel(jobs, rank, size)

# Print the results at each process

# Print the results at the root process
if rank == 0:
    for job_index in sorted(start_times.keys(), key=lambda x: start_times[x]):
        print(f"Job {job_index}: Start Time: {start_times[job_index]}, Completion Time: {completion_times[job_index]}")

    print(f"Makespan: {makespan}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
