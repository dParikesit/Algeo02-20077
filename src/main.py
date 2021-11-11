import os
import secrets
import time
from typing import Optional
from fastapi import FastAPI, File, Form, UploadFile
from fastapi import staticfiles
from fastapi.param_functions import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.background import BackgroundTasks
from processor.image import compress

app = FastAPI()

print("Welcome to Algeo SVD Image Compressor")

async def chunked_copy(src, dst):
    start = time.perf_counter_ns()
    await src.seek(0)
    with open(dst, "wb+") as buffer:
        while True:
            contents = await src.read(1024)
            if not contents:
                break
            buffer.write(contents)
    stop = time.perf_counter_ns()
    return stop-start


@app.post("/files/")
async def upload_file(
    file: UploadFile = File(...), rate: str = Form(...)
):
    print(rate)
    fileId = secrets.token_urlsafe()
    extension = (os.path.splitext(file.filename)[1])
    filePath = os.path.join("files", fileId+extension)
    time = await chunked_copy(file, filePath)
    compress(filePath)
    
    return{
        "time": time,
        "fileId": fileId,
        "fileExt": extension[1:]
    }


@app.get("/files/{file_id}/{ext}")
async def send_file(file_id: str, bgTask: BackgroundTasks, ext: str):
    filePath = os.path.join("files", file_id+"."+str(ext))
    print(os.path.isfile(filePath))

    bgTask.add_task(os.remove, filePath)
    return FileResponse(filePath, background=bgTask)

app.mount("/", StaticFiles(directory="frontend", html=True), name="static")