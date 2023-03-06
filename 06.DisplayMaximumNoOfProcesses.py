from mpi4py import MPI

# Get the size of the communicator
size = MPI.COMM_WORLD.size
rank = MPI.COMM_WORLD.rank

if rank == 0:
    # Print the size of the communicator
    print(f"The maximum number of processes that can run is {size}")