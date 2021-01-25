from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.post("/files/")
async def read_file(file: UploadFile = File(...)):
    file_data = await file.read()
    with open(file.filename, "wb") as f:
        f.write(file_data)
    # 参考リンク https://qiita.com/ke_ix1/items/7a4face267bace3dcfa7
    return {"text": file.filename}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
