from fastapi import APIRouter,Depends,Response,status
from sqlalchemy.ext.asyncio import AsyncSession
from domain.user.user_crud import get_id_from_token

from database import get_DB
from domain.post import post_crud, post_schema

router = APIRouter(
    prefix = "/KU/Post"
)

#개시물 리스트 출력
@router.get("/List/")
async def get_post_list(response : Response, page_num : int, db : AsyncSession = Depends(get_DB)):
    _result = await post_crud.get_post_list_from_db(page_num, db)
    response.status_code = status.HTTP_200_OK
    return _result

#개시물 객체 출력
@router.get("/")
async def get_post_by_id(post_num : int, response : Response, db : AsyncSession = Depends(get_DB)):
    _result = await post_crud.get_post_from_db(post_num,db)
    response.status_code = status.HTTP_200_OK
    return _result

#개시물 추가
@router.post("/")
async def add_post(request : post_schema.PostRequest,response : Response, request_user_id : int = Depends(get_id_from_token), db : AsyncSession = Depends(get_DB)):
    _result = await post_crud.add_post_on_db(request_user_id, request, db)
    response.status_code = status.HTTP_201_CREATED
    return _result

#개시물 게시물 수정
@router.put("/")
async def modify_post(post_num : int ,request : post_schema.ModifyRequest, response : Response, request_user_id : int = Depends(get_id_from_token), db : AsyncSession = Depends(get_DB)):
    _result = await post_crud.modifing_post_in_db(request_user_id, post_num,request, db)
    response.status_code = status.HTTP_200_OK
    return _result

#개시물 삭제
@router.delete("/")
async def delete_post(post_num : int, response : Response, request_user_id : int = Depends(get_id_from_token), db : AsyncSession = Depends(get_DB)):
    await post_crud.delete_post_on_db(request_user_id,post_num, db)
    response.status_code = status.HTTP_204_NO_CONTENT
