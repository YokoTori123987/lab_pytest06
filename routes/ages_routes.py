from fastapi import APIRouter
import datetime

year_api_router = APIRouter()
y = datetime.datetime.now()

@year_api_router.get("/service/getage")
async def get_test(year: int):
    age = (y.year+543) - year
    return {"age": age}

# @year_api_router.get("/service/getage/str")
# async def get_test(year: str):
#     return {"age": year + "no"}