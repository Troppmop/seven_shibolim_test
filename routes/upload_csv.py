from fastapi import UploadFile, APIRouter, File

from utils.csv_handler import process_csv

router = APIRouter()

@router.post("/assignWithCsv/")
def upload_csv(file: UploadFile = File()):
    return process_csv(file)