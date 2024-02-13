def min_min_sequential(jobs):
    # Initialize metrics
    start_times = {}
    completion_times = {}
    makespan = 0

    # Assign each job to the processor with the earliest minimum completion time
    for _ in range(len(jobs)):
        min_job_index, min_job_size = min(jobs, key=lambda x: x[1])

        # Calculate start time
        start_times[min_job_index] = makespan

        # Update completion time and makespan
        completion_times[min_job_index] = makespan + min_job_size
        makespan = max(makespan, completion_times[min_job_index])

        # Remove the assigned job from the list
        jobs.remove((min_job_index, min_job_size))

    # Calculate turnaround time and waiting time
    total_turnaround_time = sum(completion_times.values()) - sum(start_times.values())
    total_waiting_time = sum(start_times.values())
    
    # Calculate average turnaround time and average waiting time
    num_jobs = len(start_times)
    avg_turnaround_time = total_turnaround_time / num_jobs
    avg_waiting_time = total_waiting_time / num_jobs

    return start_times, completion_times, makespan, avg_turnaround_time, avg_waiting_time

# Read the dataset from the provided text file
with open("GoCJ_Dataset_800.txt", "r") as file:
    dataset = [int(job) for job in file.read().split("\n")]

# Create list of jobs
jobs = [(i, size) for i, size in enumerate(dataset, start=1)]

# Run Min-Min scheduling algorithm in sequential
start_times, completion_times, makespan, avg_turnaround_time, avg_waiting_time = min_min_sequential(jobs)

# Print the results
for job_index in sorted(start_times.keys()):
    print(f"Job {job_index}: Start Time: {start_times[job_index]}, Completion Time: {completion_times[job_index]}")

print(f"Makespan: {makespan}")
print(f"Average Waiting Time: {avg_waiting_time}")
print(f"Average Turnaround Time: {avg_turnaround_time}")
