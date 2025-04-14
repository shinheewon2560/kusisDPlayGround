# init_db.py
#데이터 베이스에 조그마한 수정이 있어도 다시 생성해야함
from database import Base, engine
from models import Crew  # crew 모델을 import 해서 등록시켜야 함

# 테이블 생성
Base.metadata.create_all(bind=engine)

###table이 생성되지 않아 생성하는 생성자
