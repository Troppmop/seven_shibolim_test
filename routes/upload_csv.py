from fastapi import UploadFile, APIRouter, File

from utils.upload_response import response

router = APIRouter()

@router.post("/assignWithCsv/")
def upload_csv(file: UploadFile = File()):
    return response(file)