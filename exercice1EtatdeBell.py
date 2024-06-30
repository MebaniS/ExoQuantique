from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(qr, cr)

state= input("Etat de Bell ? Φ+(1), Φ-(2), Ψ+(3), Ψ-(4)")
#Pour ∣Φ+⟩
if state=="1":
# Appliquez la porte Hadamard au premier qubit
    qc.h([0])

# Appliquez la porte CNOT
    qc.cx([0],[1])

    qc.measure(qr, cr)

#Pour ∣Φ-⟩
elif state=="2" :
    qc.h(0)
    qc.cx(0, 1)
    qc.z([0])
    qc.measure(qr,cr)

#Pour ∣Ψ+⟩
elif state=="3":
    qc.h(0)
    qc.cx(0, 1)
    qc.x([0])
    qc.measure(qr,cr)

#Pour ∣Ψ-⟩
elif state=="4":
    qc.h(0)
    qc.cx(0, 1)
    qc.z([0])
    qc.x([0])
    qc.measure(qr,cr)


# Exécutez le circuit sur le simulateur BasicAer
simulator=AerSimulator()
compiled_circuit = transpile(qc,simulator)
qobj=assemble(compiled_circuit)
result=simulator.run(qobj).result()
# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure:",counts)