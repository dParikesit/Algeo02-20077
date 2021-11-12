import cv2 as cv
import sys
import numpy as np


def simultaneous_power_iteration(A, k):
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

  A = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  rows, cols = A.shape
  mode = False
  if rows < cols:
    mode = True  # True jika return U, False return V

  eigen, arr = simultaneous_power_iteration(A, min(A.shape))
  print("Eigen")
  print(eigen)

  if mode==True:
    print("U")
  else:
    print("V")
  print(arr)


if __name__=="__main__":
  compress("C:/Users/rioau/Documents/ITB/2Tingkat 2/Tugas/Algeo/Tubes/2/Algeo02-20077/src/files/test.jpg")
