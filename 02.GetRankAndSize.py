
from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Print the rank and size of the communicator
print(f"I am process {rank} of {size}")