from Matriks import Matriks
from FungsiSVD import SVD
import random

import numpy as np
import cv2 as cv
import os

def accuracy(A, ANew):
    accuracy = np.sum(A) - np.sum(ANew)
    return (1 - accuracy/(A.shape[1] * A.shape[0])) * 100


#def split_matrix(matrix):

def compression(matrix, compRate=1, iterations=1000):
    A = matrix.copy()
    
    ANew = SVD.find_SVD(A,compRate=compRate, decimal_places=1, stat=False, iterations=iterations)
    
    return ANew

def compress_from_file(filePath, compRates):
    #Import Image
    img = cv.imread(filePath)
    fileFormat = filePath.split(".")[-1]
    #print(fileFormat)
    BGRArray = cv.split(img)
    #print(img.shape)
    

    #Compressing Image
    Iterations = [10]
    compRates = [compRates/100]
    QUALITY_JPG = 85
    QUALITY_PNG = 9
    for iterations in Iterations:
        i = 1
        for compRate in compRates:
            #print(f"Iterasi {iterations} compRate {compRate}")
            BGRNew = []
            for color in BGRArray:
                colorMatrix = np.array(color)
                colorMatrix = colorMatrix.astype(float)
                #print(colorMatrix)
                #minCol = min(colorMatrix.shape)
                #colorMatrix = colorMatrix[:minCol, :minCol]
                #color = color[:minCol, :minCol]
                colorMatrix = compression(colorMatrix, compRate=compRate,iterations=iterations)
                #print(colorMatrix)
                BGRNew.append(colorMatrix)
                #print(f"accuraccy : {accuracy(color,colorMatrix)} %")

            #Export File
            img_bgr = cv.merge(BGRNew)
            #print(type(BGRNew))
            path = "C:/Users/rioau/Documents/ITB/2Tingkat 2/Tugas/Algeo/Tubes/2/Algeo02-20077/test"
            
            if (fileFormat == "png"):
                quality = QUALITY_PNG
            else:
                quality = QUALITY_JPG
            
            cv.imwrite(
                os.path.join(path, f'Testing 3 Compressed {int(compRate*100)}%.{fileFormat}'),
                img_bgr,
                #[int(cv.IMWRITE_JPEG_QUALITY),QUALITY],
                [int(cv.IMWRITE_PNG_COMPRESSION) ,quality])
            i += 1



#testing_svd()
compress_from_file("C:/Users/rioau/Documents/ITB/2Tingkat 2/Tugas/Algeo/Tubes/2/Algeo02-20077/test/Testing 1.jpg", 25)

