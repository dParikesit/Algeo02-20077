@ECHO OFF
TITLE "SVD Setup"
ECHO "Website setup akan dimulai. Silahkan ditunggu terlebih dahulu"

ECHO "1. cd to src"
CD.\src

ECHO "2. Create python venv"
python3 -m venv algeo

ECHO "3. Activating venv"
source algeo\Scripts\activate.bat

ECHO "4. Install dependencies"
pip install -r requirements.txt

ECHO "5. Running Website"
uvicorn main:app