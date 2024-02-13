from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Create a data array to be scattered
data = []
for i in range(size):
    data.append(i*2)

# Scatter the data to all the processes
local_data = MPI.COMM_WORLD.scatter(data, root=0) # scatters the data array data to all processes in the MPI communicator.
# Each process receives a portion of the data.

# Perform some computation on the local data
if rank == 0:
    print(f"Local Data {local_data} given to Process {rank}")
    local_data += 8
    print(f"Local Data updated to {local_data} of Process {rank}")

if rank == 1:
    print(f"Local Data {local_data} given to Process {rank}")
    local_data += 3
    print(f"Local Data updated to {local_data} of Process {rank}")

if rank == 2:
    print(f"Local Data {local_data} given to Process {rank}")
    local_data += 1
    print(f"Local Data updated to {local_data} of Process {rank}")

if rank == 3:
    print(f"Local Data {local_data} given to Process {rank}")
    local_data += 5
    print(f"Local Data updated to {local_data} of Process {rank}")


# result =local_data
# print(result)

# Gather the results from all the processes
results = MPI.COMM_WORLD.gather(local_data, root=0)

# Print the results on the root process
if rank == 0:
    print(f"Local Data before Scattered {data}")
    print(f"Results: after gathering {results}")