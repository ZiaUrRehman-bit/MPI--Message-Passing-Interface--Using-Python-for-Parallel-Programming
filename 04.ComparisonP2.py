from mpi4py import MPI
import os

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# Print the rank and size of the communicator
print(f"I am process {rank} of {size}")

if rank == 0:
    result = 0
    startTime = os.times()
    for i in range(1000000):
        result = i*i
    endTime = os.times()
    print(f"User CPU Start Time: {startTime.user}")
    # print(f"System CPU Start Time: {startTime.system}")

    print(f"User CPU End Time: {endTime.user}")
    # print(f"System CPU End Time: {endTime.system}")

    totalUserTime = endTime.user - startTime.user
    totalSystemTime = endTime.system - startTime.system

    print(f"User CPU Time: {totalUserTime}")
    print(f"System CPU Time: {totalSystemTime}")


if rank == 1:
    
    result1 = 0
    startTime = os.times()
    for j in range(1000000):
        result1 = j*j

    endTime = os.times()
    print(f"User CPU Start Time: {startTime.user}")
    # print(f"System CPU Start Time: {startTime.system}")

    print(f"User CPU End Time: {endTime.user}")
    # print(f"System CPU End Time: {endTime.system}")

    totalUserTime = endTime.user - startTime.user
    totalSystemTime = endTime.system - startTime.system

    print(f"User Time: {totalUserTime}")
    print(f"System Time: {totalSystemTime}")
