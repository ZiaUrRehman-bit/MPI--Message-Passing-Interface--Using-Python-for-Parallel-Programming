from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Create a data array to be scattered
data = []
for i in range(size):
    data.append(i*2)
# Scatter the data to all the processes
local_data = MPI.COMM_WORLD.scatter(data, root=0)

if rank == 1:
    print(local_data)
    local_data += 3
# Perform some computation on the local data
result =sum([local_data])
print(result)
# Gather the results from all the processes
results = MPI.COMM_WORLD.gather(result, root=0)

# Print the results on the root process
if rank == 0:
    print(data)
    print(f"Results: {results}")