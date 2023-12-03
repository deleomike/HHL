# import math lib
from math import pi
from matplotlib import pyplot as plt

# import Qiskit
from qiskit import Aer, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library import CU1Gate, CU3Gate

# import basic plot tools
from qiskit.tools.visualization import plot_histogram


class HHLCircuit:

    def __init__(self, num_bits: int = 4):

        # TODO: Check if hermitian matrix, otherwise C=

        # create Quantum Register called "qr" with 4 qubits
        qr = QuantumRegister(num_bits, name="qr")
        # create Quantum Register called "cr" with 4 qubits
        cr = ClassicalRegister(num_bits, name="cr")
        # Creating Quantum Circuit called "qc" involving your Quantum Register "qr"
        # and your Classical Register "cr"
        qc = QuantumCircuit(qr, cr, name="solve_linear_sys")

        # To use local qasm simulator
        backend = Aer.get_backend('qasm_simulator')

        # Initialize other params
        r = 4
        t_0 = 2 * pi

        # Initialize times that we get the result vector
        n0 = 0
        n1 = 0

        for i in range(10):
            # TODO How is this setting the state??
            # Set the input|b> state"
            qc.x(qr[2])

            qc.barrier(label="Phase Est.")

            # Set the phase estimation circuit
            qc.h(qr[0])
            qc.h(qr[1])
            qc.p(pi, qr[0])
            qc.p(pi / 2, qr[1])
            qc.cx(qr[1], qr[2])

            # The quantum inverse  Fourier transform
            qc.h(qr[0])
            qc.append(CU1Gate(-pi / 2), [qr[0], qr[1]])
            qc.h(qr[1])

            qc.barrier(label="Rotation")

            # R（lamda^-1） Rotation
            qc.x(qr[1])
            qc.cu
            qc.append(CU3Gate(pi / (2**r), 0, 0), [qr[0], qr[3]])
            qc.append(CU3Gate(2 * pi / (2**r), 0, 0), [qr[1], qr[3]])

            qc.barrier(label="Uncomputation")

            # Uncomputation
            qc.x(qr[1])
            qc.h(qr[1])
            qc.append(CU1Gate(pi / 2), [qr[0], qr[1]])
            qc.h(qr[0])

            qc.cx(qr[1], qr[2])
            qc.p(-pi / 2, qr[1])
            qc.p(-pi, qr[0])

            qc.h(qr[1])
            qc.h(qr[0])

            # To measure the whole quantum register
            qc.measure(qr[0], cr[0])
            qc.measure(qr[1], cr[1])
            qc.measure(qr[2], cr[2])
            qc.measure(qr[3], cr[3])

            job = execute(qc, backend=backend, shots=8192, )
            result = job.result()

            # Get the sum og all results
            n0 = n0 + result.get_counts("solve_linear_sys")['1000']
            n1 = n1 + result.get_counts("solve_linear_sys")['1100']

            # print the result
            print(result)
            #     print(result.get_data(qc))
            plot_histogram(result.get_counts())

            #     Reset the circuit
            qc.reset(qr)

            # calculate the scale of the elements in result vectot and print it.
            p = n0 / n1
            print(n0)
            print(n1)
            print(p)

            # qc.draw("mpl")
            # plt.show()

if __name__ == "__main__":

    circ = HHLCircuit()