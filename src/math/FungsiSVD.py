from Matriks import Matriks
import math
import numpy as np

DECIMAL_PLACES = 5

class SVD(Matriks):

    def find_SVD(m, compRate, stat=True, decimal_places = DECIMAL_PLACES):
        """
            Mencari Bentuk Matriks SVD
            A = (U . Zigma . Vt)
            U       : null-space dari singular kiri
            Zigma   : nilai eigen singular kanan
            Vt      : null-space dari singular kanan

            Notes : mungkin dua alur kerja dibawah bisa dibikin fungsi baru (pipeline baru)
        """
        A = m.copy()
        ATrans = A.transpose()
        #print(A)
        #print(ATrans)

        #Singular Kanan (Mencari V)
        ATransposeA = Matriks.mult(ATrans, A)
        U = Matriks()
        eigenValues, U.mat = SVD.simultaneous_power_iteration(ATransposeA.mat, min(ATransposeA.size))
        U.fill(U.mat)

        #Singular Kiri (Mencari U)
        AATranspose = Matriks.mult(A, ATrans)
        V = Matriks()
        eigenValues, V = SVD.simultaneous_power_iteration(AATranspose.mat, min(AATranspose.size))
        V.fill(V.mat)

        #Zigma
        eigenValues = [p for p in eigenValues if p != 0] #Nilai singular tidak nol
        Zigma = Matriks(size=(A.size))
        for i in range(len(eigenValues)):
            Zigma.mat[i][i] = round((eigenValues[i]) ** 0.5, DECIMAL_PLACES)

        #Hasil perkalian
        #ANew = SVD.newMatrix(U, Zigma, V)

        if stat:
            print("Matrix U:\n", U)
            print("Matrix Vt:\n", V)
            print("Matrix Zigma:\n", Zigma)
            print("Matrix A:\n", A)

        return 

        #Singular Kiri (Mencari U)
        AATranspose = Matriks.mult(A, ATrans)
        eigenValues = SVD.eigen_values(AATranspose)
        U = SVD.find_vectors(eigenValues=eigenValues, matrix = AATranspose)

        #Singular Kanan (Mencari V)
        ATransposeA = Matriks.mult(ATrans, A)
        eigenValues = SVD.eigen_values(ATransposeA)
        V = SVD.find_vectors(eigenValues=eigenValues, matrix = ATransposeA)
        VTranspose = V.transpose()

        #Zigma
        eigenValues = [p for p in eigenValues if p != 0] #Nilai singular tidak nol
        Zigma = Matriks(size=(A.size))
        for i in range(len(eigenValues)):
            Zigma.mat[i][i] = (eigenValues[i]) ** 0.5

        #Hasil perkalian
        ANew = SVD.newMatrix(U, Zigma, VTranspose)

        #Compression
        ANew = SVD.compression(U, Zigma, VTranspose, compRate=compRate)
        ANew.round(decimal_places=decimal_places)

        if stat:
            print("Matrix U:\n", U)
            print("Matrix Vt:\n", VTranspose)
            print("Matrix Zigma:\n", Zigma)
            print("Matrix A:\n", A)
            print("Matrix A Baru:\n", ANew)
            print("Total Nodes      :", len(eigenValues))
            print(f"Compression Rate : {100*compRate}%")



        """
            Dari file testing masih ada nilai - yang kebalik (mungkin mirip sama problem amar di grup wa)
        """

        return ANew
        
    def eigen_values(matrix):
        #Mencari Eigen Value
        eigenMatrix = Matriks.sub(Matriks.identity_eigen(size=(matrix.rows, matrix.cols)), matrix)
        determinant = eigenMatrix.determinan()
        #determinant.Pol = [round(x) for x in determinant.Pol]
        eigenValues = np.roots(determinant.Pol[::-1])
        #eigenValues = [round(x,DECIMAL_PLACES) for x in eigenValues]

        return eigenValues

    def find_vectors(eigenValues, matrix):
        #matrix variable contains either A.Atranpose or Atranspose.A

        #Iniasisi besar ruang vektor
        lenList = len(eigenValues)
        vectors = Matriks(size=matrix.size)
        allBasis = []

        #Mengiterasi setiap nilai eigen
        for i in range(lenList):
            print("Progress ", i)
            #Memanggil fungsi null space
            IdentitasEigen = Matriks.identity_eigen(size = matrix.size, fills=eigenValues[i])
            #print(IdentitasEigen)
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
        #print(vectors)
        vectors = vectors.transpose()
        #vectors.round()

        return vectors

    def null_space(matrix):
        # Mereduksi Matrix
        A = matrix.copy()
        A = A.reduksi()
        print(A)

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
        if basis == [] :
            basis = [[0 for _ in range(A.cols)]]
        return basis
    
    def null_space_2(matrix):
        A = matrix.copy()
        A = A.reduksi()
        #print(A)

        #X ke-n selalu menjadi basis
        basis = [[0 for _ in range(A.cols)]]
        basis[-1][-1] = 1

        valLead = A.cols-2
        
        while (valLead >= 0):
            #Jika menjadi basis
            if matrix.mat[valLead][valLead] == 0:
                basis.append([0 for _ in range(A.cols)])

                #Nilai koef yang menjadi basis selalu 1
                basis[-1][valLead] = 1
                valLead -= 1
                continue
        
            #Jika tidak menjadi basis      
            numBasis = len(basis)
            for k in range(numBasis):
                #print(basis)
                temp = 0
                for l in range(valLead+1, A.cols):
                    temp += (A.mat[valLead][l]) * (basis[k][l]) * (-1)
                    #print(valLead, valLead, k, l)
                basis[k][valLead] = temp
            
            valLead-=1
        
        basis.reverse()

        return basis


    def norm_null_space(matrix):
        #Mencari basis/null space
        basis = SVD.null_space_2(matrix)

        for i in range(len(basis)):
            normRat = sum(map(lambda x:x*x, basis[i])) ** 0.5
            if normRat != 0:
                basis[i] = [j/normRat for j in basis[i]]
        
        return basis

    def newMatrix(U, Zigma, Vt):
        #Hasil U.Zigma.Vt
        ANew = Matriks.mult(U, Zigma)
        ANew = Matriks.mult(ANew, Vt)

        return ANew

    def compression(U, Zigma, Vt, compRate = 1):
        totalNodes = Zigma.cols
        compCols = max(1, int(totalNodes * compRate))
        totalNodes = Zigma.rows
        compRows = max(1, int(totalNodes * compRate))

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

    def simultaneous_power_iteration(A, k):
        A = np.array(A)
        n, m = A.shape
        Q = np.random.rand(n, k)
        Q, _ = np.linalg.qr(Q)
        Q_prev = Q
        for i in range(1000):
            Z = A.dot(Q)
            Q, R = np.linalg.qr(Z)
            # can use other stopping criteria as well
            err = ((Q - Q_prev) ** 2).sum()
            Q_prev = Q
            if err < 1e-3:
                break

        
        return np.diag(R), Q

    def compress(filePath):
        # #Import Image
        # img = cv.imread(filePath)
        # BGRArray = cv.split(img)
        # print(img.shape)

        # #Compressing Image
        # for color in BGRArray:
        #   color = (list(color))
            


        # #Export File
        # img_bgr = cv.merge(BGRArray)
        # cv.imwrite('Test2.jpg',img_bgr)

        A = Matriks(size=(2,3))
        A.mat = np.array([[3,1,1],[-1,3,1]])
        At = A.transpose()
        ATA = Matriks.mult(At, A)
        
        rows, cols = ATA.size
        mode = False
        if rows < cols:
            mode = True  # True jika return U, False return V

        eigen, arr = SVD.simultaneous_power_iteration(ATA.mat, min(ATA.size))
        print("Eigen")
        print(eigen)

        if mode==True:
            print("U")
        else:
            print("V")
        print(arr)

        
    