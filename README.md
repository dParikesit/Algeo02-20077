# Tugas Besar II IF2123 Aljabar Linier dan Geometri <br/> Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar
> _Program Ini Dibuat Untuk Memenuhi Tugas Perkuliahan Mata Kuliah Aljabar Linier dan Geometri (IF2123)_ <br/>
>
> _Program Studi Teknik Informatika <br/>
> Sekolah Teknik Elektro dan Informatika <br/>
> Institut Teknologi Bandung <br/>
> Semester I Tahun 2021/2022 <br/>_

## Table of Contents
* [Tech Stack](#tech-stack)
* [Deployment](#deployment)
* [Contributors](#contributors)

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
<table>
    <tr>
      <td><b>Nama</b></td>
      <td><b>NIM</b></td>
    </tr>
    <tr>
      <td><a href="https://github.com/sivaren"><b>Rava Naufal Attar</b></a></td>
      <td><b>13520077</b></td>
    </tr>
    <tr>
      <td><a href="https://github.com/dParikesit"><b>Dimas Shidqi Parikesit</b></a></td>
      <td><b>13520087</b></td>
    </tr>
    <tr>
      <td><a href="https://github.com/Audino723"><b>Rio Alexander Audino</b></a></td>
      <td><b>13520088</b></td>
    </tr>
</table>
