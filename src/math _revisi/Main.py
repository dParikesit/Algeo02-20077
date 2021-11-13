from Matriks import Matriks
from FungsiSVD import SVD
import random

import numpy as np
import cv2 as cv
import os

def testing_svd():

    cols = 553
    rows = 560
    #A = np.ndarray([[random.randint(0,255) for _ in range(cols)] for _ in range(rows)])
    
    A = np.array(np.random.randint(low = 1, high=255, size = (rows, cols)))
    A = np.array([[3,1,1],[-1, 3, 1]], dtype=object)
    ACopy = A.copy()
    
    """
    ANew = np.zeros(A.shape)
    i = 0
    while (i <= A.shape[0]):
        i += 100
        iTemp = i - 100
        j = 0
        while (j <= A.shape[1]):
            j += 100
            jTemp = j - 100
            ANew[iTemp:i, jTemp:j] = SVD.find_SVD(A[iTemp:i, jTemp:j],compRate=1, decimal_places=1, stat=False, iterations=100)
    """

    print(ACopy)

    ANew = SVD.find_SVD(A,compRate=1, decimal_places=1, stat=True, iterations=100)
    
    print(ANew)
    print(f"Size : {cols} accuraccy : {accuracy(ACopy,ANew)}")

    return

    A = Matriks()
    cols = 10
    rows = cols
    A.fill([[random.randint(0,255) for _ in range(cols)] for _ in range(rows)])
    #print(A)
    
    ANew = SVD.find_SVD3(A,compRate=0.5, decimal_places=1, stat=True)
    print(f"Size : {cols} accuraccy : {accuracy(A,ANew)}")

    return

    #Test find svd
    # Isi Ukuran random di sini
    for i in range(1,100):
        A = Matriks()
        cols = i
        rows = i
        A.fill([[random.randint(0,255) for _ in range(cols)] for _ in range(rows)])
        #print(A)
        
        ANew = SVD.find_SVD(A,compRate=1, decimal_places=1, stat=False)
        print(f"Size : {i} accuraccy : {accuracy(A,ANew)}")

def accuracy(A, ANew):
    accuracy = np.sum(A) - np.sum(ANew)
    return (1 - accuracy/(A.shape[1] * A.shape[0])) * 100


#def split_matrix(matrix):

def compression(matrix, compRate=1, iterations=1000):
    A = matrix.copy()
    
    
    """
    #Splitting Image into Chunkz
    ANew = np.zeros(A.shape)
    i = 0
    while (i <= A.shape[0]):
        i += 100
        iTemp = i - 100
        j = 0
        while (j <= A.shape[1]):
            j += 100
            jTemp = j - 100
            ANew[iTemp:i, jTemp:j] = SVD.find_SVD(A[iTemp:i, jTemp:j],compRate=compRate, decimal_places=1, stat=False, iterations=iterations)
    """
    ANew = SVD.find_SVD(A,compRate=compRate, decimal_places=1, stat=False, iterations=iterations)
    
    return ANew

def compress_from_file(filePath):
    #Import Image
    img = cv.imread(filePath)
    BGRArray = cv.split(img)
    print(img.shape)
    

    #Compressing Image
    Iterations = [10]
    compRates = [0.001, 0.004, 0.032, 0.064, 1]
    QUALITY_JPG = [85]
    QUALITY_PNG = [90, 100, 120]
    for iterations in Iterations:
        i = 1
        for compRate in compRates:
            print(f"Iterasi {iterations} compRate {compRate}")
            BGRNew = []
            for color in BGRArray:
                colorMatrix = np.array(color)
                colorMatrix = colorMatrix.astype(float)
                print(colorMatrix)
                #minCol = min(colorMatrix.shape)
                #colorMatrix = colorMatrix[:minCol, :minCol]
                #color = color[:minCol, :minCol]
                colorMatrix = compression(colorMatrix, compRate=compRate,iterations=iterations)
                print(colorMatrix)
                BGRNew.append(colorMatrix)
                print(f"accuraccy : {accuracy(color,colorMatrix)} %")

            #Export File
            img_bgr = cv.merge(BGRNew)
            print(type(BGRNew))
            path = "C:/Users/rioau/Documents/ITB/2Tingkat 2/Tugas/Algeo/Tubes/2/Algeo02-20077/test"
            
            for quality in QUALITY_PNG:
                cv.imwrite(
                    os.path.join(path, f'Testing 3 {iterations} {i} Iterasi, CompRate {compRate} quality {quality}.png'),
                    img_bgr,
                    #[int(cv.IMWRITE_JPEG_QUALITY),QUALITY],
                    [int(cv.IMWRITE_PNG_COMPRESSION) ,quality])
            i += 1



#testing_svd()
compress_from_file("C:/Users/rioau/Documents/ITB/2Tingkat 2/Tugas/Algeo/Tubes/2/Algeo02-20077/test/Testing 3.jpg")

