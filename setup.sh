#! /bin/bash

echo "Website setup akan dimulai. Silahkan ditunggu terlebih dahulu"

echo "1. cd to src"
cd src

echo "2. Create python venv"
python3 -m venv algeo

echo "3. Activating venv"
source algeo/bin/activate

echo "4. Install dependencies"
pip install -r requirements.txt

echo "5. Running website"
uvicorn main:app