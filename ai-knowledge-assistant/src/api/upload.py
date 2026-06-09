from fastapi import (APIRouter,UploadFile)

from src.services.upload_service import (upload_document)

router = APIRouter()

@router.post("/")
async def upload(file: UploadFile):
    return upload_document(file)