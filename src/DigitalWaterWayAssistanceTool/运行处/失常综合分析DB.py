from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
from .sql import sqlConfig
from .船舶轨迹查询 import 船舶轨迹查询
Base = declarative_base()

class 失常综合分析(Base):
    __tablename__ = '失常综合分析'
    失常ID = Column(String(50), primary_key=True,unique=True)  # id
    单位 = Column(String(50))
    hb_id = Column(String(50), index=True)
    航标 = Column(String(50))
    失常时间 = Column(DateTime())
    失常合并 = Column(DateTime())
    恢复时间 = Column(DateTime())
    失常类型合并 = Column(String(255))
    恢复时长 = Column(Float())
    失常恢复时限 = Column(Integer())
    报警ID = Column(String(50))
    报警类型 = Column(String(50))
    报警开始时间 = Column(DateTime())
    报警结束时间 = Column(DateTime())
    最后调度时间 = Column(DateTime())
    重点航标 = Column(Integer())
    最后定级 = Column(Integer())
    报警时长 = Column(Float())
    重要程度 = Column(String(50))
    总时限 = Column(Integer())
    时限修正 = Column(Integer())
    重要程度排序 = Column(Integer())
    真失常时间 = Column(DateTime())
    真恢复时间 = Column(DateTime())
    失常登记准确性 = Column(Integer())
    失常恢复及时性 = Column(Integer())
    通告编号 = Column(String(255))
    维护船舶 = Column(String(50))
    到达现场时间 = Column(DateTime())
    现场距离 = Column(Float())
    基点经度 = Column(Float())
    基点纬度 = Column(Float())
    航道里程 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession,库名):
        sql = text(
            f"""INSERT IGNORE INTO 失常综合分析
SELECT tt1.*,tt2.jdzbjd as 基点经度,tt2.jdzbwd as 基点纬度,tt2.jdlc as 航道里程 FROM(SELECT
	t1.*,
 (case 	when t1.报警ID IS NOT NULL  and t1.最后定级=1 and t1.重要程度排序 < 10 and unix_timestamp( 失常时间 )> unix_timestamp( 最后调度时间 )
            	then 最后调度时间
        when t1.报警ID IS NOT NULL  and t1.最后定级 !=1 and	t1.重要程度排序 < 10 and 	时限修正 is not null and  unix_timestamp( 失常时间 )> unix_timestamp( 报警开始时间 )+(时限修正 - 失常恢复时限)* 60
            	then from_unixtime( unix_timestamp( 报警开始时间 )+( 时限修正 - 失常恢复时限 )* 60 )
        when t1.报警ID IS NOT NULL  and  t1.最后定级 !=1 and  t1.重要程度排序 < 10 and  时限修正 is null and 	unix_timestamp( 失常时间 )> unix_timestamp( 报警开始时间 )+(总时限 - 失常恢复时限)* 60
            	then from_unixtime( unix_timestamp( 报警开始时间 )+( 总时限 - 失常恢复时限 )* 60 )
        ELSE 失常时间 end)AS 真失常时间,
			IF (t1.报警ID IS NOT NULL AND unix_timestamp( 恢复时间 )< unix_timestamp( 报警结束时间 ), 报警结束时间, 恢复时间 ) AS 真恢复时间,
	IF ((( t1.最后定级 = 1 AND unix_timestamp( 失常时间 )> unix_timestamp( 最后调度时间 )+ 10 * 60 ) 
	OR ( t1.报警ID IS NOT NULL AND unix_timestamp( 恢复时间 )< unix_timestamp( 报警结束时间 )- 10 * 60 )),0,1) AS 失常登记准确性,
	IF ((( t1.报警ID IS NULL OR t1.重要程度排序 > 10 ) AND 恢复时长 <= 失常恢复时限 ) 
	OR (t1.报警ID IS NOT NULL AND t1.重要程度排序 < 10 AND ( 报警时长 <= 失常恢复时限 + 30 OR 报警时长 <= 总时限 )),
	1,0 ) AS 失常恢复及时性,
	group_concat( t2.tgbh ) AS 通告编号,null as 维护船舶,null as 到达现场时间,null as 现场距离   
			FROM
	`{库名}`.`失常分析视图` t1  LEFT JOIN `{库名}`.`失常恢复通告` t2 ON  
	(
		unix_timestamp( t2.cjsj )< unix_timestamp( t1.恢复时间 ) 
	OR unix_timestamp( t2.cjsj )< unix_timestamp( t1.报警结束时间 )) 
	AND ( unix_timestamp( t2.cjsj )>= unix_timestamp( t1.失常时间 )- 3600 OR unix_timestamp( t2.cjsj )>= unix_timestamp( t1.报警开始时间 )- 3600 ) 
	AND tgnr LIKE concat( '%', 航标, '%' ) 
GROUP BY
	失常ID)tt1 LEFT JOIN `{库名}`.`航标基础数据` tt2 on tt1.hb_id=tt2.id;"""
        )

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 更新到达时间_主中心(sqlsession,engine,分中心Session,分中心UA伪装,主中心Session,主中心UA伪装,库名):
        失常航标船舶匹配 = 船舶轨迹查询.匹配(sqlsession,库名)
        sqltext = text('''
                       UPDATE 失常综合分析
                       SET
                           维护船舶 = :维护船舶,
                           到达现场时间 = :到达现场时间,
                           现场距离 = :现场距离
                       WHERE 失常ID = :失常ID
                   ''')
        for i in range(0, len(失常航标船舶匹配)):
            航标轨迹=船舶轨迹查询.航标轨迹查询(分中心Session,分中心UA伪装,失常航标船舶匹配.loc[i, "真失常时间"],失常航标船舶匹配.loc[i, "真恢复时间"],失常航标船舶匹配.loc[i, "hb_id"])
            船舶轨迹= 船舶轨迹查询.主中心船舶轨迹查询(主中心Session, 主中心UA伪装,失常航标船舶匹配.loc[i, '真失常时间'],失常航标船舶匹配.loc[i, '真恢复时间'],失常航标船舶匹配.loc[i, '船舶ID'])
            到达现场时间,到达现场位置 = 船舶轨迹查询.计算到达现场时间(
                航标轨迹,
                船舶轨迹,
                失常航标船舶匹配.loc[i, '基点经度'],
                失常航标船舶匹配.loc[i, '基点纬度']
            )
            现场距离=None
            维护船舶=失常航标船舶匹配.loc[i, "船舶名称"]
            失常ID=失常航标船舶匹配.loc[i, "失常ID"]
            if 到达现场时间 is not  None :
                现场距离 = 船舶轨迹查询.获取里程信息(engine, 船舶轨迹,到达现场位置)
                # 提供参数字典
                sqlsession.execute(sqltext, {
                    '维护船舶': 维护船舶,
                    '到达现场时间': 到达现场时间,
                    '现场距离': 现场距离,
                    '失常ID': 失常ID
                })
        # 提交事务
        sqlsession.commit()

    @staticmethod
    def 更新到达时间_分中心(sqlsession,engine,分中心Session,分中心UA伪装,库名):
        失常航标船舶匹配 = 船舶轨迹查询.匹配(sqlsession,库名)
        sqltext = text('''
                       UPDATE 失常综合分析
                       SET
                           维护船舶 = :维护船舶,
                           到达现场时间 = :到达现场时间,
                           现场距离 = :现场距离
                       WHERE 失常ID = :失常ID
                   ''')
        for i in range(0, len(失常航标船舶匹配)):
            航标轨迹=船舶轨迹查询.航标轨迹查询(分中心Session,分中心UA伪装,失常航标船舶匹配.loc[i, "真失常时间"],失常航标船舶匹配.loc[i, "真恢复时间"],失常航标船舶匹配.loc[i, "hb_id"])
            船舶轨迹= 船舶轨迹查询.分中心船舶轨迹查询(分中心Session, 分中心UA伪装,失常航标船舶匹配.loc[i, '真失常时间'],失常航标船舶匹配.loc[i, '真恢复时间'],失常航标船舶匹配.loc[i, '船舶ID'])
            到达现场时间,到达现场位置 = 船舶轨迹查询.计算到达现场时间(
                航标轨迹,
                船舶轨迹,
                失常航标船舶匹配.loc[i, '基点经度'],
                失常航标船舶匹配.loc[i, '基点纬度']
            )
            现场距离=None
            维护船舶=失常航标船舶匹配.loc[i, "船舶名称"]
            失常ID=失常航标船舶匹配.loc[i, "失常ID"]
            if 到达现场时间 is not  None :
                现场距离 = 船舶轨迹查询.获取里程信息(engine, 船舶轨迹,到达现场位置)
                # 提供参数字典
                sqlsession.execute(sqltext, {
                    '维护船舶': 维护船舶,
                    '到达现场时间': 到达现场时间,
                    '现场距离': 现场距离,
                    '失常ID': 失常ID
                })
        # 提交事务
        sqlsession.commit()

    @staticmethod
    def 失常综合分析(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text(
            '''SELECT
  t2.单位,
  COALESCE(t1.失常数量, 0) AS 失常数量,
  CONCAT(ROUND(t1.失常登记准确率 * 100, 2), '%') AS 失常登记准确率,
  ROUND(t1.失常恢复时长, 2) AS 失常恢复时长,
  COALESCE(t1.失常数量_排通告, 0) AS 失常数量_排通告,
  ROUND(t1.到达现场时长, 2) AS 到达现场时长,
  ROUND(t1.失常恢复效率, 2) AS 失常恢复效率,
  CONCAT(ROUND(t1.失常及时恢复率 * 100, 2), '%') AS 失常及时恢复率
FROM
  基础数据.基层处 t2
  LEFT JOIN (
    SELECT
      单位,
      COUNT(*) as 失常数量,
      SUM(失常登记准确性)/COUNT(*) as 失常登记准确率,
      AVG(unix_timestamp(真恢复时间) - unix_timestamp(真失常时间)) / 3600 AS 失常恢复时长,
			COUNT(CASE WHEN 通告编号 IS NULL THEN 1 END) AS 失常数量_排通告,
			AVG(CASE WHEN 通告编号 IS NULL THEN unix_timestamp(到达现场时间) - unix_timestamp(真失常时间) END) / 60 AS 到达现场时长,
			AVG(CASE WHEN 通告编号 IS NULL THEN ((unix_timestamp(到达现场时间) - unix_timestamp(真失常时间)) / 60 / 现场距离) + ((unix_timestamp(真恢复时间) - unix_timestamp(到达现场时间)) / 60) END) AS 失常恢复效率,
			SUM(CASE WHEN 通告编号 IS NULL THEN 失常恢复及时性 END) / COUNT(CASE WHEN 通告编号 IS NULL THEN 1 END) AS 失常及时恢复率
    FROM
      失常综合分析
			WHERE YEAR(恢复时间) = YEAR(CURDATE()) 
    GROUP BY
      单位 
			UNION ALL
			SELECT
				'总计' AS 单位,
				COUNT(*) AS 失常数量,
				SUM(失常登记准确性) / COUNT(*) AS 失常登记准确率,
				AVG(unix_timestamp(真恢复时间) - unix_timestamp(真失常时间)) / 3600 AS 失常恢复时长,
				COUNT(CASE WHEN 通告编号 IS NULL THEN 1 END)  AS 失常数量_排通告,
				AVG(CASE WHEN 通告编号 IS NULL THEN unix_timestamp(到达现场时间) - unix_timestamp(真失常时间) END) / 60 AS 到达现场时长,
				AVG(CASE WHEN 通告编号 IS NULL THEN ((unix_timestamp(到达现场时间) - unix_timestamp(真失常时间)) / 60 / 现场距离) + ((unix_timestamp(真恢复时间) - unix_timestamp(到达现场时间)) / 60) END) AS 失常恢复效率,
				SUM(CASE WHEN 通告编号 IS NULL THEN 失常恢复及时性 END) / COUNT(CASE WHEN 通告编号 IS NULL THEN 1 END) AS 失常及时恢复率
			FROM
				失常综合分析
				WHERE YEAR(恢复时间) = YEAR(CURDATE()) 
  ) t1 ON t2.单位 = t1.单位 
ORDER BY
  基础数据.机构排序(t2.单位);'''
        )

        # 执行查询语句
        result = sqlsession.execute(sql)

        # 获取查询结果
        query_result = result.fetchall()

        return query_result

if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    失常综合分析.建表(失常综合分析,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()

