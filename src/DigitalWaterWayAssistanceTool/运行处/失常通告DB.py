from sqlalchemy import Column,String,Integer,DateTime,Float,text,Text,Index
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 失常恢复通告(Base):
    __tablename__ = '失常恢复通告'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    sd_id =Column(String(255))
    xf_tglb = Column(Integer())
    tgbt = Column(String(255))
    fbqy = Column(String(255))
    tgbh = Column(String(255))
    tgnr = Column(Text)
    fssj = Column(DateTime())
    fbsj = Column(DateTime())
    fbkssj = Column(DateTime())
    fbjssj = Column(DateTime())
    ssjg_id = Column(String(50))
    ngr_id = Column(String(255))
    shr_id = Column(String(255))
    dh = Column(String(255))
    tgkh =  Column(Integer())
    xf_fbqd = Column(String(50))
    xf_bq = Column(String(255))
    tgmb_id = Column(String(255))
    Index('ix_失常恢复通告_tgnr', tgnr, mysql_length=255)
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession,查询开始时间,查询结束时间):
        data= 数据导出.失常通告导出(查询开始时间,查询结束时间)
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [失常恢复通告(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()


