from Matriks import Matriks

class SVD(Matriks):

    def find_SVD(m):
        A = m.copy()
        ATranspose = A.transpose()

        print(A)
        print(ATranspose)