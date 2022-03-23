import app.sql_list.dbconfig as dbConf

###############################################################
###############################################################
# 당첨 결과값 가져오기
def GetWin():
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = """
        select seq, n1, n2, n3, n4, n5, n6
          from innodb.lotto
         where 1=1
           and seq between 990 and (select max(seq) from innodb.lotto)
         order by 1 desc
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source
###############################################################
###############################################################

###############################################################
###############################################################
# 최신 당첨 번호 가져오기 
def GetLastWin():
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = """
        select seq, n1, n2, n3, n4, n5, n6
          from innodb.lotto
         where 1=1
           and seq = (select max(seq) from innodb.lotto)
         order by 1 desc
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source
###############################################################
###############################################################

###############################################################
###############################################################
# 당첨 패턴 가져오기
def GetWinPatten():
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = """
        select stan  as seq
             , 3cnt  as 3cnt
             , 5cnt  as 5cnt 
             , 10cnt as 10cnt 
             , 30cnt as 30cnt
          from in_list_2
         order by 1 desc
         limit 10
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source
###############################################################
###############################################################

###############################################################
###############################################################
# 패턴으로 데이터 얻기
def GetNumber(seq, pt3, pt5, pt10, pt30):
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = f"""
       select sum(case when row_num = 1 then num end) as n1
        , sum(case when row_num = 2 then num end) as n2
              , sum(case when row_num = 3 then num end) as n3
              , sum(case when row_num = 4 then num end) as n4
              , sum(case when row_num = 5 then num end) as n5
              , sum(case when row_num = 6 then num end) as n6
              , '' as bin
              , sum(case when row_num = 1 then seq end) as pt1
              , sum(case when row_num = 2 then seq end) as pt2
              , sum(case when row_num = 3 then seq end) as pt3
              , sum(case when row_num = 4 then seq end) as pt4
              , sum(case when row_num = 5 then seq end) as pt5
              , sum(case when row_num = 6 then seq end) as pt6
           from (
         select num
              , @rownum:=@rownum+1 as row_num
              , seq
           from (
                select seq, num   
                  from (select 3 as seq, num
                          from innodb.in_list 
                         where seq = {seq}
                           and val = 3 
                         order by rand() 
                         limit {pt3}
                       ) as t3
                union all
                select seq, num   
                  from (select 5 as seq, num
                          from innodb.in_list 
                         where seq = {seq}
                           and val = 5 
                         order by rand() 
                         limit {pt5}
                       ) as t5 
                union all
                select seq, num   
                  from (select 10 as seq, num
                          from innodb.in_list 
                         where seq = {seq}
                           and val = 10
                         order by rand() 
                         limit {pt10}
                       ) as t10
                union all
                select seq, num   
                from (select 30 as seq, num
                        from innodb.in_list 
                       where seq = {seq}
                         and val = 30 
                       order by rand() 
                       limit {pt30}
                     ) as t30
                 order by num 
             ) as a
             , (SELECT @rownum:=0) TMP
             ) as b 
         ;
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source
###############################################################
###############################################################







