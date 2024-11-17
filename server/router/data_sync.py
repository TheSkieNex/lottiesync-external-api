from fastapi import HTTPException
from pydantic import BaseModel

class GoogleSheetsRequest(BaseModel):
    token: str

class DataSync:
    async def get_google_sheets_data(request_data: GoogleSheetsRequest):
        try:
            print(request_data.token)

            return {"success": "Data received"}
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Bad Request") from e