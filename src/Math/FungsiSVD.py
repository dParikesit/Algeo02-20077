from Matriks import Matriks

class SVD(Matriks):

    def find_SVD(m):
        A = m.copy()
        ATranspose = A.transpose()

        print(A)
        print(ATranspose)
    
    def get_leading_index(row):
        #Mencari Posisi Leading 1
        r = list(row)
        if 1 in r:
            return r.index(1)

    def null_space(matrix):
        # Mereduksi Matrix
        A = matrix.copy()
        A = A.reduksi()

        row, col = A.size
        # Mencari posisi-posisi leading 1
        non_basis = [SVD.get_leading_index(r) for r in A.mat]
        non_basis = [p for p in non_basis if p != None] #menghilangkan anggota None

        # Mencari posisi-posisi non-leading 1
        basis = list(set(range(col)).difference(non_basis))

        """
            - Yang tidak menjadi leading value, akan menjadi basis nullspace

        """

        def z(i,j):
            # Jika xi adalah basis dan sedang mencari null-spacenya
            if i in basis and i == basis[j]:
                return 1
            
            # Jika xi adalah basis dan tidak sedang mencari null-spacenya
            elif i in basis and i != basis[j]:
                return 0
            
            # Jika xi bukanlah basis
            elif i in non_basis:
                k = non_basis.index(i)
                return -A.mat[k][basis[j]]
        
        # Menginisiasi basis (jumlah kolom x jumlah basis)
        basis = [list([z(i,j) for i in range(col)]) for j in range(len(basis))]

        return basis