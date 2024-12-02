from sqlalchemy import Column,String,DateTime,Float,text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class 水位数据异常(Base):
    __tablename__ = '水位数据异常'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    水位站= Column(String(50))
    测量时间 = Column(DateTime())
    水位 = Column(Float())
    差值 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)
