from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
import io

app = FastAPI()

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
    try:
        # Read the file into memory
        contents = await file.read()
        pdf_file = io.BytesIO(contents)
        
        # Initialize the PDF Reader
        reader = PdfReader(pdf_file)
        number_of_pages = len(reader.pages)
        
        # Extract text from the first page as a sample
        first_page = reader.pages[0]
        text_sample = first_page.extract_text()[:200] # Get first 200 characters

        return {
            "message": f"Successfully processed {file.filename}!",
            "pages": number_of_pages,
            "preview": text_sample
        }
    except Exception as e:
        return {"message": f"Error: {str(e)}"}
