from Polynom import Polynom

class Matriks(Polynom):
    #Atribut
    def __init__(self, size=(1,1), fills = Polynom()):
        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.mat = [[fills] * self.cols for i in range(self.rows)]
    
    def __str__(self): 
        rows = len(self.mat)
            
        mtxStr = ''
        mtxStr += '------------- output -------------\n'     
            
        for i in range(rows):
            mtxStr += ('|')
            if isinstance(self.mat[i][0], (int,float)):
                mtxStr += (', '.join( map(lambda x:'{0:12.3f}'.format(x), self.mat[i])))
            else:
                for j in range(self.cols):
                    if isinstance(self.mat[i][j], Polynom):
                        pol = self.mat[i][j]
                        mtxStr += ' '*5 + Polynom.__str__(pol) + ' '*5
                    
                    

            mtxStr += ('| \n')

        mtxStr += '----------------------------------'
        return mtxStr
    
    def fill(self, fills):
        
        for i in range(self.rows):
            for j in range(self.cols):
                if isinstance(fills, list):
                    if (isinstance(fills[i][j], list)):
                        fillPol = Polynom(len=len(fills[i][j]))
                        fillPol.Pol = fills[i][j]
                        self.mat[i][j] = fillPol
                    else:
                        fillPol = Polynom(len=1)
                        fillPol.Pol[0] = fills[i][j]
                        self.mat[i][j] = fillPol
                else:
                    fillPol = Polynom(len=1)
                    fillPol.Pol[0] = fills
                    self.mat[i][j] = fillPol

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
        det = Polynom()
        temp = Polynom()


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
                
                temp = self.mat[0][i] * mSub.determinan()
                temp *= ((-1) ** (i))
                det = det + temp
                
        
        return det
    
    def add(m1, m2):
        m3 = Matriks(size=(m1.rows, m1.cols))
        temp = Polynom()
        for i in range(m3.rows):
            for j in range(m3.cols):
                temp = m1.mat[i][j] + m2.mat[i][j]
                m3.mat[i][j] = temp

        return m3

    def mult(m1, m2):
        
        m3 = Matriks(size=(m1.rows, m2.cols))
        for i in range(m3.rows):
            for j in range(m3.cols):
                fillPol = Polynom()
                for k in range(m1.cols):
                    fillPol += (m1.mat[i][k]) * (m2.mat[k][i])
                m3.mat[i][j] = fillPol

        return m3
    
    def isAllColsZero(m, col):
        ans = True
        zeroPol = Polynom()

        for i in range(m.rows):
            zeroPol.Len = m.mat[i][col].Len
            zeroPol.fill()
            if m.mat[i][col] != zeroPol:
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
                        #swaping rows
                        mTemp.mat[i][j], mTemp.mat[k][j] = mTemp.mat[k][j], mTemp.mat[i][j]
                k+=1
            
            #Mulai Mereduksi
            for j in range(i+1, mTemp.rows):
                ratio = mTemp.mat[j][i].Pol[0]/mTemp.mat[i][i].Pol[0]
                for k in range(mTemp.cols):
                    mTemp.mat[j][k] -= mTemp.mat[i][k] * ratio

        return mTemp


