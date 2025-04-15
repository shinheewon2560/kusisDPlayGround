from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

#사용자 정보 담기
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = False)
    user_info = Column(Text, nullable = True)
    contact_info = Column(String)
    create_on = Column(DateTime, nullable = False)

    remove = relationship("CrewApply", back_populates = "user", cascade = "all, delete", passive_deletes = True)

#소모임 게시판 내용
class CrewPost(Base):
    __tablename__ = "crew_post"

    id = Column(Integer, primary_key=True, index  = True)

    subject = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    post_user_id = Column(Integer, nullable= False)

    create_on = Column(DateTime, nullable = False)

    remove = relationship("CrewApply", back_populates = "crew_post", cascade = "all, delete", passive_deletes = True)

class CrewApply(Base):
    __tablename__ = "crew_apply"

    id = Column(Integer, primary_key = True)

    post_num = Column(Integer, ForeignKey(CrewPost.id, ondelete = "CASCADE"), nullable = False)
    user_id = Column(Integer, ForeignKey(User.id, ondelete = "CASCADE"), nullable = False)
    content= Column(String, nullable = False)

    create_on = Column(DateTime, nullable = False)

    crew_post = relationship("CrewPost", back_populates = "remove")
    user = relationship("User", back_populates = "remove")

#운영자 정보 담기
class Operator(Base):
    __tablename__ = "operator"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable = False)
    description = Column(Text , nullable = False)
    contact_info = Column(String)

    create_on = Column(DateTime)

#삭제한 게시물도 운영자는 볼 수 있도록
class DeletedCrew(Base):
    __tablename__ = "deleted_crew"

    id = Column(Integer, primary_key=True)

    subject = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    post_num = Column(Integer, nullable= False)
    post_user_id = Column(Integer, nullable = False)

    deleted_on = Column(DateTime, nullable = False)