def mct_sequential(jobs):
    # Sort jobs based on their processing time (job size)
    sorted_jobs = sorted(jobs, key=lambda x: x[1]) # jobs will be sorted based on their sizes.
    
    # Initialize metrics
    start_times = {}
    completion_times = {}
    turnaround_times = {}
    waiting_times = {}
    makespan = 0
    
    # Assign each job to the processor with the earliest completion time
    current_time = 0
    for job_index, job_size in sorted_jobs:
        # Calculate start time
        start_times[job_index] = current_time
        
        # Update completion time and makespan
        completion_times[job_index] = current_time + job_size
        current_time += job_size
        makespan = max(makespan, completion_times[job_index])
    
    # Calculate turnaround time and waiting time
    total_turnaround_time = 0
    total_waiting_time = 0
    for job_index, _ in sorted_jobs:
        turnaround_times[job_index] = completion_times[job_index] - start_times[job_index]
        waiting_times[job_index] = start_times[job_index]
        total_turnaround_time += turnaround_times[job_index]
        total_waiting_time += waiting_times[job_index]
    
    # Calculate average waiting time and average turnaround time
    num_jobs = len(jobs)
    avg_waiting_time = total_waiting_time / num_jobs
    avg_turnaround_time = total_turnaround_time / num_jobs
    
    return start_times, completion_times, turnaround_times, waiting_times, makespan, avg_waiting_time, avg_turnaround_time

# Read the dataset from the provided text file
with open("GoCJ_Dataset_800.txt", "r") as file:
    dataset = [int(job) for job in file.read().split("\n")]

# Create list of jobs
jobs = [(i, size) for i, size in enumerate(dataset, start=1)]

# Run MCT scheduling algorithm
start_times, completion_times, turnaround_times, waiting_times, makespan, avg_waiting_time, avg_turnaround_time = mct_sequential(jobs)

for job_index, _ in sorted(start_times.items(), key=lambda x: x[1]):
    print(f"Job {job_index}: Start Time: {start_times[job_index]}, Completion Time: {completion_times[job_index]}, Turnaround Time: {turnaround_times[job_index]}, Waiting Time: {waiting_times[job_index]}")

print(f"Makespan: {makespan}")
print(f"Average Waiting Time: {avg_waiting_time}")
print(f"Average Turnaround Time: {avg_turnaround_time}")

