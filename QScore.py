from transformers import pipeline
import numpy as np
from qiskit import QuantumCircuit, transpile
import json, math, qiskit_aer
from sentence_transformers import SentenceTransformer



# Combines the two semantic vector embeddings into a complex number
# example -> vector1 [0.1, 0.2, 0.2] <> vector2 [0.3, -0.2, 0.3] -> complexVector [0.1 + i0.3, 0.2 - i0.2, 0.2 + i0.3] 
def complexCombine(vector1 ,vector2):
    if len(vector1) == len(vector2):
        complexVector = []
        for i in range(0,len(vector1)-1):
            complexVector.append(complex(vector1[i], vector2[i]))
        return complexVector
    else:
        raise ValueError("Unequal vector sizes")


# Runs our quantum circuit giving a distribution of "likeness" scores
def run(complexMixedVector, shots=4096):
    qubitCount = len(complexMixedVector)
    qc = QuantumCircuit(qubitCount, qubitCount)
    complexVectorNormalized = []
    for i in range(0, qubitCount-1):
        
        complexVectorNormalized.append(complexMixedVector[i] / np.linalg.norm(complexMixedVector[i]))


        # Automatically does the transformations (rx, ry, rz) required to point in the imaginary numbers direction
        qc.initialize([complexVectorNormalized[i].real , complexVectorNormalized[i].imag], i)



    # Hamards forces the two vectors to interact
    # Extra rotation that forces the imaginary (vector b) and real (vector a) to ineract with eachother
    # This allows the similarity comparison since 
    qc.h(range(0,qubitCount-1))
    qc.measure(range(0,qubitCount-1), range(0,qubitCount-1))


    backend = qiskit_aer.AerSimulator()
    job = backend.run(qc, shots=shots)

    counts = job.result().get_counts()
 
    return job.result()


# Tally's the instances & their score then return an average of all the individual shot's scores
def compare(qResult, shots = 4096):
    counts = qResult.get_counts()
    likenessList = []
    i = 1

    # Loop through the keys in the first dictionary
    for key, count in counts.items():
        # Get the likeness of the shot starting at 1 for 100% alike, all the way to 1 / int(111111) (which is lowwwww)
        likeness = 1 / (int(key, 2)+1)

        # Creates the total amount of 
        likenessList.append((count * likeness))


    total = likenessList[0]
    for i in range(1,len(likenessList)-1):
        total = (total+likenessList[i])
    return total / shots


# initialize the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


# Calculates the similarity score
def calcScore(request, docVector, shots = 4096, qubits = 20, autoScore=True, autoScoreReach=3):
    requestVector = model.encode(request)
    
    # If for some reason a string was brought into the docVector we'll just transform it
    if type(docVector) == type(request):
        docVector = model.encode(docVector)

    
    complexVector = complexCombine(requestVector, docVector)

    total = []
    lenOfVec = len(complexVector)


    # Since we don't have 300+ qubits to work with we've split the total embedding space into chunks
    for i in range(0,lenOfVec,qubits):
        total.append(compare(run(complexVector[i:i+(qubits)],shots),shots))

    total.sort(reverse=True)
    if autoScore:
        return sum(total[0:autoScoreReach-1]) / autoScoreReach
    else:
        return total

