from fastapi import APIRouter,Depends,Response,status
from sqlalchemy.orm import Session
from domain.crew import crew_schema

from database import get_DB
from domain.crew import crew_schema, crew_crud

router = APIRouter(
    prefix = "/kusisD/crew"
)

#소모임 리스트 출력
@router.get("/list")
def show_crew_list(response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.show_crew(db)
    response.status_code = status.HTTP_202_ACCEPTED
    return _result

#소모임 객체 출력
@router.get("/list/{post_num}")
def serching_id(post_num : int, response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.serching_crew(post_num,db)
    response.status_code = status.HTTP_200_OK
    return _result

#소모임 추가
@router.post("/post")
def add_crew(request_user_id : int ,request : crew_schema.CrewPostRequest,response: Response, db : Session = Depends(get_DB)):
    _result = crew_crud.post_crew(request_user_id, request, db)
    response.status_code = status.HTTP_201_CREATED
    return _result

#소모임 게시물 수정
@router.put("/modify")
def modify_crew(request_user_id : int, post_num : int ,request : crew_schema.CrewModifyRequest, response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.modifing_post(request_user_id, post_num,request, db)
    response.status_code = status.HTTP_202_ACCEPTED
    return _result

#소모임 삭제
@router.delete("/delete")
def delete_crew(request_user_id : int, post_num : int, response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.delete_crew(request_user_id,post_num, db)
    response.status_code = status.HTTP_204_NO_CONTENT
    return _result

#소모임 지원서 목록 보기
#@

#소모임 개별 지원서 보기
#@

#소모임 지원서 추가
@router.post("/apply/post")
def apply_crew(request_user_id : int , post_num : int ,request : crew_schema.CrewApplyRequest, response : Response, db : Session = Depends(get_DB)):
    _result = crew_crud.apply_crew(request_user_id, post_num, request,db)
    response.status_code = status.HTTP_201_CREATED
    return _result

#소모임 지원서 수정
#@

#소모임 지원서 삭제
#@