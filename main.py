from fastapi import FastAPI

from routes.upload_csv import router as csv_route
 
#initialize server
app = FastAPI()

app.include_router(csv_route)