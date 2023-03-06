from mpi4py import MPI

def broadcast(comm, data, root):
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == root:
        # Send the data to all other processes
        for i in range(size):
            if i != root:
                comm.send(data, dest=i)
    else:
        # Receive the data from the root process
        data = comm.recv(source=root)
        print(f"{data} recieved by Process {rank}")

# Broadcast a message from the root process
data = "Hello, World!"
root = 0
comm = MPI.COMM_WORLD
broadcast(comm, data, root)