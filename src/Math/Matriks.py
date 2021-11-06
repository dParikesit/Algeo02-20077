#Kelas Matriks

class Matriks:
    #Atribut
    def __init__(self, size, fills = 0):
        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.mat = [[fills] * self.cols for i in range(self.rows)]
    
    def __str__(self): 
        rows = len(self.mat)
            
        mtxStr = ''
        mtxStr += '------------- output -------------\n'     
            
        for i in range(rows):
                
            mtxStr += ('|' + ', '.join( map(lambda x:'{0:8.3f}'.format(x), self.mat[i])) + '| \n')

        mtxStr += '----------------------------------'
        return mtxStr
    
    def transpose(self):
        mTrans = Matriks(size=(self.size))

        for i in range(self.rows):
            for j in range(self.cols):  
                mTrans.mat[j][i] = self.mat[i][j]

        return mTrans

    def determinan(self):
        #Mencari determinan dengan metode kofaktor
        det = 0

        #Jika ukurannya sudah 2x2
        if (self.size == (2,2)):
            #print(self)
            det = self.mat[0][0]*self.mat[1][1] - self.mat[0][1]*self.mat[1][0]
            #print("determinan ", det)

        else:
            #print(self)
            for i in range(self.cols):
                mSub = Matriks(size=(self.rows-1, self.cols-1))

                for j in range(1, self.rows):
                    col = 0
                    for k in range(self.cols):
                        if (i != k):
                            mSub.mat[j-1][col] = self.mat[j][k]
                            col = (col + 1) % self.cols
                
                det += self.mat[0][i] * mSub.determinan() * ((-1) ** (i))
        
        return det
    
    def add(m1, m2):
        m3 = Matriks(size=(m1.rows, m1.cols))

        for i in range(m3.rows):
            for j in range(m3.cols):
                m3.mat[i][j] = m1.mat[i][j] + m2.mat[i][j]

        return m3

    def mult(m1, m2):
        
        m3 = Matriks(size=(m1.rows, m2.cols))
        for i in range(m3.rows):
            for j in range(m3.cols):
                temp = 0
                for k in range(m1.cols):
                    temp += (m1.mat[i][k]) * (m2.mat[k][i])
                m3.mat[i][j] = temp

        return m3
    
