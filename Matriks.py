#Kelas Matriks

class Matriks:
    #Atribut
    def __init__(self, size=(1,1), fills = 0):
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
    
    def copy(self):
        mTemp = Matriks(size=self.size)
        
        for i in range(self.rows):
            for j in range(self.cols):
                mTemp.mat[i][j] = self.mat[i][j]

        return mTemp

    def transpose(self):
        mTrans = Matriks(size=(self.cols, self.rows))

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
    
    def isAllColsZero(m, col):
        ans = True
        for i in range(m.rows):
            if m.mat[i][col] != 0:
                ans = False
                break
        
        return ans

    def reduksi(m):
        mTemp = m.copy()

        for i in range(mTemp.cols):
            #Jika jumlah kolom melebihi baris
            if (i > mTemp.rows-1):
                break
            #Jika ada kolom yang full kosong
            if (Matriks.isAllColsZero(mTemp,i)):
                continue
            
            #Jika ada nilai mat(i,i) yang nol
            k = 0
            while (mTemp.mat[i][i] == 0 and (k < mTemp.rows)):
                if (i!=k):
                    for j in range(mTemp.cols):
                        mTemp.mat[i][j], mTemp.mat[k][j] = mTemp.mat[k][j], mTemp.mat[i][j]
                k+=1
            
            #Mulai Mereduksi
            for j in range(i+1, mTemp.rows):
                ratio = mTemp.mat[j][i]/mTemp.mat[i][i]
                for k in range(mTemp.cols):
                    mTemp.mat[j][k] -= ratio * mTemp.mat[i][k]
                print("----test----\n",mTemp)

        return mTemp


