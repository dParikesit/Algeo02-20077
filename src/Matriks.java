
public class Matriks {
    // Atribut
    public int row;
    public int col;
    public double[][] Mat; 
    final int UNVAL_INDEX = -1;
    final int UNVAL_VALUE = -999;

    // Method:
    Matriks(int row, int col) {
        this.col = col;
        this.row = row;

        int i, j;

        if (row > UNVAL_INDEX && col > UNVAL_INDEX) {
            this.Mat = new double[this.row][this.col];
            for (i = 0; i < row; i++) {
                for (j = 0; j < col; j++) {
                    this.Mat[i][j] = 0;
                }
            }
        }
    }

    public boolean isRowSPLZero (int i, int jStart, int jMax){
        /*
        Mengembalikan true jika kolom spl pada matrix augmented bernilai nol semua, dengan kata lain tidak memiliki penyelesaian.
        */
            //KAMUS
            boolean flag = true;
            int j;
    
            //ALGORITMA
            for (j = jStart; j < jMax; j ++){
                if (this.Mat[i][j] != 0){
                    flag = false;
                    break;
                }
            }
    
            return flag;
        }

    public boolean isZeroColExist(int iStart, int jStart) {
        int i;
        boolean isZero;
        isZero = true;

        for (i = iStart; i < this.row; i++) {
            if (this.Mat[i][jStart] != 0) {
                isZero = false;
                break;
            }
        }
        return isZero;

    }

    public Matriks Transpose() {
        Matriks m2 = new Matriks(this.col, this.row);

        for (int i = 0; i < this.row; i++) {
            for (int j = 0; j < this.col; j++) {
                m2.Mat[j][i] = this.Mat[i][j];
            }
        }

        return m2;
    }

    public Matriks reduksiMatriks(){
        //KAMUS
        int i, j, k;
        double ratio;
        Matriks mTemp;
        mTemp = this;

        //ALGORITMA
        for (i = 0; (i < mTemp.row) && (i < mTemp.col-1) ; ++i) {
            k = 0;

            //Mengecek apakah ada satu column yang nol semua
            if (i<mTemp.col-2 && this.isZeroColExist(i, i) ) {
                continue;
            }

            //Mengecek apakah ada nilai (i,i) yang nol
            while ((i < mTemp.col-1) && (k + i < mTemp.row-1) && (mTemp.Mat[i + k][i] == 0)) {
                k++;
                if (mTemp.Mat[i + k][i] != 0) {
                    for (j = 0; j < mTemp.col; ++j) {
                        mTemp.Mat[i][j] += mTemp.Mat[i + k][j];
                    }
                    break;
                }

            }
            
            //Mengurangi sampai nol
            for (j = i + 1; j < mTemp.row; ++j) {
                ratio = mTemp.Mat[j][i] / mTemp.Mat[i][i];
                for (k = i; k < mTemp.col; ++k) {
                    mTemp.Mat[j][k] -= ratio * mTemp.Mat[i][k];
                }
            }
        }

        return mTemp;
    }

    public Matriks konversiEselonMatriks(){
        //KAMUS
        Matriks mTemp = this.reduksiMatriks();
        int i, j;
        double temp;

        //Mengubah matriks tereduksi menjadi matriks tereduksi eselon
        for (i = 0; i < this.row;++i){
            if ((i < mTemp.col) && mTemp.Mat[i][i] != 1 && (mTemp.Mat[i][i] != 0)){

                temp = mTemp.Mat[i][i];
                for (j = 0; j < this.col; j ++){
                    mTemp.Mat[i][j] /= temp;
                }
            }
        }

        return mTemp;
    }

    public Matriks eselonTereduksiMatriks(){
        //KAMUS
        Matriks mTemp = this.konversiEselonMatriks();
        int i, j, k;
        double ratio;

        //ALGORITMA

        //Diiterasi dari baris ujung kiri atas, ke ujung kiri kanan. (i,i)
        for (i = 1; (i < mTemp.row) && (i<mTemp.col-1) ; i ++){
            if (isZeroColExist(0, i) || isRowSPLZero(i, 0, this.col)){
                continue;
            }

            //Diiterasi dari nilai diagonal ke bawah
            for (j = 0; j < mTemp.row; ++j) {
                if (i!= j){
                    ratio = mTemp.Mat[j][i] / mTemp.Mat[i][i];
                    for (k = i; k < mTemp.col ; k ++){
                        mTemp.Mat[j][k] -= ratio * mTemp.Mat[i][k];
                    }
                }
            }
        }
        
        return mTemp;
    }
    
    public static double detKofaktor(Matriks m) {
        // Kamus Lokal
        int i, j, k;
        int kolom, baris;
        int itemp, jtemp;
        double det = 0;
        // Algoritma
        baris = m.row;
        kolom = m.col;
        if (baris == 1) {
            return m.Mat[0][0];
        } else {
            if (baris == 2) {
                return m.Mat[0][0] * m.Mat[1][1] - m.Mat[0][1] * m.Mat[1][0];
            }
            for (i = 0; i < baris; i++) {
                Matriks mtemp = new Matriks(baris - 1, kolom - 1);
                itemp = 0;
                jtemp = 0;
                for (j = 1; j < baris; j++) {
                    for (k = 0; k < kolom; k++) {
                        if (k != i) {
                            mtemp.Mat[itemp][jtemp] = m.Mat[k][j];
                            itemp += 1;
                        }
                    }
                    jtemp += 1;
                    itemp = 0;
                }
                if (i % 2 == 1) {
                    det += -1 * m.Mat[i][0] * detKofaktor(mtemp);
                } else {
                    det += m.Mat[i][0] * detKofaktor(mtemp);
                }
            }
            return det;
        }
    }
}