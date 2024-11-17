from fastapi import APIRouter

from server.router.data_sync import DataSync

router = APIRouter()

router.add_api_route('/get_google_sheets_data', DataSync.get_google_sheets_data, methods=['POST'])