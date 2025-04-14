from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import String, Text,Integer
from datetime import datetime

from models import Crew
from domain.crew import crew_schema

def show_crew(db : Session):
    crew_list = db.query(Crew).order_by(Crew.id.asc()).all()
    if crew_list is None:
        return HTTPException(status_code = 404, detail = "해당 게시물을 찾을 수 없습니다.")
    return crew_list

def post_crew(db : Session, CrewApply : crew_schema.crew_form, user_id : Integer):
    new_crew = Crew(
        subject = CrewApply.subject,
        content = CrewApply.content,
        post_user_id = user_id,
        create_date = datetime.now()
    )
    if new_crew.subject is None or new_crew.content is None:
        return HTTPException(status_code=400,detail = "잘못된 응답입니다.")
    
    db.add(new_crew)
    db.commit()
    return {"message":"성공적으로 등록되었습니다."}


#forntend에서 수정버튼을 누르면 원래 있었던 data를 보여줌
#그리고 나서 data를 수정하는데 안 바꾸면 그냥 원래 있던 애들 그대로를 집어넣음
def update_crew( newdata : crew_schema.crew_form, crew_id : Integer, user_id : Integer, db : Session):
    patch_db = db.query(Crew).filter(Crew.id == crew_id).first()
    if user_id != patch_db.post_user_id:
        return HTTPException(status_code = 401, detail = "게시물은 작성자와 운영자 외에 수정 불가능합니다.")
    if patch_db is None:
        return HTTPException(status_code = 404, datail = "해당 게시물을 찾을 수 없습니다.")

    patch_db.content = newdata.content + f"{datetime.now()}수정됨"
    patch_db.subject = newdata.subject
    
    #이미 DB에 있으니 굳이 add는 안해도 된다
    db.commit()
    return {"message":"성공적으로 수정되었습니다."}