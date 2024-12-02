from sqlalchemy import Column,String,DateTime,Float,text,Integer,Date,Text
from sqlalchemy.orm import declarative_base
from sql import sqlConfig
Base = declarative_base()

class 调度合格率(Base):
    __tablename__ = '调度合格率'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    调度合格数 = Column(Integer())
    调度总数 = Column(Integer())
    调度合格率 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 统计(sqlsession):
        sql = text('''select 
REPLACE(UUID(), '-', '') as ID,
CURDATE() as 检查日期,
sum(调度合格) as 调度合格数,
count(调度合格) as 调度总数,
ROUND( sum(调度合格)/count(调度合格) * 100, 2) AS 合格率
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
                                            调度分析视图 t1) tt''')

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
                异常 = 调度合格率(
                    ID=i[0],
                    检查日期=i[1],
                    调度合格数=i[2],
                    调度总数=i[3],
                    调度合格率=i[4]
                )
                sqlsession.add(异常)
            sqlsession.commit()
if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    调度合格率.建表(调度合格率,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()