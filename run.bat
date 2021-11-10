@ECHO OFF
TITLE "ALGEO SVD"
ECHO "Running website..."

CD.\src
algeo\Scripts\activate.bat
uvicorn main:app