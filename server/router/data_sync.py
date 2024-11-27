from fastapi import HTTPException
from pydantic import BaseModel

from googleapiclient.discovery import build

class GoogleSheetsRequest(BaseModel):
    api_key: str
    spreadsheet_id: str
    range: str

class DataSync:
    async def get_google_sheets_data(request_data: GoogleSheetsRequest):
        try:
            service = build("sheets", "v4", developerKey=request_data.api_key)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=request_data.spreadsheet_id, range=request_data.range_name).execute()
        
            values = result.get("values")

            return { "data": values }
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Bad Request") from e