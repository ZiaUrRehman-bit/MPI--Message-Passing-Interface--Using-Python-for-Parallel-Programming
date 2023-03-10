from mpi4py import MPI

# Get the rank of the process
rank = MPI.COMM_WORLD.rank

# Send a message to the other process
if rank == 0:
    message = "Hello from process 0"
    MPI.COMM_WORLD.send(message, dest=1)

    message = MPI.COMM_WORLD.recv(source=1)
    print(f"Process 0 Received message: {message}")

elif rank == 1:
    # Receive the message from the other process
    message = MPI.COMM_WORLD.recv(source=0)
    print(f"Process 1 Received message: {message}")

    # Send a reply to the other process
    reply = "Hello from process 1"
    MPI.COMM_WORLD.send(reply, dest=0)