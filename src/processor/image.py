import numpy as np
import cv2 as cv
import os
import time

# =================================================================
DECIMAL_PLACES = 5

def simultaneous_power_iteration(A, k, iterations=1000):
    A = np.array(A)
    n, m = A.shape
    Q = np.random.rand(n, k)
    Q, _ = np.linalg.qr(Q)
    Q_prev = Q
    for i in range(iterations):
        Z = A.dot(Q)
        Q, R = np.linalg.qr(Z)

        # Stop criteria
        err = ((Q - Q_prev) ** 2).sum()
        Q_prev = Q
        if err < 1e-10:
            break

    return np.diag(R), Q


def find_SVD(m, compRate, stat=True, decimal_places=DECIMAL_PLACES, iterations=1000):
    flip = False
    if(m.shape[0]>m.shape[1]):
        m = m.T
        flip = True
    A = m.copy()
    ATrans = A.transpose()
    ATransposeA = ATrans @ A
    eigenValues, V = simultaneous_power_iteration(
        ATransposeA, min(ATransposeA.shape), iterations=iterations)
    Vt = V.transpose()
    Vt = np.dot(Vt, -1)
    eigenValues = np.ndarray.tolist(eigenValues)
    Zigma = np.zeros(A.shape)
    for i in range(min(min(Zigma.shape), len(eigenValues))):
        if (eigenValues[i] > 0):
            Zigma[i][i] = (np.sqrt(((eigenValues[i]))))
        else:
            temp = -1
            Zigma[i][i] = (temp) * (np.sqrt(abs((eigenValues[i]))))
    U = np.zeros(shape=(A.shape[0], A.shape[0]))
    for i in range(A.shape[0]):
        U[i] = A @ Vt[i] / Zigma[i][i]
    Ut = U.T
    U = Ut
    ANew = U @ Zigma
    ANew = ANew @ Vt
    ANew = ANew.round()
    AComp,k  = createResult(U, Zigma, Vt, compRate=compRate)
    AComp = AComp.round()

    # Difference Percentage
    diff = k*(A.shape[0] + A.shape[1] + 1)/(A.shape[0] + A.shape[1])

    if stat:
        print("Matrix U:\n", U)
        print("Matrix Vt:\n", Vt)
        print("Matrix Zigma:\n", Zigma)
        print("Matrix A:\n", A)
        print("Matrix A Baru:\n", ANew)
        print("Matrix A Baru:\n", AComp)
        print("Total Nodes      :", len(eigenValues))
        print(f"Compression Rate : {100*compRate}%")

    if(flip==True):
        AComp = AComp.T

    return AComp, diff


def createResult(U, Zigma, Vt, compRate=1):
    totalNodes = Zigma.shape[1]
    compCols = max(1, int(totalNodes * compRate))
    totalNodes = Zigma.shape[0]
    compRows = max(1, int(totalNodes * compRate))

    # Pemotongan U
    UNew = U[:, :compRows]
    # Pemotongan Zigma
    ZigmaNew = Zigma[:compRows, :compCols]
    # Pemotongan V
    VNew = Vt[:compCols, :]

    ANew = UNew @ ZigmaNew
    ANew = ANew @ VNew

    k = np.count_nonzero(ZigmaNew)
    return ANew,k

# =================================================================
def accuracy(A, ANew):
    accuracy = np.sum(A) - np.sum(ANew)
    return (1 - accuracy/(A.shape[1] * A.shape[0])) * 100

def compression(matrix, compRate=1, iterations=1000):
    A = matrix.copy()
    
    ANew, diff = find_SVD(A,compRate=compRate, decimal_places=1, stat=False, iterations=iterations)
    
    return ANew, diff

def compress_from_file(filePath, compRates):
    start = time.perf_counter_ns()

    #Import Image
    img = cv.imread(filePath)
    fileFormat = filePath.split(".")[-1]
    BGRArray = cv.split(img)
    diff = 0

    #Compressing Image
    Iterations = [10]
    compRates = [compRates/100]
    QUALITY_JPG = 85
    QUALITY_PNG = 9
    for iterations in Iterations:
        i = 1
        for compRate in compRates:
            BGRNew = []
            for color in BGRArray:
                colorMatrix = np.array(color)
                colorMatrix = colorMatrix.astype(float)
                colorMatrix, diff = compression(colorMatrix, compRate=compRate,iterations=iterations)
                BGRNew.append(colorMatrix)

            #Export File
            img_bgr = cv.merge(BGRNew)

            if (fileFormat == "png"):
                quality = QUALITY_PNG
                cv.imwrite(
                    os.path.join(filePath),
                    img_bgr,
                    [int(cv.IMWRITE_PNG_COMPRESSION), quality])
            elif(fileFormat=='jpeg' or fileFormat=='jpg'):
                quality = QUALITY_JPG
                cv.imwrite(
                    os.path.join(filePath),
                    img_bgr,
                    [int(cv.IMWRITE_JPEG_QUALITY), quality])
            else:
                cv.imwrite(
                    os.path.join(filePath),
                    img_bgr)
            i += 1
    
    stop = time.perf_counter_ns()
    return stop-start, diff

