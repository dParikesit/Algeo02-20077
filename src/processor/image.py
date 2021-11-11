import cv2 as cv
import sys

def compress(filePath):
  #Import Image
  img = cv.imread(filePath)
  BGRArray = cv.split(img)
  print(img.shape)

  #Compressing Image
  for color in BGRArray:
    color = (list(color))
    


  #Export File
  img_bgr = cv.merge(BGRArray)
  cv.imwrite('Test2.jpg',img_bgr)


if __name__=="__main__":
  compress("C:/Users/rioau/Documents/ITB/2Tingkat 2/Tugas/Algeo/Tubes/2/Algeo02-20077/src/files/test.jpg")
