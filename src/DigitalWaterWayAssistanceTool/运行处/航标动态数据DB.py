from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 航标动态数据(Base):
    __tablename__ = '航标动态数据'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hb_id = Column(String(255),index=True)
    dqzbjd = Column(Float())
    dqzbwd = Column(Float())
    wyfz = Column(Float())
    pyfz = Column(Float())
    rgfz = Column(Float())
    dqrg = Column(String(50))
    rgsz = Column(String(50))
    sbpc = Column(String(50))
    jspc = Column(String(50))
    ydsd = Column(Float())
    zjmx = Column(String(50))
    bjlmd = Column(String(50))
    dlzt = Column(String(50))
    ckzt = Column(String(50))
    gpsgh = Column(String(50))
    dzzt = Column(String(50))
    cdjc = Column(String(50))
    gmsgh = Column(String(50))
    dqtx = Column(String(50))
    dqkzq = Column(String(50))
    mcugh = Column(String(50))
    dqdz = Column(String(50))
    dlxp = Column(String(50))
    tbss = Column(String(50))
    gpsdw = Column(String(50))
    eprom = Column(String(50))
    lxjg =  Column(Integer())
    gpsjc = Column(String(50))
    adjc = Column(String(50))
    bjjg = Column(Integer())
    ssbj = Column(String(50))
    sybj = Column(String(50))
    dxbj = Column(String(50))
    hbzd_id = Column(String(50))
    jtdy = Column(Float())
    gzdy = Column(Float())
    gzdl = Column(Float())
    cddy = Column(Float())
    cddl = Column(Float())
    szzt = Column(String(50))
    dqcddl = Column(Float())
    dqfddl = Column(Float())
    ytcddl = Column(Float())
    ytfddl = Column(Float())
    sydl = Column(Float())
    dygyz = Column(Float())
    dydyz = Column(Float())
    hbd = Column(String(50))
    hbdjtdy = Column(Float())
    hbdgzdy = Column(Float())
    hbdgzdl = Column(Float())
    hbdcddy = Column(Float())
    hbdcddl = Column(Float())
    hbddygyz = Column(Float())
    hbddydyz = Column(Float())
    ssjg_id = Column(String(50))
    sbsj = Column(DateTime())
    flag = Column(String(50))
    hb_zddz = Column(String(50))
    hbd_ytsydl = Column(Integer())
    qyjcs = Column(Integer())
    gsm_qd = Column(Integer())
    xylx = Column(Integer())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }


    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        data= 数据导出.航标动态数据导出()
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [航标动态数据(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()
    航标动态数据.建表(engine)
    航标动态数据.数据导入(sqlsession)

