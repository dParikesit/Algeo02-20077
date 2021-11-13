from Matriks import Matriks
import numpy as np
import random

DECIMAL_PLACES = 5

class SVD(Matriks):
    def simultaneous_power_iteration(A, k, iterations = 1000):
        A = np.array(A)
        n, m = A.shape
        Q = np.random.rand(n, k)
        Q, _ = np.linalg.qr(Q)
        Q_prev = Q
        for i in range(iterations):
            if i%50 == 0: print("--------------",i)
            Z = A.dot(Q)
            Q, R = np.linalg.qr(Z)
            # can use other stopping criteria as well
            err = ((Q - Q_prev) ** 2).sum()
            Q_prev = Q
            if err < 1e-10:
                break
        
        #R = np.ndarray.tolist(np.diag(R))
        #R = [p for p in R if round(p, DECIMAL_PLACES) != 0]
        #Q = np.ndarray.tolist(Q)
        #R = np.diag(R)
        #R = np.append(A, np.zeros(size), axis=1)
        
        return np.diag(R), Q

    def find_SVD(m, compRate, stat=True, decimal_places = DECIMAL_PLACES, iterations = 1000):
        A = m.copy()
        ATrans = A.transpose()
        #print(A.shape)
        #print(ATrans)

        #Singular Kanan (Mencari V)
        ATransposeA = ATrans @ A
        eigenValues, V = SVD.simultaneous_power_iteration(ATransposeA, min(ATransposeA.shape), iterations=iterations)
        Vt = V.transpose()
        Vt = np.dot(Vt,-1)
        #print(Vt)

        #Zigma
        #print("Singular val : ",len(eigenValues))
        eigenValues = np.ndarray.tolist(eigenValues)
        #eigenValues = [p for p in eigenValues if round(p) != 0] #Nilai singular tidak nol
        Zigma = np.zeros(A.shape)
        #print(Zigma.shape)
        for i in range(min(min(Zigma.shape), len(eigenValues))):
            if (eigenValues[i] > 0):
                Zigma[i][i] = (np.sqrt(((eigenValues[i]))))
            else:
                temp = -1 # ----------> Inget Ganti
                Zigma[i][i] = (temp) * (np.sqrt(abs((eigenValues[i])))) 
            #print((eigenValues[i]))
        #print(Zigma)
        #print("Singular val : ",i)

        #Mencari U dari V
        #print(A.shape[0])
        U = np.zeros(shape=(A.shape[0],A.shape[0]))
        for i in range(A.shape[0]):
            U[i] = A @ Vt[i] / Zigma[i][i]
        Ut = U.T
        U = Ut
        #print(U)

        #Hasil perkalian
        ANew = U @ Zigma 
        ANew = ANew @ Vt
        ANew = ANew.round()
        #ANew = ANew.flip()

        AComp = SVD.compression(U, Zigma, Vt, compRate=compRate)
        AComp = AComp.round()

        if stat:
            print("Matrix U:\n", U)
            print("Matrix Vt:\n", Vt)
            print("Matrix Zigma:\n", Zigma)
            print("Matrix A:\n", A)
            print("Matrix A Baru:\n", ANew)
            print("Matrix A Baru:\n", AComp)
            print("Total Nodes      :", len(eigenValues))
            print(f"Compression Rate : {100*compRate}%")

        return AComp
            
    def compression(U, Zigma, Vt, compRate = 1):
        totalNodes = Zigma.shape[1]
        compCols = max(1, int(totalNodes * compRate))
        totalNodes = Zigma.shape[0]
        compRows = max(1, int(totalNodes * compRate))

        # Pemotongan U
        UNew = U[:,:compRows]
        
        # Pemotongan Zigma
        ZigmaNew = Zigma[:compRows,:compCols]

        # Pemotongan V
        VNew = Vt[:compCols,:]

        
        print("KOmpresi=========================")
        print(U.shape)
        print(UNew.shape)
        print(Zigma.shape)
        print(ZigmaNew.shape)
        print(Vt.shape)
        print(VNew.shape)
        

        ANew = UNew @ ZigmaNew
        ANew = ANew @ VNew

        return ANew

        