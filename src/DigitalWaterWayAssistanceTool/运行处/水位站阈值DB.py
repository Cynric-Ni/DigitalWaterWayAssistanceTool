from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class 水位站阈值(Base):
    __tablename__ = '水位站阈值'
    水位站ID = Column(String(100), primary_key=True,unique=True)  # id
    水位站 = Column(String(100))
    阈值 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }