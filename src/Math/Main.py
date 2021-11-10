from Matriks import Matriks
from FungsiSVD import SVD
from Polynom import Polynom

def testing_matriks():
    #Test Instance
    #instatiate + call method fill
    m1 = Matriks(size=(3,3))
    m1.fill(2)
    print(m1)

    #Test Transpose
    m2 = m1.transpose()
    print(m2)

    #Test Determinan
    m3 = Matriks(size=(2,2))
    m3.fill([
                [[-11,1],-1],
                [-1,[-11,1]]
            ])
    print(m3)
    det_m3 = m3.determinan()
    print("Determinan :",det_m3)
    
    #Test Mult
    m4 = Matriks(size=(4,2))
    m4.fill(2)
    m5 = Matriks(size=(2,4))
    m5.fill([[7,2,1,3],[2,1,5,1]])
    print("Matriks 5\n",m5)
    m6 = Matriks.mult(m5, m4)
    print("Matriks 4\n",m4)
    print("Perkalian Matriks\n",m6)

    #Test add
    m4 = Matriks(size=(3,3))
    m4.fill(2)
    m5 = Matriks(size=(3,3))
    m5.fill([[7,2,3],[2,1,5],[3,7,2]])
    m6 = Matriks.sub(m5, m4)
    print("Matriks 5\n",m5)
    print("Matriks 4\n",m4)
    print("Pengurangan Matriks\n",m6)

    #Test reduksi
    m5 = Matriks(size=(5,6))
    m5.fill([
                [2,1,5,1,5,1],
                [1,1,3,1,6,-1],
                [-1,1,-1,0,4,-3],
                [-3,2,-4,-4,-7,0],
                [3,-1,5,2,2,3]
            ])
    #m5.mat = [[1,2,3,9],[2,-1,1,8], [3,0,-1,3]]
    m6 = Matriks.reduksi(m5)
    print("Matriks 5\n",m5)
    print("Reduksi Matriks 5\n",m6) 

    #Test Identitas
    m1 = Matriks.identity()
    print(m1)
    m1 = Matriks.identity_eigen()
    print(m1)
   
def testing_polynom():
    X = Polynom(len=3)
    X.Pol = [1,3,4]
    Y = Polynom(len=2)
    Y.Pol = [2,3]
    print("X: ", X)
    print("Y: ", Y)
    print("X + Y: ",X+Y)
    print("X - Y: ",X-Y)
    print("X - 3: ",X-3)
    print("X * Y: ",X * Y)
    print("X * 3: ",X * 3)

def testing_svd():

    #Test find svd
    A = Matriks(size=(3,4))
    A.fill([[1,2,-2,0], [3,2,-1,1],[2,1,-3,1]])
    SVD.find_SVD(A)

    return


    #Singular Kiri
    AATranspose = Matriks.mult(A, A.transpose())
    IdentitasEigen = Matriks.identity_eigen()
    m = Matriks.sub(AATranspose, IdentitasEigen)
    print("Singular Kiri", m)

    #Singular Kanan
    ATransposeA = Matriks.mult(A.transpose(), A)
    IdentitasEigen = Matriks.identity_eigen(size=(4,4))
    m = Matriks.sub(ATransposeA, IdentitasEigen)
    print("Singular Kanan", m)

    #Test Null Space
    m = Matriks(size=(5,6))
    m.fill([
            [2,1,5,1,5,1],
            [1,1,3,1,6,-1],
            [-1,1,-1,0,4,-3],
            [-3,2,-4,-4,-7,0],
            [3,-1,5,2,2,3]
            ])
    mRed = Matriks.reduksi(m)
    nullSpace = SVD.null_space(mRed)
    normNullSpace = SVD.norm_null_space(mRed)
    print("Matriks 5\n",m)
    print("Reduksi Matriks 5\n",mRed) 
    print("Null Space:", nullSpace)
    print("Norm null Space:", normNullSpace)


"""
    CARA MENGGUNAKAN SYSTEM MATRIKS DAN POLYNOM
    1. Polynom
        - Polynom dibuat dengan instatiate polynom
        contohPol = Polynom()
        contohPol.Len = 3 ----> Isi panjang
        contohPol.Pol = [3, 5, 2] ------> (3 + 5X + 2X^2)

        - Gunakan Polynom seperti biasa (+, -, * saja)
        contohPol = contohPol1 + contohPol2
        contohPol = contohPol1 - contohPol2
        contohPol = contohPol1 * contohPol2
        print(contohPol)

    2. Instatiate Matrix:
        - Isi seragam
        m1 = Matriks(size=(3,3))
        m1.fill(2) -> Isi Seragam
        print(m1)

        - Isi dengan polynom (Tambahkan List dalam list)
        m3 = Matriks(size=(2,2))
        m3.fill([
                [[-11,1],-1], -------> | (-11 + K)    (-1)   | 
                [-1,[-11,1]]           |    (-1)   (-11 + K) |
                ])
        print(m3)

    Udah instatiate matrix A dan matrix diagonal I:
    m = Matrix.mult(A, A.transpose()) - Matriks.
"""

def main():
    testing_svd()


main()
