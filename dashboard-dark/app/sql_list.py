
# 패턴으로 데이터 얻기
def GetNumber(seq, pt3, pt5, pt10, pt30):
    sql = f"""
         select sum(case when row_num = 1 then num end) as n1
              , sum(case when row_num = 2 then num end) as n2
              , sum(case when row_num = 3 then num end) as n3
              , sum(case when row_num = 4 then num end) as n4
              , sum(case when row_num = 5 then num end) as n5
              , sum(case when row_num = 6 then num end) as n6
              , '' as bin
              , sum(case when row_num = 1 then seq end) as n1_seq
              , sum(case when row_num = 2 then seq end) as n2_seq
              , sum(case when row_num = 3 then seq end) as n3_seq
              , sum(case when row_num = 4 then seq end) as n4_seq
              , sum(case when row_num = 5 then seq end) as n5_seq
              , sum(case when row_num = 6 then seq end) as n6_seq
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

    return sql