from qiskit import QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble
import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Créez les registres quantiques
qr = QuantumRegister(1, 'q')
qc = QuantumCircuit(qr)

def prepare_arbitrary_state(a, b):
    # Normaliser les coefficients
    norm = np.sqrt(np.abs(a)**2 + np.abs(b)**2)
    a = a / norm
    b = b / norm

    # Calcul des angles de rotation
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b) - np.angle(a)

    # Application des rotations nécessaires
    qc.ry(theta, 0)
    qc.rz(phi, 0)

    return qc

def portefunc(nom_porte, circuit):
    # Appliquer la porte spécifiée
    if nom_porte == 'H':
        circuit.h(0)
    elif nom_porte == 'X':
        circuit.x(0)
    elif nom_porte == 'Y':
        circuit.y(0)
    elif nom_porte == 'Z':
        circuit.z(0)
    # Simulation de l'état quantique
    simulator = AerSimulator()
    compiled_circuit = transpile(circuit, simulator)
    qobj = assemble(compiled_circuit)
    result = simulator.run(qobj).result()

    # Obtenir l'état après l'opération
    statevector = Statevector.from_instruction(circuit)

    # Visualiser sur la sphère de Bloch
    plot_bloch_multivector(statevector)
    plt.title(f"Après Porte {nom_porte}")
    plt.show()

# Préparer l'état arbitraire
a = 1 / np.sqrt(2)  # Exemple : 1/√2
b = 1 / np.sqrt(2)  # Exemple : 1/√2
prepare_arbitrary_state(a, b)

# Demander à l'utilisateur de choisir une porte
gate = input("Entrez la porte à appliquer (H, X, Y, Z) : ").strip().upper()

# Appliquer la porte choisie et visualiser l'état du qubit
portefunc(gate, qc)
