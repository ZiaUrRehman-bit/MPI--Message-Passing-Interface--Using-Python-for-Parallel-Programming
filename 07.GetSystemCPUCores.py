import psutil

# Get the number of CPU cores on the system
num_cores = psutil.cpu_count()

# Calculate the maximum number of processes that can run
max_processes = num_cores

print(f"The maximum number of processes that can run is {max_processes}")