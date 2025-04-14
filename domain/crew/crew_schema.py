from pydantic import BaseModel, field_validator
from sqlalchemy import String, Text
from datetime import datetime

#pydantic이니까 pydantic의 데이터 형을 써야함
class crew_form(BaseModel):
    subject : str
    content : str

 