from fastapi import APIRouter
import datetime
# from datetime import date
year_api_router = APIRouter()
y = datetime.datetime.now()
# years = date.today().year

@year_api_router.get("/service/getage")
async def get_test(year: int):
    if year != 0:
        # if year >= years:
        age = (y.year+543) - year
        return {"age": age}
        # else:
            # return {"age": "Can't input less than zero"}
    else:
        return {"age": "Can't input less than zero"}

# @year_api_router.get("/service/getage/str")
# async def get_test(year: str):
#     return {"age": year + "no"}