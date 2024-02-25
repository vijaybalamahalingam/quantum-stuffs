from qiskit import *
from qiskit_aer import AerSimulator
# Create a Quantum Circuit with one qubit
qr = QuantumCircuit(1, 1)  # Initialize with one qubit and one classical bit for measurement result

# Apply the Hadamard gate (H) to the qubit, putting it in a superposition state
qr.h(0)

# Measure the qubit in the standard basis
qr.measure(0, 0)

backend = AerSimulator()
job = backend.run(qr, shots=1024) # Increase shots for better statistics

# Get the results
result = job.result()
counts = result.get_counts(qr)

# Print the measurement outcomes
print("Counts:")
print(counts)

# Determine the most frequent outcome (0 or 1) as the random bit
random_bit = max(counts, key=counts.get)
print("Random bit:", random_bit)
