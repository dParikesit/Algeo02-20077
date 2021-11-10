#! /bin/bash

echo "Website setup akan dimulai. Silahkan ditunggu terlebih dahulu"

echo "1. Create python venv"
python3 -m venv algeo

echo "2. Activating venv"
source algeo/bin/activate

echo "3. Install dependencies"
pip install -r requirements.txt

echo "4. Running website"
uvicorn main:app