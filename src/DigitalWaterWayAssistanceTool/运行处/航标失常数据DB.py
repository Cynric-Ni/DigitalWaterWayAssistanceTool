from sqlalchemy import Column,String,Integer,DateTime,Float,text,Text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 航标失常恢复(Base):
    __tablename__ = '航标失常恢复'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hb_sclx = Column(Integer())
    hb_scyylx = Column(Integer())
    hb_scxz = Column(Integer())
    hb_id = Column(String(255), index=True)
    bjxx_id = Column(String(50))
    xdsj = Column(DateTime())
    wcsj = Column(DateTime())
    rwnr = Column(String(255))
    hd_rwzt = Column(String(255))
    hd_zxzt = Column(String(255))
    cbchjl_id = Column(String(255))
    flag = Column(Integer())
    zpdw_id = Column(String(255))
    cb_id = Column(String(255))
    whr_id = Column(String(255))
    单位 = Column(String(50))
    航标 = Column(String(50))
    失常类型 = Column(String(50))
    匹配报警 = Column(String(255))
    匹配通告 = Column(String(255))
    报警开始时间 = Column(DateTime())
    报警结束时间 = Column(DateTime())
    报警类型 = Column(String(50))
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession,查询开始时间,查询结束时间):
        data= 数据导出.航标失常数据导出(查询开始时间,查询结束时间)
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [航标失常恢复(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配单位_航标(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标失常恢复 
JOIN 航标基础数据 
ON 航标基础数据.id = 航标失常恢复.hb_id 
SET 航标失常恢复.单位 = 航标基础数据.单位,
航标失常恢复.航标 = 航标基础数据.hbmc'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配失常类型(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标失常恢复 
JOIN 基础数据.失常类型
ON 航标失常恢复.hb_sclx = 基础数据.失常类型.id 
SET 航标失常恢复.失常类型 = 基础数据.失常类型.类型'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()


if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()


