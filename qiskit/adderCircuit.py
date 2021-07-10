from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

# First Circuit
n = 8
n_q = n
n_b = n

qc_output = QuantumCircuit(n_q, n_b)

for j in range(n):
    qc_output.measure(j, j)

qc_output.draw()

