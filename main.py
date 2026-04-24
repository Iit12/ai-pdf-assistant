from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Your familiar CORS fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "AI Assistant Online"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # This is where we will add the PDF logic tomorrow
    return {"message": f"Received {file.filename}. Ready to process!"}
