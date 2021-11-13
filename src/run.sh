#! /bin/bash

echo "Running website..."
source algeo/bin/activate
uvicorn main:app 