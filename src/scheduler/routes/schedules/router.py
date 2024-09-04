from fastapi import APIRouter

router = APIRouter()

sample =[{
    "start_time":"2024, 9, 1, 10, 45, 53, 550141",
    "end_time":"(2024, 9, 1, 17, 45, 53, 550141",
    "utc_datetime": "2024, 9, 1, 21, 54, 49, 832923",
    "location":"conover, field-4",
    "field_team_status": "home",
    "opponent" : "sideways cats"
},{
    "start_time":"2024, 10, 1, 10, 45, 53, 550141",
    "end_time":"(2024, 10, 1, 17, 45, 53, 550141",
    "utc_datetime": "2024, 9, 1, 21, 54, 49, 832923",
    "location":"conover, field-4",
    "field_team_status": "vistor",
    "opponent" : "sideways cats"
}]



@router.get("/", tags=["schedules"])
async def teams_schedule ():
    return {"data": sample}
