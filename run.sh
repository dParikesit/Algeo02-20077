#! /bin/bash

ECHO "Running website..."
cd src
source algeo/bin/activate
uvicorn main:app