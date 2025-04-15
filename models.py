from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship

from database import Base

#사용자 정보 담기
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False)
    user_hello = Column(Text, nullable = True)
    create_on = Column(DateTime, nullable = False)

#소모임 게시판 내용
class Crew(Base):
    __tablename__ = "crew"

    id = Column(Integer, primary_key=True, index  = True)
    subject = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    post_user_id = Column(Integer, nullable= False)
    create_on = Column(DateTime, nullable = False)

#운영자 정보 담기
class Operator(Base):
    __tablename__ = "operator"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)
    description = Column(Text , nullable = False)
    create_on = Column(DateTime)

#삭제한 게시물도 운영자는 볼 수 있도록
class DeletedCrew(Base):
    __tablename__ = "deletedCrew"

    id = Column(Integer, primary_key=True, index  = True)
    subject = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    list_index_num = Column(Integer, nullable= False)
    post_user_id = Column(Integer, nullable = False)
    deleted_on = Column(DateTime, nullable = False)