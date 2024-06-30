from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(qr, cr)

# Appliquez la porte Hadamard au premier qubit
qc.h([0])
# Appliquez la porte CNOT
qc.cx([0],[1])
state= input("Bits ? 00,01,10,11")
#Pour 00

#Pour 01
if state=="01" :
    qc.z([0])

#Pour 10
elif state=="10":
    qc.x([0])

#Pour 11
elif state=="11":
    qc.z([0])
    qc.x([0])
    


qc.cx(qr[0], qr[1])
qc.h([0])
qc.measure(qr,cr)

# Exécutez le circuit sur le simulateur BasicAer
simulator=AerSimulator()
compiled_circuit = transpile(qc,simulator)
qobj=assemble(compiled_circuit)
result=simulator.run(qobj).result()
# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure:",counts)
