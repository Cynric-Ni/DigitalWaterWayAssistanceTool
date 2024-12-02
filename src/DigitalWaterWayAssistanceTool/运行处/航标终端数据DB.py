from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 终端数据(Base):
    __tablename__ = '终端数据'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hb_id = Column(String(255),index=True)
    sim = Column(String(50))
    imei = Column(String(50))
    hbdxh = Column(String(50))
    zddydmx = Column(Float())
    zddygmx = Column(Float())
    rgyz = Column(Float())
    lxzq = Column(Integer())
    bjzq = Column(Integer())
    bjlmd = Column(Integer())
    gpsjd = Column(Integer())
    dqdymxsz = Column(String(255))
    rgyzszyx = Column(String(255))
    ckdzszyx = Column(String(255))
    hb_dyxms = Column(Integer())
    hb_qzgzms = Column(Integer())
    hb_dqzgz = Column(Integer())
    hb_sfcs = Column(String(255))
    imsi = Column(String(255))
    zdxlh = Column(String(50))
    zdgjh = Column(String(50))
    zdgjh2 = Column(String(50))
    zdcph_id = Column(String(50))
    zdrjbbh = Column(String(50))
    hb_zdlx = Column(String(50))
    hb_zdzt = Column(String(50))
    bhyhm = Column(String(50))
    fwqip = Column(String(50))
    fwqdk = Column(String(50))
    bhhm = Column(String(50))
    bhmm = Column(String(50))
    apn = Column(String(50))
    txptupl = Column(String(50))
    xtjg = Column(Integer())
    dns = Column(String(50))
    jmlx = Column(String(50))
    jcmy = Column(String(50))
    wyfz = Column(Float())
    pyfz = Column(Float())
    jdjd = Column(Float())
    jdwd = Column(Float())
    dmsj = Column(Float())
    hb_zddz = Column(Integer())
    dxzx = Column(String(50))
    dxpt = Column(String(50))
    dxtf = Column(String(50))
    wljrd = Column(String(50))
    dydmx = Column(Float())
    dygmx = Column(Float())
    flag = Column(Integer())
    ssjg_id = Column(String(50))
    qyjcs = Column(Integer())
    ty_zdsyzt = Column(String(50))
    cj = Column(String(50))
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }


    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        data= 数据导出.终端数据导出()
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [终端数据(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()

if __name__ == "__main__":
    sqlsession, engine,第一天,最后一天 = 统计表.日报()
    终端数据.建表(终端数据, sqlsession, engine)
    终端数据.数据导入(sqlsession)

