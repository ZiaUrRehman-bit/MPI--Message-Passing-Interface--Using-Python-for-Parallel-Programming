from mpi4py import MPI

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Split the communicator into even-sized groups
color = rank % 2 # Each process calculates its color based on its rank. 
# In this case, it takes the remainder of the rank divided by 2, resulting in either 0 or 1.

comm = MPI.COMM_WORLD.Split(color, rank) # This line splits the MPI.COMM_WORLD communicator into even-sized groups based on the color calculated
# in the previous step. Processes with the same color are grouped together. Each process receives a new communicator named comm.

# Print the rank and size of the new communicator
print(f"Process {rank}: color = {color}, rank = {comm.rank}, size = {comm.size}") # This line prints information about each process, including
# its original rank, color, and rank within the new communicator (comm). It helps to verify the splitting of the communicator.

#  This can be useful in a variety of situations where we want to group processes 
#  together for more efficient communication or to perform collective operations.

#  One common use case for MPI.COMM_WORLD.Split() is in load balancing applications,
#  where we want to divide the workload among multiple groups of processes. 
#  By splitting the communicator based on some criteria, such as the current load 
#  on each process, we can create groups of processes that have similar workloads and 
#  can therefore perform work more efficiently. This can lead to faster execution 
#  times and better performance overall.

