from fastapi import FastAPI
from routes.ages_routes import year_api_router

app = FastAPI()

app.include_router(year_api_router)