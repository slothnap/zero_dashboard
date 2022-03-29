import app.sql_list.dbconfig as dbConf


###############################################################
###############################################################
# 당첨 결과값 가져오기
def GetWin(seq_first, seq_last):
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = f"""
        select seq, n1, n2, n3, n4, n5, n6
          from innodb.lotto
         where 1=1
           and seq between {seq_first} and {seq_last}
         order by 1 desc
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source
###############################################################
###############################################################


###############################################################
###############################################################
# 당첨 비율 가져오기 
def GetRateWin(seq_first, seq_last):
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = f"""
        select ifnull(sum(case when num between 1  and 9  then 1 end),0) r1
             , ifnull(sum(case when num between 10 and 19 then 1 end),0) r10
             , ifnull(sum(case when num between 20 and 29 then 1 end),0) r20
             , ifnull(sum(case when num between 30 and 39 then 1 end),0) r30
             , ifnull(sum(case when num between 40 and 45 then 1 end),0) r40
          from innodb.temp2
         where 1=1
           and seq between {seq_first} and {seq_last}
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source
###############################################################
###############################################################



###############################################################
###############################################################
# 번호 출현 횟수 가져오기
def GetNumAllCnt(seq_first, seq_last):
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = f"""
        select num
             , count(*) cnt 
          from innodb.temp2
         where seq between {seq_first} and {seq_last}
         group by num 
         order by 2 desc
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

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

###############################################################
###############################################################
# 패턴으로 데이터 얻기
def GetNumber(pt3, pt5, pt10, pt30):
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
                         where seq = (select max(seq) from innodb.lotto)
                           and val = 3 
                         order by rand() 
                         limit {pt3}
                       ) as t3
                union all
                select seq, num   
                  from (select 5 as seq, num
                          from innodb.in_list 
                         where seq = (select max(seq) from innodb.lotto)
                           and val = 5 
                         order by rand() 
                         limit {pt5}
                       ) as t5 
                union all
                select seq, num   
                  from (select 10 as seq, num
                          from innodb.in_list 
                         where seq = (select max(seq) from innodb.lotto)
                           and val = 10
                         order by rand() 
                         limit {pt10}
                       ) as t10
                union all
                select seq, num   
                from (select 30 as seq, num
                        from innodb.in_list 
                       where seq = (select max(seq) from innodb.lotto)
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


###############################################################
###############################################################
# 당첨 패턴 후 경우의 수 가져오기
def Next_patten(p1, p2, p3, p4):
  zeroDb = dbConf.DbConfig("zero")
  zeroDb.opendb()

  sql = f"""
        select 3cnt 
             , 5cnt 
             , 10cnt 
             , 30cnt
             , count(*) cnt
          from in_list_2 
         where 1=1 
           and stan in (
                        select stan + 1
                          from in_list_2
                         where 1=1 
                           and 3cnt  = {p1}
                           and 5cnt  = {p2}
                           and 10cnt = {p3}
                           and 30cnt = {p4}
                       ) 
         group by 3cnt, 5cnt, 10cnt, 30cnt
         order by cnt desc;
        """
  source = zeroDb.select(sql)
  zeroDb.closedb()

  return source




