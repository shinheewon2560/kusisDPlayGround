from database import SessionLocal
from models import Crew,User,Operator
from datetime import datetime

db = SessionLocal()

#q = db.get(Crew,2)

#db.delete(q)
user = User(user_name = "신희원", user_hello = "제가 이 프로그램 재작자입니다,\n히힣,,,,,,저 좀 멋지죠?ㅎ", create_date = datetime.now())
crew = Crew(subject = "test", content = "networking ok", create_date = datetime.now(),post_user_id = 1)
operator = Operator(name = "신희원")
db.add(user)
db.add(crew)
db.add(operator)
db.commit()