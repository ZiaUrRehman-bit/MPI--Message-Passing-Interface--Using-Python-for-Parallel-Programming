from mpi4py import MPI
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load the dataset
data = pd.read_csv("array.csv")
X = data.iloc[:, 0:9]
y = data.iloc[:, -1]

# Split the dataset into chunks
chunk_size = len(X) // size
X_chunk = X[rank * chunk_size: (rank + 1) * chunk_size]
y_chunk = y[rank * chunk_size: (rank + 1) * chunk_size]

# Train a random forest classifier on the chunk
model = RandomForestClassifier(n_estimators=10)
model.fit(X_chunk, y_chunk)

# Evaluate the model on the test set
test_X = X
test_y = y
accuracy = model.score(test_X, test_y)

# Gather the accuracy scores from all processes
accuracies = comm.gather(accuracy, root=0)

# Print the final accuracy if this is the root process
if rank == 0:
    print(f"Final accuracy: {np.mean(accuracies)}")