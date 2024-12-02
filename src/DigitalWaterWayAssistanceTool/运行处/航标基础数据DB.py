from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 航标基础数据(Base):
    __tablename__ = '航标基础数据'
    id = Column(String(255), primary_key=True,unique=True,index=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hbmc = Column(String(50))
    hb_hbdl = Column(String(50))
    hb_hbxl = Column(Integer())
    ssjg_id = Column(Integer())
    pbtj = Column(String(255))
    hbtb_id = Column(String(50))
    hb_btlx = Column(Integer())
    jdlc = Column(Float())
    ty_anb = Column(Integer())
    jdzbjd = Column(Float())
    jdzbwd = Column(Float())
    hb_sbzt = Column(Integer())
    sshd_id = Column(String(255))
    zsbz = Column(Integer())
    hb_zdybq = Column(String(50))
    wymx = Column(Float())
    pymx = Column(Float())
    zxhxjl = Column(Float())
    hb_hbxz = Column(Integer())
    sjbw_id = Column(String(255))
    sjbwzb_id = Column(String(255))
    flag = Column(Integer())
    hb_syzt = Column(Integer())
    qyjcs = Column(Integer())
    fdd = Column(Integer())
    jzsj = Column(DateTime())
    单位 = Column(String(50))
    终端 = Column(String(50))
    厂家 = Column(String(50))
    航标灯类型 = Column(String(50))
    上数时间 = Column(DateTime())
    应为重点航标 = Column(Integer())
    日光阈值 = Column(Float())
    轮询周期 = Column(Integer())
    报警周期 = Column(Integer())
    终端高电压阈值 = Column(Float())
    终端低电压阈值 = Column(Float())
    航标灯高电压阈值 = Column(Float())
    航标灯低电压阈值 = Column(Float())
    理论位移阈值 = Column(Integer())
    理论漂移阈值 = Column(Integer())
    理论日光阈值  = Column(Integer())
    理论轮询周期 = Column(Integer())
    理论报警周期= Column(Integer())
    理论终端高电压阈值 = Column(Float())
    理论终端低电压阈值 = Column(Float())
    理论航标灯高电压阈值 = Column(Float())
    理论航标灯低电压阈值 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        data= 数据导出.航标基础数据导出()
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        objects = [航标基础数据(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配单位(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标基础数据 
        JOIN 基础数据.组织机构 
        ON 航标基础数据.ssjg_id = 基础数据.组织机构.ID 
        SET 航标基础数据.单位 = 基础数据.组织机构.单位'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配动态(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标基础数据 
        JOIN 航标动态数据
        ON 航标基础数据.id = 航标动态数据.hb_id 
        SET 航标基础数据.终端 = 航标动态数据.hbzd_id , 航标基础数据.上数时间 = 航标动态数据.sbsj'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()

    @staticmethod
    def 检查标签(sqlsession):
        标签检查sql = text('''UPDATE 航标基础数据
	JOIN 基础数据.重点航标清单 ON 航标基础数据.HBMC = 基础数据.重点航标清单.航标 
	SET 航标基础数据.应为重点航标 = 1;''')
        # 执行查询语句
        sqlsession.execute(标签检查sql)
        sqlsession.commit()

    @staticmethod
    def 检查阈值(sqlsession):
        理论位移阈值sql=text('''
        UPDATE 航标基础数据 t1
LEFT JOIN 基础数据.阈值特批清单 t3
ON t1.hbmc = t3.航标 
AND (
    (MONTH(NOW()) BETWEEN 6 AND 10 AND t3.时期 = '汛期') 
    OR 
    (MONTH(NOW()) NOT BETWEEN 6 AND 10 AND t3.时期 = '非汛期')
)
LEFT JOIN 基础数据.阈值规定 t2 ON (
    (
        ( t1.hb_btlx = 1 AND t2.航标类型 = '浮标' ) 
        AND (
            ( MONTH ( NOW()) BETWEEN 6 AND 10 AND t2.时期 = '汛期' ) 
            OR ( MONTH ( NOW()) NOT BETWEEN 6 AND 10 AND t2.时期 = '非汛期' ) 
        ) 
        AND (
            ( find_in_set( '10', t1.hb_zdybq ) AND t2.航标重要程度 = '重点' ) 
            OR ( NOT find_in_set( '10', t1.hb_zdybq ) AND t2.航标重要程度 = '一般' ) 
        ) 
    ) 
    OR ( t1.hb_btlx = 2 AND t2.航标类型 = '岸标' ) 
) 
SET 
    t1.理论位移阈值 = COALESCE(t3.理论位移阈值, t2.理论位移阈值),
    t1.理论漂移阈值 = COALESCE(t3.理论漂移阈值, t2.理论漂移阈值),
		t1.理论日光阈值 =t2.理论日光阈值,
		t1.理论轮询周期 = t2.理论轮询周期,
		t1.理论报警周期 = t2.理论报警周期;
''')
        sqlsession.execute(理论位移阈值sql)
        sqlsession.commit()


        理论电压阈值sql=text('''
                UPDATE 航标基础数据 t1
LEFT JOIN 基础数据.电压阈值规定 t2 ON 
t1.航标灯类型=t2.航标灯类型 and
t1.厂家=t2.厂家
SET 
    t1.理论终端高电压阈值 = t2.理论终端高电压阈值,
    t1.理论终端低电压阈值 = t2.理论终端低电压阈值,
		t1.理论航标灯高电压阈值 =t2.理论航标灯高电压阈值,
		t1.理论航标灯低电压阈值 = t2.理论航标灯低电压阈值;
        ''')
        sqlsession.execute(理论电压阈值sql)
        sqlsession.commit()

    @staticmethod
    def 匹配终端(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标基础数据 
        JOIN 终端数据
        ON 航标基础数据.id = 终端数据.hb_id 
        SET 航标基础数据.终端高电压阈值 = 终端数据.zddygmx, 
        航标基础数据.终端低电压阈值 = 终端数据.zddydmx,
        航标基础数据.航标灯高电压阈值=终端数据.dygmx,
        航标基础数据.航标灯低电压阈值=终端数据.dydmx,
        航标基础数据.日光阈值=终端数据.rgyz,
        航标基础数据.轮询周期=终端数据.lxzq,
        航标基础数据.报警周期=终端数据.bjzq,
        航标基础数据.厂家=终端数据.cj'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配航标灯类型(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 航标基础数据 
LEFT JOIN  航标器材配置
ON 航标基础数据.id = 航标器材配置.hb_id
SET 航标基础数据.航标灯类型 = CASE 
    WHEN (find_in_set('010701', 航标器材配置.qclx_id)  or find_in_set('010703', 航标器材配置.qclx_id) or find_in_set('010702', 航标器材配置.qclx_id)) and not find_in_set('010901', 航标器材配置.qclx_id)  and not find_in_set('01070101', 航标器材配置.qcgg_id) THEN  '一体化RTU'
    WHEN find_in_set('010901', 航标器材配置.qclx_id) or find_in_set('01070101', 航标器材配置.qcgg_id) THEN '分体式' 
    ELSE
        航标基础数据.航标灯类型
END;'''
        )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()



if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()
    航标基础数据.建表(engine)
    航标基础数据.数据导入(sqlsession)
    航标基础数据.匹配单位(sqlsession)
    #建航标动态表
    航标基础数据.匹配动态(sqlsession)
    #需要测试解绑后是否匹配到终端
    #建航标终端信息表
