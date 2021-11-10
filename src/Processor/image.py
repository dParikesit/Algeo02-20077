import cv2 as cv
import numpy as np
import os

def compress(filePath):
  img = cv.imread(filePath)
  print(img.shape)
  b,g,r = cv.split(img)
  
  #  Process here

  cv.imwrite(os.path.join("files",filePath), cv.merge((b,g,r)))

if __name__=="__main__":
  print("Halo")
  compress('nama.png')