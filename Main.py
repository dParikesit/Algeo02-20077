from typing import Sized
from Matriks import Matriks

def main():
    #Test Instance
    m1 = Matriks(size=(3,3), fills=1)
    print(m1)

    #Test Transpose
    m2 = m1.transpose()
    print(m2)

    #Test Determinan
    m3 = Matriks(size=(4,4))
    m3.mat = [[4,2,1,3],[3,1,5,1],[5,3,1,2],[5,1,4,8]]
    print(m3)
    det_m3 = m3.determinan()
    print("Determinan :",det_m3)

    #Test Mult
    m4 = Matriks(size=(4,2), fills=2)
    m5 = Matriks(size=(2,4))
    m5.mat = [[7,2,1,3],[2,1,5,1]]
    m6 = Matriks.mult(m5, m4)
    print("Matriks 5\n",m5)
    print("Matriks 4\n",m4)
    print("Perkalian Matriks\n",m6)

    #Test add
    m4 = Matriks(size=(3,3), fills=2)
    m5 = Matriks(size=(3,3))
    m5.mat = [[7,2,3],[2,1,5],[3,7,2]]
    m6 = Matriks.add(m5, m4)
    print("Matriks 5\n",m5)
    print("Matriks 4\n",m4)
    print("Penjumlahan Matriks\n",m6)

main()

