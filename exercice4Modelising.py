from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble
steps=3
theta=0.2
# Créez les registres quantique et classique
n= int(input("nombre de qubits?"))
qr = QuantumRegister(n, 'q')
cr = ClassicalRegister(n, 'c')
qc = QuantumCircuit(qr, cr)
#Appliquer Hadamart sur tout les qubits
for i in range(n):
    qc.h([i])

#Boucle avec les pas
for step in range(steps):
# Appliquer CNOT entre chaque paire de qubits
    for i in range(n - 1):
        qc.cx([i], [i + 1])

# Appliquer une rotation RZ à chaque qubit
    for i in range(n):
        qc.rz(theta, [i])

# Ajouter les mesures
    qc.measure(qr,cr) 

 #Exécutez le circuit sur le simulateur BasicAer
simulator=AerSimulator()
compiled_circuit = transpile(qc,simulator)
qobj=assemble(compiled_circuit)
result=simulator.run(qobj).result()
# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure:",counts)