from mpi4py import MPI
import numpy as np

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Create a random matrix and vector
matrix = np.ones((10, 10), dtype="uint8")*2
vector = np.ones(10, dtype="uint8")

# Divide the matrix into rows and distribute them among the processes
local_rows = np.array_split(matrix, size)[rank]
# if rank == 1:
#     print(local_rows)

# Compute the local dot product
local_result = np.dot(local_rows, vector)
print(local_result)
# Gather the local results into a single array on the root process
result = MPI.COMM_WORLD.gather(local_result, root=0)

# Print the result on the root process
if rank == 0:
    print(matrix)
    print(vector)
    print(f"Result: {result}")