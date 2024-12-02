from sqlalchemy import Column,String,DateTime,Float,text,Integer,Date,Text,BigInteger
from sqlalchemy.orm import declarative_base
from sql import sqlConfig
Base = declarative_base()

class 调度不合格明细(Base):
    __tablename__ = '调度不合格明细'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    单位 = Column(String(50))
    航标 = Column(String(50))
    是否为重点航标 = Column(Integer())
    sim卡号 = Column(BigInteger())
    报警类型 = Column(String(50))
    报警时间 = Column(DateTime())
    报警消除时间 = Column(DateTime())
    报警时长 = Column(Float())
    调度阶段 = Column(Integer())
    定级建议 = Column(Integer())
    分类建议 = Column(Integer())
    调度时间 = Column(DateTime())
    调度详情 = Column(Text)
    实际定级 = Column(Integer())
    实际分类 = Column(Integer())
    调度类型 = Column(String(50))
    是否参照其他报警调度 = Column(Integer())
    首次参照时间 = Column(DateTime())
    最后调度时间 = Column(DateTime())
    最后调度详情 = Column(Text)
    最后定级 = Column(Integer())
    最后分类 = Column(Integer())
    最后调度类型 = Column(String(50))
    调度是否合格 = Column(Integer())
    报警ID = Column(String(50))
    任务ID = Column(String(50))
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 明细(sqlsession):
        sql = text('''select REPLACE(UUID(), '-', '') as ID,
CURDATE() as 检查日期,
tt.单位 as 所属单位,
tt.航标 as 航标,
tt.重点航标 as 是否为重点航标,
tt.sim as sim卡号,
tt.报警类型 as 报警类型,
tt.scbjsj as 报警时间,
tt.czsj as 报警消除时间,
tt.报警时长 as 报警时长,
tt.调度阶段 as 调度阶段,
tt.定级建议 as 定级建议,
tt.分类建议 as 分类建议,
tt.rwsj as 调度时间,
tt.rwnr as 调度详情,
tt.定级 as 实际定级, 
tt.分类 as 实际分类,
tt.调度类型 as 调度类型,
tt.参照执行 as 是否参照其他报警调度,
tt.首次参照时间 as 首次参照时间,
tt.最后调度时间 as 最后调度时间,
tt.最后调度 as 最后调度详情,
tt.最后定级 as 最后定级,
tt.最后分类 as 最后分类 ,
tt.最后调度类型 as 最后调度类型 ,
tt.调度合格 as 调度是否合格,
tt.id as 报警ID,
tt.任务ID as 任务ID 
from(
SELECT
			t1.*,
			(case when t1.hb_bjlx =1 then '终端故障'
			when t1.hb_bjlx =2 then '参数未同步'
			when t1.hb_bjlx =3 then '航标灯报警'
			when t1.hb_bjlx =4 then '灯通讯报警'
			when t1.hb_bjlx =5 then '电压报警'
			when t1.hb_bjlx =6 then '定位无效'
			when t1.hb_bjlx =7 then '位移报警'
			when t1.hb_bjlx =8 then '漂移报警'
			when t1.hb_bjlx =9 then '超时报警' end )as 报警类型
			,
			(
			CASE
					WHEN t1.rwsj IS NULL THEN 
						CASE
								WHEN t1.报警时长 <= t1.最晚调度时限     
								OR ( t1.最后调度类型 IS NOT NULL AND unix_timestamp(t1.最后调度时间) < unix_timestamp( t1.scbjsj )+ t1.最早调度时限 * 60 ) THEN   
									NULL ELSE 0 
								END 
                    WHEN t1.rwsj IS NOT NULL THEN
                        CASE
                                WHEN length( t1.rwnr )< 20 THEN 0 
                                WHEN t1.rwsj < t1.最后调度时间 AND t1.调度类型 is  null  AND t1.最后调度类型 = '现场作业' THEN 0 
                                WHEN t1.rwsj < t1.最后调度时间 AND  t1.调度类型 != t1.最后调度类型 THEN 0 
																WHEN t1.rwsj < t1.最后调度时间 AND  t1.调度类型 = t1.最后调度类型 THEN 1 					
                                WHEN t1.定级 = t1.定级建议  AND t1.分类 = t1.分类建议   AND ( (t1.参照执行 IS NULL AND t1.rwnr NOT LIKE '%参照%') OR ( t1.参照执行 = 1 AND t1.rwnr LIKE '%参照%' )) THEN  1 
																WHEN (t1.hb_bjlx != 4 and t1.hb_bjlx != 9 and t1.hb_bjlx != 6 and t1.hb_bjlx != 3 and t1.hb_bjlx != 8) or 
																(t1.hb_bjlx = 6 and t1.异常编号='C43') or 
																((t1.hb_bjlx = 3 or t1.hb_bjlx = 8) AND t1.参照执行 is null) AND t1.调度类型 = '综合手段' 
																THEN 0 
                                WHEN t1.rwsj = t1.最后调度时间 AND ( t1.最后调度类型 = '现场作业' OR t1.最后调度类型 = '综合手段'   OR t1.最后调度类型 = '一级一类'  OR t1.最后调度类型 = '修正基点' ) THEN 1

                                ELSE 0 
                                END 
                    END 
                                            ) AS 调度合格 
                                        FROM
                                            调度分析视图 t1) tt
																						where tt.调度合格=0''')

        # 执行查询语句
        result = sqlsession.execute(sql)

        # 获取查询结果
        query_result = result.fetchall()
        # 关闭会话
        sqlsession.close()
        return query_result

    @staticmethod
    def 数据导入(数据,sqlsession):
        if len(数据)!=0:
            for i in 数据:
                异常 = 调度不合格明细(
                    ID=i[0],
                    检查日期=i[1],
                    单位=i[2],
                    航标=i[3],
                    是否为重点航标=i[4],
                    sim卡号=i[5],
                    报警类型=i[6],
                    报警时间=i[7],
                    报警消除时间=i[8],
                    报警时长=i[9],
                    调度阶段=i[10],
                    定级建议=i[11],
                    分类建议=i[12],
                    调度时间=i[13],
                    调度详情=i[14],
                    实际定级=i[15],
                    实际分类=i[16],
                    调度类型=i[17],
                    是否参照其他报警调度=i[18],
                    首次参照时间=i[19],
                    最后调度时间=i[20],
                    最后调度详情=i[21],
                    最后定级=i[22],
                    最后分类=i[23],
                    最后调度类型=i[24],
                    调度是否合格=i[25],
                    报警ID=i[26],
                    任务ID=i[27]
                )
                sqlsession.add(异常)
            sqlsession.commit()
if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    调度不合格明细.建表(调度不合格明细,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()