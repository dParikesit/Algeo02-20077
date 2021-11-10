import cv2 as cv
<<<<<<< HEAD:src/Processor/image.py
import sys
=======
import numpy as np
import os
>>>>>>> dafd397ba029fb4682cc628a6260718f21705668:src/processor/image.py

def compress(filePath):
  #Import Image
  img = cv.imread(filePath)
<<<<<<< HEAD:src/Processor/image.py
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
=======
  print(img.shape)
  b,g,r = cv.split(img)
  
  #  Process here

  cv.imwrite(os.path.join("files",filePath), cv.merge((b,g,r)))

if __name__=="__main__":
  print("Halo")
  compress('nama.png')
>>>>>>> dafd397ba029fb4682cc628a6260718f21705668:src/processor/image.py
