from fastapi import FastAPI, UploadFile, File
import shutil, os

# ✅ Import parser with package prefix
from app.parser import parse_pdf, parse_docx, extract_info

app = FastAPI()

UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Resume Parser API running"}

@app.post("/parse_resume")
async def parse_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = ""
    if file.filename.endswith(".pdf"):
        text = parse_pdf(file_path)
    elif file.filename.endswith(".docx"):
        text = parse_docx(file_path)
    else:
        return {"error": "Unsupported file format"}

    extracted = extract_info(text)
    return extracted
