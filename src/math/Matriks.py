from textwrap import fill
from numpy.lib.arraysetops import isin
from Polynom import Polynom

DECIMAL_PLACES = 5

class Matriks(Polynom):
    #Atribut
    def __init__(self, size=(1,1)):
        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.mat = [[0] * self.cols for i in range(self.rows)]
    
    def __str__(self): 
        rows = self.rows
        cols = self.cols
            
        mtxStr = ''
        mtxStr += '------------- output -------------\n'     
            
        for i in range(rows):
            mtxStr += ('|')
            if isinstance(self.mat[i][0], (int,float)):
                mtxStr += (', '.join( map(lambda x:'{0:12.3f}'.format(x), self.mat[i])))
            else:
                for j in range(cols):
                    if isinstance(self.mat[i][j], Polynom):
                        pol = self.mat[i][j]
                        mtxStr += ' '*5 + Polynom.__str__(pol) + ' '*5
                    
                    

            mtxStr += ('| \n')

        mtxStr += '----------------------------------'
        return mtxStr
    
    def fill(self, fills = 0):
        
        if isinstance(fills, list):
            self.rows = len(fills)
            self.cols = len(fills[0])
            self.size = (self.rows, self.cols)
        
        self.mat = [[0] * self.cols for i in range(self.rows)]

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

    def identity(size=(3,3)):
        m = Matriks(size=size)
        m.fill(0)
        for i in range(m.rows):
            fillPol = Polynom(len=1)
            fillPol.Pol[0] = 1
            m.mat[i][i] = fillPol
        
        return m
    
    def identity_eigen(size=(3,3), fills=Polynom()):
        m = Matriks(size=size)
        m.fill(0)

        if isinstance(fills, Polynom):
            # Jika belum memiliki nilai eigen
            for i in range(m.rows):
                fillPol = Polynom(len=2)
                fillPol.Pol[1] = 1
                m.mat[i][i] = fillPol
        else:
            # Jika sudah memiliki nilai eigen
            for i in range(m.rows):
                fillPol = Polynom(len=1)
                fillPol.Pol[0] = fills
                m.mat[i][i] = fillPol
        
        return m

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
        #print("Procces",self.mat[0][0].Pol)
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

    def sub(m1, m2):
        return Matriks.add(m1, Matriks.mult(m2, -1))

    def mult(m1, m2):
        
        if isinstance(m2, Matriks):

            m3 = Matriks(size=(m1.rows, m2.cols))
            if isinstance(m1.mat[0][0], Polynom):
            #Untuk Perkalian Polinom
                for i in range(m3.rows):
                    for j in range(m3.cols):
                        fillPol = Polynom()
                        for k in range(m1.cols):
                            fillPol += (m1.mat[i][k]) * (m2.mat[k][j])
                            #print(fillPol, m1.mat[i][k] , (m2.mat[k][j]))
                        m3.mat[i][j] = fillPol
            else:
                for i in range(m3.rows):
                    l = 0
                    for j in range(m3.cols):
                        for k in range(m1.cols):
                            m3.mat[i][j] += (m1.mat[i][k]) * (m2.mat[k][l])
                        l+=1
        else:
            m3 = Matriks(size=m1.size)
            for i in range(m3.rows):
                for j in range(m3.cols):
                    m3.mat[i][j] = m1.mat[i][j] * m2

        return m3
    
    def isAllColsZero(m, row, col):
        ans = True
        
        for i in range(row, m.rows):    
            if m.mat[i][col] != 0:
                ans = False
                break
        
        return ans

    def reduksi(m):
        # Matriks yang diterima adalah yang sudah disimplified
        m.simplified()
        mTemp = m.copy()
        colLead = 0
        rowLead = 0

        while (colLead < mTemp.cols and rowLead < mTemp.rows):
            #Jika ada kolom yang full kosong
            if (Matriks.isAllColsZero(mTemp,rowLead,colLead)):
                colLead += 1
                continue
            
            
            #print("Start\n",rowLead,colLead,mTemp)        
            
            #Jika ada leading value yang nol
            k = rowLead
            while (mTemp.mat[rowLead][colLead] == 0 and (k < mTemp.rows)):
                # Mengecek dari baris rowLead
                if (rowLead!=k):
                    for j in range(mTemp.cols):
                        #swaping rows
                        mTemp.mat[rowLead][j], mTemp.mat[k][j] = mTemp.mat[k][j], mTemp.mat[rowLead][j]
                k+=1
            
                  
            #Merubah leading value menjadi 1
            ratio = mTemp.mat[rowLead][colLead]
            for j in range(colLead, mTemp.cols):
                mTemp.mat[rowLead][j] /= ratio
            
                 
            #Mulai Mereduksi
            for j in range(rowLead,mTemp.rows):
                if (j != rowLead):
                    ratio = mTemp.mat[j][colLead]/mTemp.mat[rowLead][colLead]
                    for k in range(mTemp.cols):
                        mTemp.mat[j][k] -= mTemp.mat[rowLead][k] * ratio

            colLead += 1
            rowLead += 1
        return mTemp

    def simplified(self):
        if isinstance(self.mat[0][0], Polynom):
            # Merubah isi polinom menjadi angka biasa
            for i in range(self.rows):
                for j in range(self.cols):
                    self.mat[i][j] = self.mat[i][j].Pol[0]

    def round(self, decimal_places = DECIMAL_PLACES):
        for i in range(self.rows):
            for j in range(self.cols):
                self.mat[i][j] = round(self.mat[i][j], decimal_places)