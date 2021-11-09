from Matriks import Matriks
import math
import numpy as np

class SVD(Matriks):

    def find_SVD(m):
        """
            Mencari Bentuk Matriks SVD
            A = (U . Zigma . Vt)
            U       : null-space dari singular kiri
            Zigma   : nilai eigen singular kanan
            Vt      : null-space dari singular kanan

            Notes : mungkin dua alur kerja dibawah bisa dibikin fungsi baru (pipeline baru)
        """
        #-------- Hanya untuk testing ---------
        A = m
        ATrans = A.transpose()

        ATA = Matriks.mult(ATrans, A)
        eigenMatrix = Matriks.sub(Matriks.identity_eigen(size=(ATA.rows, ATA.cols)), ATA)
        determinant = eigenMatrix.determinan()
        eigenValues = np.roots(determinant.Pol)

        print(eigenValues)

        #Singular Kiri (Mencari U)
        AATranspose = Matriks.mult(A, ATrans)
        U = []
        for eigen in eigenValues:
            IdentitasEigen = Matriks.identity_eigen(fills=eigen)
            m = Matriks.sub(AATranspose, IdentitasEigen)
            basis = SVD.null_space(m)
            U.append(basis)
            print(f"Eigen Value : {eigen}, basis :\n",basis)

        """
            Dari file testing masih ada nilai - yang kebalik (mungkin mirip sama problem amar di grup wa)
        """

        #Singular Kanan (Mencari V)
        eigenValues = [12,10, 0]
        ATransposeA = Matriks.mult(ATrans, A)
        V = []
        for eigen in eigenValues:
            IdentitasEigen = Matriks.identity_eigen(fills=eigen)
            m = Matriks.sub(ATransposeA, IdentitasEigen)
            basis = SVD.null_space(m)
            V.append(basis)
            print(f"Eigen Value : {eigen}, basis :\n",basis)



    def null_space(matrix):
        # Mereduksi Matrix
        A = matrix.copy()
        A = A.reduksi()

        row, col = A.size

        def get_leading_index(row):
            #Mencari Posisi Leading 1
            r = list(row)
            if 1 in r:
                return r.index(1)

        # Mencari posisi-posisi leading 1
        non_basis = [get_leading_index(r) for r in A.mat]
        non_basis = [p for p in non_basis if p != None] #menghilangkan anggota None

        # Mencari posisi-posisi non-leading 1
        basis = list(set(range(col)).difference(non_basis))

        """
            - Yang tidak menjadi leading value, akan menjadi basis nullspace

        """

        def z(i,j):
            # Jika xi adalah basis dan sedang mencari null-spacenya
            if i in basis and i == basis[j]:
                return 1
            
            # Jika xi adalah basis dan tidak sedang mencari null-spacenya
            elif i in basis and i != basis[j]:
                return 0
            
            # Jika xi bukanlah basis
            elif i in non_basis:
                k = non_basis.index(i)
                return -A.mat[k][basis[j]]
        
        # Menginisiasi basis (jumlah kolom x jumlah basis)
        basis = [list([z(i,j) for i in range(col)]) for j in range(len(basis))]

        mBasis = Matriks(size=(len(basis), col))
        mBasis.mat = basis

        return mBasis
    
    def norm_null_space(matrix):
        #Mencari basis/null space
        basis = SVD.null_space(matrix)

        for i in range(basis.rows):
            normRat = math.sqrt(sum(map(lambda x:x*x, basis.mat[i])))
            basis.mat[i] = [j/normRat for j in basis.mat[i]]
        
        return basis

    