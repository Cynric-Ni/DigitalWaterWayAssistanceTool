from sqlalchemy import Column,String,Integer,DateTime,text,Text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 航标调度任务(Base):
    __tablename__ = '航标调度任务'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    fsr_id = Column(String(255))
    jsr_id = Column(String(255))
    rwnr = Column(Text)
    cljg = Column(Text)
    hd_rwzt = Column(Integer())
    hd_zxzt = Column(String(50))
    rwsj = Column(DateTime())
    clsj = Column(DateTime())
    wcsj = Column(DateTime())
    fzr_id = Column(String(255))
    ssjg_id = Column(String(50))
    hb_id = Column(String(50))
    hb_bjdj =  Column(Integer())
    bjxx_id = Column(String(50),index=True)
    hfnr = Column(Text)
    cb_id_id =  Column(String(50))
    zxbm_id = Column(String(50))
    qqr_id = Column(String(50))
    qrsj = Column(DateTime())
    cjbm_id =Column(String(50))
    xgcs =  Column(Integer())
    flag =  Column(Integer())
    定级 =  Column(Integer())
    分类 =  Column(Integer())
    调度类型 =Column(String(50))
    调度阶段外是否合格=  Column(Integer())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }


    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession,查询开始时间,查询结束时间):
        data= 数据导出.航标调度任务导出(查询开始时间,查询结束时间)
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df['rwnr'] = df['rwnr'].str.replace('\n', ' ')
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [航标调度任务(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配调度类型(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标调度任务
SET
    调度类型 = CASE
                WHEN 分类 = 1 AND 定级=1 THEN '一类'
                WHEN 定级=3 AND 分类 = 4 and rwnr like "%基点%" THEN '基点修正'
                WHEN 定级=3 AND 分类 = 3 and rwnr like "%现场作业%" THEN '现场作业'
                WHEN 定级=3 AND 分类 = 3 and rwnr like "%综合手段%" THEN '综合手段'  
                ELSE 航标调度任务.调度类型
           END;''')

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()




if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()


