# Tugas Besar II IF2123 Aljabar Linier dan Geometri <br/> Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar
> _Program Ini Dibuat Untuk Memenuhi Tugas Perkuliahan Mata Kuliah Aljabar Linier dan Geometri (IF2123)_ <br/>
>
> _Program Studi Teknik Informatika <br/>
> Sekolah Teknik Elektro dan Informatika <br/>
> Institut Teknologi Bandung <br/>
> Semester I Tahun 2021/2022 <br/>_

## Table of Contents
* [General Information](#general-information)
* [Web Design](#web-design)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Deployment](#deployment)
* [Screenshot](#screenshot)
* [Project Status](#project-status)
* [Contributors](#contributors)

## General Information
- Program kompresi gambar dengan memanfaatkan algoritma SVD (_Singular Value Decomposition_) dalam bentuk website lokal sederhana
- Website dapat menerima file gambar beserta _input_ tingkat kompresi gambar
- Website dapat menampilkan gambar _input_, _output_, _runtime_ algoritma, dan persentase hasil kompresi gambar (perubahan jumlah pixel gambar)
- File _output_ hasil kompresi dapat diunduh melalui website

## Web Design
> You can see it [_here_](https://www.figma.com/file/jsMp4hkcpi8EAUo395qvNu/Algeo02-20077?node-id=6%3A54).

## Tech Stack
- **Client:** HTML, CSS, Vanilla Javascript <br/>
- **Server:** FastAPI, OpenCV

## Prerequisites
> **Pastikan branch repository berada di `master`** </br>

**Clone repository ini menggunakan command berikut (git bash)**
```
$ git clone https://github.com/dParikesit/Algeo02-20077.git
```

## Deployment
> **To first setup this project run**

Windows (open `cmd` on this folder)
```bash
  CD.\src
  python -m venv algeo
  algeo\Scripts\activate.bat
  pip install -r requirements-win.txt
  uvicorn main:app
```

Linux
```bash
  chmod +x setup.sh
  ./src/setup.sh
```

> **If you have ran setup and want to start server** 

Windows (open `cmd` on this folder)
```bash
  algeo\Scripts\activate.bat
  uvicorn main:app
```

Linux
```bash
  chmod +x run.sh
  ./src/run.sh
```

## Screenshot
> ![test 0 1](https://user-images.githubusercontent.com/88304340/141690259-d4e9511a-0a4f-4a05-9173-1d112d34dd08.png)

## Project Status
> **Project is: _complete_**

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
