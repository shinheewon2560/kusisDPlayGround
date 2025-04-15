# init_db.py
#데이터 베이스에 조그마한 수정이 있어도 다시 생성해야함
from database import Base, engine, SessionLocal
from models import Crew,User,Operator
from datetime import datetime

# 테이블 생성
Base.metadata.create_all(bind=engine)

db = SessionLocal()

user = User(user_name = "신희원", user_hello = "제가 이 프로그램 재작자입니다,\n히힣,,,,,,저 좀 멋지죠?ㅎ", create_on = datetime.now())
crew = Crew(subject = "test", content = "networking ok", create_on = datetime.now(),post_user_id = 1)
operator = Operator(name = "신희원",description = "프로젝트 창시자\n프로젝트 PL",create_on = None)
db.add(user)
db.add(crew)
db.add(operator)

db.commit()