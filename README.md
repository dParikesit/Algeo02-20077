# SVD Image Compression Website

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