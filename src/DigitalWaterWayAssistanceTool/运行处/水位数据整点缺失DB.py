from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class 水位数据整点缺失(Base):
    __tablename__ = '水位数据整点缺失'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    水位站 = Column(String(50))
    缺失时间 = Column(DateTime())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)


