from mpi4py import MPI
import os

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Print the rank and size of the communicator
print(f"I am process {rank} of {size}")

startTime = os.times()

if rank == 0:
    result = 0
    for i in range(1000000):
        result = i*i

if rank == 1:
    result1 = 0
    for j in range(1000000):
        result1 = j*j

endTime = os.times()
       
totalUserTime = endTime.user - startTime.user
totalSystemTime = endTime.system - startTime.system

print(f"User Time: {totalUserTime}")
print(f"System Time: {totalSystemTime}")
