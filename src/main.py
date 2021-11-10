import os
import secrets
import time
from typing import Optional
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.param_functions import Path
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks
from Processor.image import compress

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
    fileId = secrets.token_urlsafe()
    extension = (os.path.splitext(file.filename)[1])
    filePath = os.path.join("files", fileId+extension)
    compress(filePath)
    time = await chunked_copy(file, filePath)

    return{
        "time": time,
        "fileId": fileId,
        "fileExt": extension[1:]
    }


@app.get("/files/{file_id}")
async def send_file(file_id: str, bgTask: BackgroundTasks, ext: Optional[str] = None):
    filePath = os.path.join("files", file_id+"."+str(ext))

    bgTask.add_task(os.remove, filePath)
    return FileResponse(filePath, background=bgTask)