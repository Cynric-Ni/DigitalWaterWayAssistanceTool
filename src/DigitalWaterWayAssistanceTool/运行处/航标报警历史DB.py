from sqlalchemy import Column,String,Integer,DateTime,Float,text,Text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 航标报警历史(Base):
    __tablename__ = '航标报警历史'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hb_id = Column(String(255),index=True)
    sim = Column(String(50))
    hb_bjlx = Column(Integer())
    bjsj = Column(DateTime())
    bjyy = Column(String(255))
    hb_bjdj = Column(String(50))
    ty_bjqrzt = Column(Integer())
    hb_bjyqddj = Column(Integer())
    bjyyjson = Column(String(255))
    bjqrsj = Column(DateTime())
    dbcs = Column(Integer())
    hb_bjdbzt = Column(Integer())
    tzsj = Column(DateTime())
    xysj = Column(DateTime())
    wxyyy = Column(String(255))
    czqk = Column(String(50))
    sfjc  = Column(Integer())
    czsj = Column(DateTime())
    gzcdtgz = Column(String(255))
    ssjg_id = Column(String(255))
    tbr_id = Column(String(255))
    tbsj = Column(DateTime())
    zhdjsj = Column(DateTime())
    bjjssj = Column(DateTime())
    bjxcjssj = Column(DateTime())
    flag = Column(Integer())
    yjc = Column(String(255))
    scbjsj = Column(DateTime())
    bhs = Column(Integer())
    sftc = Column(Integer())
    qyjcs = Column(Integer())
    sfyx = Column(Integer())
    xxms = Column(String(255))
    浮标 = Column(Integer())
    重点航标 = Column(Integer())
    夜间 = Column(Integer())
    报警时长 = Column(Float())
    单位 = Column(String(50))
    航标 = Column(String(50))
    最后调度时间 = Column(DateTime())
    最后定级 = Column(Integer())
    最后分类 = Column(Integer())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }


    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession, 查询开始时间, 查询结束时间):
        data = 数据导出.航标报警历史导出(查询开始时间, 查询结束时间)
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [航标报警历史(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()

    @staticmethod
    def 更新报警时长(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标报警历史
LEFT JOIN 航标基础数据
ON 航标报警历史.hb_id = 航标基础数据.id
SET 航标报警历史.浮标 = 航标基础数据.hb_btlx,
航标报警历史.重点航标 = if(find_in_set( '10', hb_zdybq ),1,0),
航标报警历史.夜间 = if (HOUR(航标报警历史.scbjsj)>= 20 OR HOUR(航标报警历史.scbjsj)< 5,1,0),
航标报警历史.报警时长 = if((航标报警历史.czsj  is not null),(abs((unix_timestamp(航标报警历史.czsj) - unix_timestamp(航标报警历史.scbjsj))) / 60),NULL),
航标报警历史.单位 = 航标基础数据.单位,
航标报警历史.航标= 航标基础数据.hbmc'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 更新定级(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标报警历史
LEFT JOIN 最后调度视图
ON 航标报警历史.id=最后调度视图.报警id
SET 航标报警历史.最后调度时间 = 最后调度视图.最后调度时间,
航标报警历史.最后定级= 最后调度视图.最后定级,
航标报警历史.最后分类= 最后调度视图.最后分类'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 更新首次参照时间(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标报警历史
LEFT JOIN 参照视图
ON 航标报警历史.id=参照视图.报警id
SET 航标报警历史.首次参照时间 = 参照视图.首次参照时间,
 航标报警历史.首次参照时长 = if((航标报警历史.首次参照时间  is not null),(abs((unix_timestamp(航标报警历史.首次参照时间) - unix_timestamp(航标报警历史.scbjsj))) / 60),NULL)'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()

        # 关闭会话
        sqlsession.close()

    @staticmethod
    def 更新航标标签(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标报警历史
LEFT JOIN 航标基础数据
ON 航标报警历史.hb_id=航标基础数据.id
SET 航标报警历史.航标标签 = 航标基础数据.hb_zdybq'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()

        # 关闭会话
        sqlsession.close()
if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()


