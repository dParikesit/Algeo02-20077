@ECHO OFF
TITLE "ALGEO SVD"
ECHO "Running website..."

CD.\src
source algeo\Scripts\activate.bat
uvicorn main:app