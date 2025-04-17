# backend/quantum_simulation.py

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.providers.backend import BackendV2
from qiskit_aer.noise import NoiseModel, pauli_error

def create_basic_circuit(apply_error=False):
    """
    Creates a simple 3-qubit circuit with a 3-qubit bit-flip error correction code.
    If apply_error is True, applies a bit-flip error on qubit 0.
    """
    # Create a 3-qubit circuit
    qc = QuantumCircuit(3, 3)

    # Initialize state: for demonstration, we start with |+++>
    qc.h(0)
    qc.h(1)
    qc.h(2)

    # Encode information (for bit-flip code, this is a simple repetition)
    # In a real error-correction scheme, you would add encoding/decoding steps

    # Introduce error if flag is set
    if apply_error:
        qc.x(0)  # Flip qubit 0

    # Syndrome measurement: measure all qubits
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

def simulate_circuit(apply_error=False, use_noise_model=False):
    """
    Simulates the quantum circuit. If use_noise_model is True, applies a depolarizing noise model.
    """
    qc = create_basic_circuit(apply_error=apply_error)

    simulator = AerSimulator()
    backend = simulator
    shots = 1024

    if use_noise_model:
        # Define a simple noise model (depolarizing error on single qubit operations)
        error = pauli_error([('X', 0.1), ('I', 0.9)])
        noise_model = NoiseModel()
        noise_model.add_all_qubit_quantum_error(error, ['h', 'x'])
        job = backend.run(transpile(qc, backend), shots=shots)
    else:
        error = pauli_error([('X', 0.1), ('I', 0.9)])
        noise_model = NoiseModel()
        noise_model.add_all_qubit_quantum_error(error, ['h', 'x'])
        job = backend.run(transpile(qc, backend), shots=shots, noise_model=noise_model)

    result = job.result()
    counts = result.get_counts(qc)
    return counts
