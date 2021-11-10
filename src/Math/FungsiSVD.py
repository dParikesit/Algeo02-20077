from Matriks import Matriks
import math

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
        A = Matriks(size=(2,3))
        #A.fill([[2,2,0], [-1,1,0]])
        A.fill([[3,1,1], [-1,3,1]])
        ATrans = A.transpose()
        #print(A)
        #print(ATrans)

        #Singular Kiri (Mencari U)
        eigenValues = [12,10]
        AATranspose = Matriks.mult(A, ATrans)
        U = SVD.find_vectors(eigenValues, matrix = AATranspose)
        print("Matrix U:\n", U)

        #Singular Kanan (Mencari V)
        eigenValues = [12,10,0]
        ATransposeA = Matriks.mult(ATrans, A)
        V = SVD.find_vectors(eigenValues, matrix = ATransposeA)
        VTranspose = V.transpose()
        print("Matrix Vt:\n", VTranspose)

        #Zigma
        eigenValues = [p for p in eigenValues if p != 0] #Nilai singular tidak nol
        Zigma = Matriks(size=(A.size))
        for i in range(len(eigenValues)):
            Zigma.mat[i][i] = (eigenValues[i]) ** 0.5
        print("Matrix Zigma:\n", Zigma)

        #Hasil perkalian
        ANew = SVD.newMatrix(U, Zigma, VTranspose)
        print("Matrix A:\n", A)
        print("Matrix A Baru:\n", ANew)

        #Compression
        ANew = SVD.compression(U, Zigma, VTranspose, 0.5)
        print("Matrix A:\n", A)
        print("Matrix A Baru:\n", ANew)


        """
            Dari file testing masih ada nilai - yang kebalik (mungkin mirip sama problem amar di grup wa)
        """

        #Singular Kanan (Mencari V)
        

    def find_vectors(eigenValues, matrix):
        #matrix variable contains either A.Atranpose or Atranspose.A
        
        #Iniasisi besar ruang vektor
        lenList = len(eigenValues)
        vectors = Matriks(size=matrix.size)
        allBasis = []

        #Mengiterasi setiap nilai eigen
        for i in range(lenList):
            #Memanggil fungsi null space
            IdentitasEigen = Matriks.identity_eigen(fills=eigenValues[i])
            m = Matriks.sub(matrix, IdentitasEigen)
            #print(m)
            basis = SVD.norm_null_space(m)

            #Karena return basis berbentuk list dalam list, harus diaapend manual
            for temp in basis:
                allBasis.append(temp)
            
            #Debugging
            #print(f"Eigen Value : {eigenValues[i]}, basis :\n",basis)
        
        vectors.mat = allBasis

        #Hasil vector ditranspose agar menjadi ruang vektor
        vectors = vectors.transpose()
        return vectors

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

        return basis
    
    def norm_null_space(matrix):
        #Mencari basis/null space
        basis = SVD.null_space(matrix)

        for i in range(len(basis)):
            normRat = sum(map(lambda x:x*x, basis[i])) ** 0.5
            basis[i] = [j/normRat for j in basis[i]]
        
        return basis

    def newMatrix(U, Zigma, Vt):
        #Hasil U.Zigma.Vt
        ANew = Matriks.mult(U, Zigma)
        ANew = Matriks.mult(ANew, Vt)

        return ANew

    def compression(U, Zigma, Vt, compRate = 1):
        totalNodes = Zigma.cols
        compCols = int(totalNodes * compRate)
        totalNodes = Zigma.rows
        compRows = int(totalNodes * compRate)

        # Pemotongan U
        UNew = Matriks(size=(U.rows, compRows))
        for j in range(compRows):
            for i in range(UNew.rows):
                UNew.mat[i][j] = U.mat[i][j]

        # Pemotongan V
        VNew = Matriks(size=(compCols, Vt.cols))
        for i in range(compCols):
            VNew.mat[i] = Vt.mat[i]
        
        # Pemotongan Zigma
        # Pemotongan V
        ZigmaNew = Matriks(size=(compRows, compCols))
        for j in range(compCols):
            for i in range(compRows):
                ZigmaNew.mat[i][j] = Zigma.mat[i][j]

        ANew = SVD.newMatrix(UNew, ZigmaNew, VNew)

        return ANew

        