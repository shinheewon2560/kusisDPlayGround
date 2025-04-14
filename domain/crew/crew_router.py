from fastapi import APIRouter,Depends,Response,status
from sqlalchemy.orm import Session
from domain.crew import crew_schema
from datetime import datetime
from models import Crew
from database import get_DB
from domain.crew import crew_schema, crew_crud

router = APIRouter(
    prefix = "/kusisD/crew"
)

@router.get("/list")
def show_crew_list(response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.show_crew(db)
    response.status_code = status.HTTP_202_ACCEPTED
    return _result

@router.post("/add")
def add_crew(CrewApply : crew_schema.crew_form, user_id : int, response: Response, db : Session = Depends(get_DB)):
    _result = crew_crud.post_crew(db, CrewApply,user_id)
    response.status_code = status.HTTP_202_ACCEPTED
    return _result

@router.put("/modify")
def modify_crew(crew_id : int, CrewModify : crew_schema.crew_form, user_id : int, response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.update_crew(CrewModify,crew_id, user_id, db)
    response.status_code = status.HTTP_202_ACCEPTED
    return _result
