#!/usr/bin/python
#encoding=utf-8

'''
流量概览
'''

import time
import datetime
import sys
sys.path.append("/home/hive/py/libs")
from utils.MailUtils import SendMail
from database.Database import ImpalaDB
from database.Database import OracleDB


def main(curday):
    year = curday[0:4]
    month = curday[5:7]
    day = curday[8:10]

    oracleDB = OracleDB()

    try:
        starttime = datetime.datetime.now()

        impalaDB = ImpalaDB()
        impalaDB.open()
        #impalaDB.refreshAll()
        impalaDB.refresh('tbl_analytics')
        impalaDB.close()

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #1.访客数:visit_type:2 表示指定的某天的全部访次， visit_type 1 表示只有一个访次的
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        selectSQL = """
        select * from (
        SELECT
        count(distinct utm_aid, visit_count) as visit_count,
        2,
        create_date,
        case
        when host_name = 'www.yougou.com' then 1
        when host_name = 'outlets.yougou.com' then 2
        when host_name = 'flashbuy.yougou.com' then 3
        when host_name = 'seoul.yougou.com' then 5
        when host_name = 'm.yougou.com' then 9
        else 1
        end site_no
        FROM tbl_analytics
        where analytic_type = 0
        and year = '%s'
        and month = '%s'
        and day = '%s'
        GROUP BY create_date,
        case
        when host_name = 'www.yougou.com' then 1
        when host_name = 'outlets.yougou.com' then 2
        when host_name = 'flashbuy.yougou.com' then 3
        when host_name = 'seoul.yougou.com' then 5
        when host_name = 'm.yougou.com' then 9
        else 1 end
        union all
        SELECT
        count(distinct utm_aid, visit_count) as visit_count,
        1,
        create_date,
        case
        when host_name = 'www.yougou.com' then 1
        when host_name = 'outlets.yougou.com' then 2
        when host_name = 'flashbuy.yougou.com' then 3
        when host_name = 'seoul.yougou.com' then 5
        when host_name = 'm.yougou.com' then 9
        else 1
        end site_no
        FROM tbl_analytics
        where analytic_type = 0 and  utm_ah in ('95907011','156676019')
        and visit_count = 1
        and year = '%s'
        and month = '%s'
        and day = '%s'
        GROUP BY create_date,
        case
        when host_name = 'www.yougou.com' then 1
        when host_name = 'outlets.yougou.com' then 2
        when host_name = 'flashbuy.yougou.com' then 3
        when host_name = 'seoul.yougou.com' then 5
        when host_name = 'm.yougou.com' then 9
        else 1 end) tmp
        """ % (year, month, day,year, month, day)
        impalaDB = ImpalaDB()
        impalaDB.open()
        results = impalaDB.select(selectSQL)
        impalaDB.close()
        endtime = datetime.datetime.now()
        print "[访客数查询] costs  :   %ds" % (endtime - starttime).seconds

        if len(results) == 0:
            return False

        oracleDB.execute("""delete from log_visit_volume_new where   report_date='%s'""" % (curday))
        '''插入oracle'''
        insertSQL = """insert into log_visit_volume_new(visit_count,visit_type,create_date,report_date,site_no) values(:1,:2,sysdate,:3,:4)"""

        params = []
        count = len(results)
        counter = 0
        for row in results:
            count -= 1
            counter += 1
            items = row.split("\t")
            params.append((items[0],int(items[1]),curday,int(items[3])))
            try:
                if counter == 1000:
                    oracleDB.batchUpdate(insertSQL, params)
                    params = []
                    counter = 0
                elif count == 0:
                    oracleDB.batchUpdate(insertSQL, params)
                    break
            except:
                params = []
                counter = 0
                info=sys.exc_info()
                print info[0],":",info[1]
                SendMail("%s [web_page_overview_hour_new中各平台访次数据] except %s:%s" % (curday,info[0],info[1]))

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #1.全站访客数：将优购站和首尔站的访次合并，即优购PC和首尔站的总访次
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        selectSQL = """
        select * from (
        SELECT
        count(distinct utm_aid, visit_count) as visit_count,
        2 visit_type
        FROM tbl_analytics
        where analytic_type = 0
        and year = '%s'
        and month = '%s'
        and day = '%s'
        and (host_name = 'www.yougou.com' or host_name = 'seoul.yougou.com')
        union all
        SELECT
        count(distinct utm_aid, visit_count) as visit_count,
        1 visit_type
        FROM tbl_analytics
        where analytic_type = 0
        and utm_ah in ('95907011','156676019')
        and visit_count = 1
        and year = '%s'
        and month = '%s'
        and day = '%s'
        and (host_name = 'www.yougou.com' or host_name = 'seoul.yougou.com')
        ) tmp
        """ % (year, month, day,year, month, day)
        impalaDB = ImpalaDB()
        impalaDB.open()
        results = impalaDB.select(selectSQL)
        impalaDB.close()
        endtime = datetime.datetime.now()
        print "[全站访客数] [Hive] Total time costs  :   %ds" % (endtime - starttime).seconds

        if len(results) == 0:
            return False


        oracleDB.execute("""delete from log_visit_volume_new where site_no=21 and  report_date='%s' """ % (curday))
        '''插入oracle'''
        insertSQL = """insert into log_visit_volume_new(visit_count,visit_type,create_date,report_date,site_no) values(:1,:2,sysdate,:3,:4)"""

        params = []
        count = len(results)
        counter = 0
        for row in results:
            count -= 1
            counter += 1
            items = row.split("\t")
            params.append((items[0],int(items[1]),curday,21))
            try:
                if counter == 1000:
                    oracleDB.batchUpdate(insertSQL, params)
                    params = []
                    counter = 0
                elif count == 0:
                    oracleDB.batchUpdate(insertSQL, params)
                    break
            except:
                params = []
                counter = 0
                info=sys.exc_info()
                print info[0],":",info[1]
                SendMail("%s [web_page_overview_hour_new中优购PC和首尔站的总访次] except %s:%s" % (curday,info[0],info[1]))

        return True

    except:
        SendMail("%s [web_page_overview_hour_new] except" % (curday))
        info=sys.exc_info()
        print info[0],":",info[1]
        return False


if __name__=='__main__':
    print ""
    if(len(sys.argv)==1):
        curday=sys.argv[0]

        starttime = datetime.datetime.now()
        print "[%s] [%s] [web_page_overview_hour_new] runing..." % (curday, starttime)
        main(curday)
        endtime = datetime.datetime.now()
        print "[%s] [%s] [web_page_overview_hour_new] 执行一共花费  :   %ds" % (curday, endtime, (endtime - starttime).seconds)
        #SendMail("[%s] [%s] [web_page_pv_h] %ds" % (curday, endtime,(endtime - starttime).seconds))