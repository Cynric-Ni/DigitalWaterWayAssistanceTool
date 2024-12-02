from sqlalchemy import Column, String, Integer, DateTime, Float, text, Text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表

Base = declarative_base()


class 失常分析:
    @staticmethod
    def 创建失常合并视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text(
            """create or replace view 失常合并视图 as
SELECT
	min( id ) AS 失常ID,单位,
	hb_id,航标,
	min( xdsj ) AS 失常时间,
	concat( DATE_FORMAT( xdsj, '%Y-%m-%d %H' ), ':00:00' ) AS 失常合并,
	max( wcsj ) AS 恢复时间,
	group_concat(失常类型) AS 失常类型合并 ,
	(unix_timestamp(max( wcsj )) - unix_timestamp(min( xdsj ))) / 60 AS 恢复时长,
	180 as 失常恢复时限
FROM
	航标失常恢复 
GROUP BY
	hb_id,失常合并;"""
        )

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 创建失常分析表(sqlsession):
        sql = text(
            """create table IF NOT EXISTS 失常分析 as
SELECT
t1.*,
t2.id AS 报警ID,
(case when t2.hb_bjlx =1 then '终端故障'
        when t2.hb_bjlx =2 then '参数未同步'
        when t2.hb_bjlx =3 then '航标灯报警'
        when t2.hb_bjlx =4 then '灯通讯报警'
        when t2.hb_bjlx =5 then '电压报警'
        when t2.hb_bjlx =6 then '定位无效'
        when t2.hb_bjlx =7 then '位移报警'
        when t2.hb_bjlx =8 then '漂移报警'
        when t2.hb_bjlx =9 then '超时报警' end )as 报警类型,
        t2.scbjsj as 报警开始时间,
        t2.czsj as 报警结束时间,
        t2.最后调度时间,
        t2.重点航标,
        t2.最后定级,
        t2.报警时长,
        t2.重要程度,
        t2.总时限,
        t2.时限修正,
        (CASE
        WHEN 最后定级 = 1  AND 重要程度 = 'A' THEN 1  #
        WHEN 最后定级 = 1  AND 重要程度 = 'B' THEN 2 
        WHEN 最后定级 = 1  AND 重要程度 = 'C' THEN 3 
        WHEN 重要程度 = 'A' AND 最后定级 = 2  THEN 4 
        WHEN 重要程度 = 'A' AND 最后定级 = 3  THEN 5 
        WHEN 重要程度 = 'A' AND 最后定级 IS NULL THEN 6 
        WHEN 重要程度 = 'B' AND 最后定级 = 2 THEN 22 
        WHEN 重要程度 = 'B' AND 最后定级 = 3 THEN 23 
        WHEN 重要程度 = 'B' AND 最后定级 IS NULL THEN 24 
        WHEN 重要程度 = 'C'  AND 最后定级 = 2 THEN 32 
        WHEN 重要程度 = 'C'  AND 最后定级 = 3 THEN 33 
        WHEN 重要程度 = 'C' AND 最后定级 IS NULL THEN 34 
        ELSE 99 END ) AS 重要程度排序 
        FROM
        失常合并视图 t1
        LEFT JOIN 报警分析视图 t2 ON t1.hb_id = t2.hb_id 
        AND (
        unix_timestamp( t1.失常时间 ) < unix_timestamp( t2.czsj ) AND unix_timestamp( t1.恢复时间 ) >= unix_timestamp( t2.scbjsj )) 
        ORDER BY
        失常ID,重要程度排序;"""
        )

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 创建失常分析视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text(
            """CREATE 
	OR REPLACE VIEW 失常分析视图 AS SELECT
	t1.*
FROM
	失常分析 t1
GROUP BY
	t1.失常ID;"""
        )

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()



'''
SELECT
	t1.*,
	(
	CASE	
			WHEN t1.报警ID IS NOT NULL AND t1.最后定级 = 1 AND t1.重要程度排序 < 10 	AND unix_timestamp( 失常时间 )> unix_timestamp( 最后调度时间 ) 
			THEN	最后调度时间 
			WHEN t1.报警ID IS NOT NULL AND t1.最后定级 != 1 AND t1.重要程度排序 < 10 AND 总时限 = 1440 AND unix_timestamp( 失常时间 )> unix_timestamp( 报警开始时间 )+(330 - 失常恢复时限)* 60 
			THEN	from_unixtime( unix_timestamp( 报警开始时间 )+( 330 - 失常恢复时限 )* 60 ) 
			WHEN t1.报警ID IS NOT NULL AND t1.最后定级 != 1 AND t1.重要程度排序 < 10 AND 总时限 != 1440 AND unix_timestamp( 失常时间 )> unix_timestamp( 报警开始时间 )+(总时限 - 失常恢复时限)* 60 
			THEN	from_unixtime( unix_timestamp( 报警开始时间 )+( 总时限 - 失常恢复时限 )* 60 ) 
			ELSE 失常时间	END 
					) AS 真失常时间,
			IF (t1.报警ID IS NOT NULL AND unix_timestamp( 恢复时间 )< unix_timestamp( 报警结束时间 ), 报警结束时间, 恢复时间 ) AS 真恢复时间,
	IF ((( t1.最后定级 = 1 AND unix_timestamp( 失常时间 )> unix_timestamp( 最后调度时间 )+ 10 * 60 ) 
	OR ( t1.报警ID IS NOT NULL AND unix_timestamp( 恢复时间 )< unix_timestamp( 报警结束时间 )- 10 * 60 )),0,1) AS 失常登记准确性,
	IF ((( t1.报警ID IS NULL OR t1.重要程度排序 > 10 ) AND 恢复时长 <= 失常恢复时限 ) 
	OR (t1.报警ID IS NOT NULL AND t1.重要程度排序 < 10 AND ( 报警时长 <= 失常恢复时限 + 30 OR 报警时长 <= 总时限 )),
	1,0 ) AS 失常恢复及时性,
	group_concat( t2.tgbh ) AS 通告编号   
			FROM
	失常分析视图 t1  LEFT JOIN 失常恢复通告 t2 ON  
	(
		unix_timestamp( t2.cjsj )< unix_timestamp( t1.恢复时间 ) 
	OR unix_timestamp( t2.cjsj )< unix_timestamp( t1.报警结束时间 )) 
	AND ( unix_timestamp( t2.cjsj )>= unix_timestamp( t1.失常时间 )- 3600 OR unix_timestamp( t2.cjsj )>= unix_timestamp( t1.报警开始时间 )- 3600 ) 
	AND tgnr LIKE concat( '%', 航标, '%' ) 
GROUP BY
	失常ID
	'''