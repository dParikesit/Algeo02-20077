import numpy as np
import cv2 as cv

def compress(filePath):
  img = cv.imread(filePath)
  b,g,r = cv.split(img)
  print(img.shape)
  print(b)
  # print(g)
  # print(r)

if __name__=="__main__":
  compress("Halo")