class Polynom():
    def __init__(self, len = 0, c='X'):
        self.Pol = [0 for _ in range(len)]
        self.Len = len
        self.coef = c

    def __str__(self):
        polStr = ''
        signPlus = False

        for i in range(self.Len):
            val = abs(self.Pol[i])
            if signPlus:
                if (self.Pol[i] > 0):
                    polStr += " + "
                else:
                    polStr += " - "
                signPlus = False
            if (i==0):
                if self.Pol[i] < 0:
                    polStr += "-"
                polStr += str(val)
                signPlus = True
            elif (i>0):
                if (val == 0):
                    continue
                polStr += str(val)
                polStr += (f"{self.coef}^" + str(i))
                signPlus = True
        return polStr
    
    def __add__(self, other):
        newPol = Polynom()
        if isinstance(other, Polynom):
            maxLen = max(self.Len, other.Len)
            newPol.Len = maxLen
            newPol.Pol = [0 for _ in range (maxLen)]

            for i in range(self.Len):
                newPol.Pol[i] += self.Pol[i]
            for j in range(other.Len):
                newPol.Pol[j] += other.Pol[j]

        #Scaler multiplication
        elif isinstance(other, (int, float)):
            newPol.Len = self.Len
            for i in range(self.Len):
                #Hasil perkalian Polinom
                newPol.Pol.append(self.Pol[i])
            newPol.Pol[0] += other

        return newPol

    def __sub__(self, other):
        other *= -1
        newPol = Polynom()
        if isinstance(other, Polynom):
            maxLen = max(self.Len, other.Len)
            newPol.Len = maxLen
            newPol.Pol = [0 for _ in range (maxLen)]

            for i in range(self.Len):
                newPol.Pol[i] += self.Pol[i]
            for j in range(other.Len):
                newPol.Pol[j] += other.Pol[j]

        #Scaler multiplication
        elif isinstance(other, (int, float)):
            newPol.Len = self.Len
            for i in range(self.Len):
                #Hasil perkalian Polinom
                newPol.Pol.append(self.Pol[i])
            newPol.Pol[0] += other

        return newPol

    def __mul__(self, other):
        newPol = Polynom()
        if isinstance(other, Polynom):
            for i in range(self.Len):
                for j in range(other.Len):
                    #Hasil perkalian Polinom
                    temp = self.Pol[i] * other.Pol[j]
                    if (i + j) >= newPol.Len:
                        newPol.Pol.append(temp)
                        newPol.Len += 1
                    else:
                        newPol.Pol[i+j] += temp
        #Scaler multiplication
        elif isinstance(other, (int, float)):
            newPol.Len = self.Len
            for i in range(self.Len):
                #Hasil perkalian Polinom
                newPol.Pol.append(self.Pol[i] * other)

        return newPol

    def fill(self, fills=0):
        self.Pol = [fills for i in range(self.Len)] 


    

            