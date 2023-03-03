
# Import MPI from mpi4py library
from mpi4py import MPI

# --> MPI.COMM_WORLD is a predefined communicator in MPI

# --> It is a communicator object that provides a way for processes 
#     to communicate and coordinate with each other in a parallel program

# --> MPI.COMM_WORLD allows processes to send and receive messages to and 
#     from any other process in the program and many other functions

# --> Rank:  Process ID or Unique number from 0 to the total number of processes
#     in the communicator minus 1
# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank

# returns how many processes initiated, total number of processes
size = MPI.COMM_WORLD.size

# If we are the root process, send a message to the other process
if rank == 0:
    message = "Hello from process 0"
    MPI.COMM_WORLD.send(message, dest=1)
    print("Massage Created ")
# If we are the other process, receive the message from the root process
if rank == 1:
    message = MPI.COMM_WORLD.recv(source=0)
    print(f"Received message: {message}")