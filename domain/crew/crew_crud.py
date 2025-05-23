from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import Integer
from datetime import datetime

from models import CrewPost, DeletedCrew,CrewApply
from domain.crew import crew_schema

#안전성 증진을 위한 int 데이터 검증 함수
#파라미터 설정에서 옵셔널이 아닌 데이터형을 모두 설정했으니 데이터가 없으면 알아서 걸러줌
#그래서 음수인 값만 예외처리해주면 됨
def num_is_valid(num : int):
    if num < 0:
        raise HTTPException(status_code = 400, detail = "잘못된 접근")
    return num


##여기서부터 데이터 처리 함수 시작
def show_crew(db : Session):
    crew_list = db.query(CrewPost).order_by(CrewPost.id.asc()).all()
    #빈 리스트가 반환된다면 아무것도 없다는 것을 의미
    if crew_list == []:
        return {"message": "아직 아무 게시물도 없습니다."}
    return crew_list

def serching_crew(post_num : int, db : Session):
    post_num = num_is_valid(post_num)
    
    data = db.query(CrewPost).filter(CrewPost.id == post_num).first()

    if data is None:
        raise HTTPException(status_code = 404, detail = "해당 게시물을 찾을 수 없습니다.")
    return data

def post_crew(request_user_id : int, request : crew_schema.CrewPostRequest,db : Session):
    request_user_id = num_is_valid(request_user_id)

    new_crew = CrewPost(
        post_user_id = request_user_id,
        **request.dict(),
        create_on = datetime.now()
    )

    db.add(new_crew)
    db.commit()
    return {"message":"성공적으로 등록되었습니다."}

def apply_crew(request_user_id : int, post_num : int, request : crew_schema.CrewApplyRequest, db : Session):
    request_user_id = num_is_valid(request_user_id)
    post_num = num_is_valid(post_num)

    apply = CrewApply(
        post_num = post_num,
        user_id = request_user_id,
        content = request.content,
        create_on = datetime.now()
    )

    db.add(apply)
    db.commit()
    return {"message":"성공적으로 등록되었습니다."}

#forntend에서 수정버튼을 누르면 원래 있었던 data를 보여줌
#그리고 나서 data를 수정하는데 안 바꾸면 그냥 원래 있던 애들 그대로를 집어넣음
def modifing_post(request_user_id : int , post_num : int, request : crew_schema.CrewModifyRequest, db : Session):
    request_user_id = num_is_valid(request_user_id)
    post_num = num_is_valid(post_num)

    patch_db = db.query(CrewPost).filter(CrewPost.id == post_num).first()
    if patch_db.post_user_id != request_user_id:
        raise HTTPException(status_code = 401, detail = "수정권한은 작성자에게만 있습니다.")

    patch_db.content = request.content + f"\n\n{datetime.now()}수정됨"
    patch_db.subject = request.subject
    
    #이미 DB에 있으니 굳이 add는 안해도 된다
    db.commit()
    return {"message":"성공적으로 수정되었습니다."}

def delete_crew(request_user_id : int, post_num : int, db : Session):
    request_user_id = num_is_valid(request_user_id)

    data = db.query(CrewPost).filter(CrewPost.id == post_num).first()
    if data.post_user_id != request_user_id:
        raise HTTPException(status_code = 401, detail = "게시물은 작성자와 운영자 외에 삭제 불가능합니다.")
    
    deleted_data = DeletedCrew(
        subject = data.subject,
        content = data.content,
        post_num = data.id,
        post_user_id = data.post_user_id,
        deleted_on = datetime.now()
    )

    db.add(deleted_data)
    db.delete(data)
    
    db.commit()
    return {"message" : "성공적으로 삭제 되었습니다."}