# Tugas Besar II IF2123 Aljabar Linier dan Geometri <br/> Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar
> _Program Ini Dibuat Untuk Memenuhi Tugas Perkuliahan Mata Kuliah Aljabar Linier dan Geometri (IF2123)_ <br/>
>
> _Program Studi Teknik Informatika <br/>
> Sekolah Teknik Elektro dan Informatika <br/>
> Institut Teknologi Bandung <br/>
> Semester I Tahun 2021/2022 <br/>_

## Table of Contents
* [Tech Stack](#tech-stack)

## Tech Stack

**Client:** HTML, CSS, Vanilla Javascript

**Server:** FastAPI, openCV

## Deployment

To first setup this project run

Windows (open cmd on this folder):
```bash
  CD.\src
  python -m venv algeo
  algeo\Scripts\activate.bat
  pip install -r requirements-win.txt
  uvicorn main:app
```
Linux:
```bash
  chmod +x setup.sh
  ./src/setup.sh
```

If you have ran setup and want to start server
Windows (open cmd on this folder):
```bash
  algeo\Scripts\activate.bat
  uvicorn main:app
```
Linux:
```bash
  chmod +x run.sh
  ./src/run.sh
```

## Contributors
 - [Dimas Shidqi Parikesit](https://github.com/dParikesit)
 - [Rava Naufal Attar](https://github.com/sivaren)
 - [Rio Alexander Audino](https://github.com/Audino723)
